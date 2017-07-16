from django.contrib import admin
from django import forms
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

from .models import *

@admin.register(Signing)
class SigningAdmin(admin.ModelAdmin):
    list_display = ('show', 'character', 'actor', 'response')
    list_editable = ('response',)
    list_display_links = None
    search_fields = ('actor', 'show', 'character')
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False


CASTING_RELEASE_TIME_LOCKS = ("publish_callbacks", "publish_first_round_casts",
                              "publish_casts")
CASTING_RELEASE_LOCK_TIME = timedelta(minutes=10)
def is_locked(dt):
    return dt and (dt - CASTING_RELEASE_LOCK_TIME < timezone.now())
    
class CastingReleaseForm(forms.ModelForm):
    def clean_publish_callbacks(self):
        if (is_locked(self.instance.publish_callbacks) or
            self.instance.stage > 0):
            raise forms.ValidationError(
                "Cannot change callback publishing time, it is too soon or "
                "has already passed.")
        return self.cleaned_data["publish_callbacks"]

    def clean_publish_first_round_casts(self):
        if (is_locked(self.instance.publish_first_round_casts) or
            self.instance.stage > 1):
            raise forms.ValidationError(
                "Cannot change first-round cast list publishing time, it is "
                "too soon or has already passed.")
        return self.cleaned_data["publish_first_round_casts"]
        
    def clean_publish_casts(self):
        if (is_locked(self.instance.publish_casts) or
            self.instance.stage > 2):
            raise forms.ValidationError(
                "Cannot change cast list publishing time, it is "
                "too soon or has already passed.")
        return self.cleaned_data["publish_casts"]

    def clean_signing_option_field(self):
        if is_locked(self.instance.publish_casts) or self.instance.stage > 2:
            raise forms.ValidationError("Cannot change signing options after "
                                        "casts have been published.")
    
    def clean_signing_opens(self):
        self.clean_signing_option_field()
        return self.cleaned_data["signing_opens"]
    
    def clean_second_signing_opens(self):
        self.clean_signing_option_field()
        return self.cleaned_data["second_signing_opens"]
    
PUBLISHING_HELP = """
The callback and cast lists will become visible on the site after the inputted
dates and times. Additionally, actors will be emailed when these times pass.
<p class="text-white bg-danger rounded p-1 mt-1">
    DANGER: These times cannot be changed after they have passed,
    or less than ten minutes before they occur. Setting them incorrectly can
    accidentally send many emails.
<span class="text-warning">
    Please wait to set them if you are unsure, and double-check when editing
    this section.
</span>
</p>
""".strip().replace("\n", " ")
SIGNING_HELP = """
Actors will be able to sign after the first time and date. At the second
time and date, second-round-cast actors will be emailed again, and given
the option to sign regardless of first-round actors.
<p class="text-white bg-warning rounded p-1 mt-1">
    WARNING: Once casts have been published, these cannot be changed. As such,
    these times are locked along with the cast list publishing setting.
</p>
""".strip().replace("\n", " ")

@admin.register(CastingReleaseMeta)
class CastingReleaseAdmin(admin.ModelAdmin):
    form = CastingReleaseForm
    fieldsets = (
        (None, {
            "fields": ("associated_with", "stage")
        }),
        ("List Publishing", {
            "fields": ("publish_callbacks", "publish_first_round_casts",
                       "publish_casts"),
            "description": PUBLISHING_HELP
        }),
        ("Signing Options", {
            "fields": ("signing_opens", "second_signing_opens"),
            "description": SIGNING_HELP
        })
    )
    readonly_fields = ("associated_with", "stage")
    list_display = ('__str__', 'stage', 'publish_callbacks',
                    'publish_first_round_casts', 'publish_casts',
                    'signing_opens', 'second_signing_opens')

    def get_readonly_fields(self, request, obj):
        readonly = list(self.readonly_fields)
        if obj.stage > 2 or (
                not obj.tracker.has_changed("publish_casts") and
                is_locked(obj.publish_casts)):
            for i in ("signing_opens", "second_signing_opens"):
                if not obj.tracker.has_changed(i):
                    readonly.append(i)
        for i, attr in enumerate(CASTING_RELEASE_TIME_LOCKS):
            if obj.stage > i:
                readonly.append(attr)
            elif (not obj.tracker.has_changed(attr)) and is_locked(
                    getattr(obj, attr)):
                readonly.append(attr)
        return readonly

    def get_actions(self, request):
        return { "delete_unnassociated": (
            CastingReleaseAdmin.delete_unnassociated,
            "delete_unnassociated", "Delete unnassociated settings") }
    
    def delete_unnassociated(self, request, queryset):
        qs = queryset.filter(castingmeta__isnull=True)
        n = qs.count()
        qs.delete()
        self.message_user(request, "%s settings object(s) deleted." % n)

    def associated_with(self, obj):
        return str(obj)
    
    def has_delete_permission(self, request, obj=None):
        if obj:
            return not obj.association
        else:
            return super().has_delete_permission(request)

class SlotAdmin(admin.StackedInline):
    model = Slot
    fields = (('space', 'day'), ('start', 'end'))
    ordering = ('day', 'start')

    class Media:
        css = {
            'all': ('casting/django_admin.css',)
        }

    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=self.type)
    
    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            n = obj.slot_set.filter(type=self.type).count()
            return max(self.extra - n, 0)
        else:
            return self.extra
    
class AuditionSlotAdmin(SlotAdmin):
    type = Slot.TYPES[0][0]
    extra = 3
    verbose_name = "Audition Slot"

class CallbackSlotAdmin(SlotAdmin):
    type = Slot.TYPES[1][0]
    extra = 1
    verbose_name = "Callback Slot"

@admin.register(CastingMeta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ('show', 'season', 'release_meta', 'contact_email')
    list_editable = ("release_meta",)
    exclude = ('callback_description', 'cast_list_description',
               'contact_email')
    search_fields = ('show__title',)
    list_filter = ('show__season', 'show__year', 'release_meta', 'slot__day')

    inlines = [
        AuditionSlotAdmin,
        CallbackSlotAdmin,
    ]
    
    def season(self, obj):
        return obj.show.seasonstr()
