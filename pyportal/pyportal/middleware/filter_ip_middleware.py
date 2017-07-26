from django.http import HttpResponseForbidden
from django.http import HttpResponse


class FilterHostMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response


    def process_request(self, request):

        allowed_hosts = ['127.0.0.1', 'localhost']  # specify complete host names here
        host = request.META.get('HTTP_HOST')

        if host[:7] == '192.168':  # if the host starts with 192.168 then add to the allowed hosts
            allowed_hosts.append(host)

        if host not in allowed_hosts:
            raise HttpResponseForbidden

        response = self.get_response(request)

        return response
