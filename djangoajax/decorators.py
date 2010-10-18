#-*- coding:utf-8 -*-

# decorators.py
# This file is part of django-ajax	
#
# Copyright (C) 2010 - Vincent Petithory
#
# django-ajax	 is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# django-ajax	 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
    
from django.utils.decorators import available_attrs
from django.http import Http404, HttpResponse

def ajax(function=None):
    """
    Decorator for views that checks if the request is a valid ajax request.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.is_ajax():
                return view_func(request, *args, **kwargs)
            from django.conf import settings
            if settings.DEBUG:
                return HttpResponse('Missing HTTP_X_REQUESTED_WITH header '
                'or finding \'XMLHttpRequest\' string '
                'in HTTP_X_REQUESTED_WITH header', status=412)
            else:
                raise Http404
        return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)
    
    if function:
        return decorator(function)
    return decorator

