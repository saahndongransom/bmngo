from .models import SiteSettings


def site_meta(request):
    return {"site_settings": SiteSettings.load()}
