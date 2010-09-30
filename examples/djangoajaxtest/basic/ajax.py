#-*- coding:utf-8 -*-

from djangoajax.decorators import ajax
from djangoajax import HttpResponseAjax

@ajax
def store_message(request):
    if request.POST:
        message = request.POST.get('message', None)
        response = {}
        if message is not None and len(message.strip()) > 0:
            response.update({'message': message.strip()})
            response.update({'code': 0})
            response.update({'errorString': None})
            # Store the message in db here
            # ....
        else:
            response.update({'code': 1})
            response.update({'errorString': 'Message is empty'})
    else:
        response.update({'code': 2})
        response.update({'errorString': 'Not a POST request'})
    return HttpResponseAjax(response)
