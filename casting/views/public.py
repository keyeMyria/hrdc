from django.views.generic.detail import DetailView
from django.conf.urls import url
from django.urls import reverse

from ..models import *

class CallbackView(DetailView):
    model = CastingMeta
    template_name = "casting/public/callbacks.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated():
            if self.request.user.is_pdsm:
                context["BT_header_url"] = 'casting:index'
        else:
            context["BT_header_url"] = None
        context["user_is_staff"] = self.object.show.user_is_staff(
            self.request.user)
        menu = context["sidebar_menu"] = {}
        submenu = menu[self.object.show.seasonstr() + " Callbacks"] = []
        filter_args = {
            "callbacks_submitted": True
        }
        if self.request.user.is_authenticated() and self.request.user.is_board:
            del filter_args["callbacks_submitted"]
        for i in CastingMeta.objects.filter(
                show__year=self.object.show.year,
                show__season=self.object.show.season, **filter_args):
            submenu.append({
                "name": i,
                "url": reverse("casting:view_callbacks", args=(i.pk,)),
                "active": self.object.pk == i.pk
            })
        return context

urlpatterns = [
    url(r'^callbacks/(?P<pk>\d+)/', CallbackView.as_view(),
        name="view_callbacks"),
]