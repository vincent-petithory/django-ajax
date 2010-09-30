#-*- coding:utf-8 -*-

# __init__.py
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

from django.http import HttpResponse
from django.utils import simplejson

class HttpResponseAjax(HttpResponse):
    status_code = 200
    
    def __init__(self, content, *args, **kwargs):
        HttpResponse.__init__(self, content=simplejson.dumps(content), mimetype='application/x-json', *args, **kwargs)
    


