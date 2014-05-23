from __future__ import unicode_literals

from .conf import BREAKPOINTS


def _get_device_type(width):
    "Returns the type based on set breakpoints."
    sorted_types = sorted(BREAKPOINTS.items(), key=lambda x: x[1] or 0)
    default_type = None
    for name, cutoff in sorted_types:
        if cutoff is None:
            default_type = name
        elif not width is None and width <= cutoff:
            return name
    return default_type


def device_info(request):
    "Add processed device info into the template context."
    default = {'width': None, 'height': None, 'pixelratio': None}
    info =  getattr(request, 'device_info', default)
    width = info.get('width', None)
    info['type'] =  _get_device_type(width)
    return {'device_info': info}
