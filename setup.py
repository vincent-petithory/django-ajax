#-*- coding:utf-8 -*-

# views.py
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

import sys, os
from distutils.core import setup

version = '0.1.0'

data = dict(
    name =          'django-ajax',
    version =       version,
    url =           'http://github.com/vincent-petithory/django-ajax',
    download_url =  'http://github.com/downloads/vincent-petithory/django-ajax/django-ajax.%s.tar.gz' % version,
    description =   'AJAX library for Django',
    author =        'Vincent Petithory',
    author_email =  'vincent [dot] petithory [at] gmail.com',
    maintainer =    'Vincent Petithory',
    maintainer_email = 'vincent [dot] petithory [at] gmail.com',
    license =       'LGPL License',
    packages =      ['djangoajax'],
    scripts =       [],
    cmdclass =      {},
    classifiers =   ['Development Status :: 5 - Production/Stable',
                    'Environment :: Web Environment',
                    'License :: OSI Approved :: LGPL License',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.6',
                    'Topic :: Software Development :: Libraries :: Python Modules',
                    'Framework :: Django',
                    'Intended Audience :: Developers',
                    'Topic :: Utilities'],
    ) 

setup(**data)
