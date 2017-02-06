from autobreadcrumbs.resolver import PathBreadcrumbResolver
from django.conf import settings


class RequestPathBreadcrumbResolver(PathBreadcrumbResolver):
    def __init__(self, root_urlconf, request):
        super().__init__(root_urlconf)
        self.request = request

    def format_title(self, value):
        if callable(value):
            return value
        return super().format_title(value)

    def resolve(self, path, request=None):
        ret = super().resolve(path, request)
        for el in ret['autobreadcrumbs_elements']:
            if callable(el.title):
                el.title = el.title(self.request, el)
        return ret


def AutoBreadcrumbsContext(request):
    """
    Context processor to resolve breadcrumbs from current ressource.

    Use ``request.path`` to know the current ressource url path and
    ``settings.ROOT_URLCONF`` to resolve it.
    """
    r = RequestPathBreadcrumbResolver(settings.ROOT_URLCONF, request)
    return r.resolve(request.path, request=request)