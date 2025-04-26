from django.http import Http404
from functools import wraps

def htmx_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.headers.get('HX-Request') != 'true':
            raise Http404("Cette page n'est accessible que via HTMX.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view