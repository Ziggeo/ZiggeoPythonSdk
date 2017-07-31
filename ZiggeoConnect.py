import base64, json, ntpath

try:
    #For Python 3.0 and later
    from urllib import request as urllib2
    from urllib import parse as urllib
    basestring = str
except ImportError:
    #For Python 2's urllib2
    import urllib2, urllib

from MultiPartForm import MultiPartForm

class ZiggeoConnect:
    def __init__(self, application):
        self.__application = application

    def request(self, method, path, data = None, file = None, timeout=60):
        path = path.encode("ascii", "ignore")
        if (method == "GET" and data != None):
            path = path.decode('ascii', 'ignore') + "?" + urllib.urlencode(data)
        if (method != "GET" and method != "POST"):
            path = path.decode('ascii', 'ignore') + "?_method=" + method
        server_api_url = self.__application.config.server_api_url
        for k, v in self.__application.config.regions.items():
            if (self.__application.token.startswith(k)):
                server_api_url = v

        if not isinstance(path, basestring):
            path = path.decode("ascii", "ignore")

        request = urllib2.Request(server_api_url + "/v1" + path)

        base64string = base64.encodestring(('%s:%s' % (self.__application.token, self.__application.private_key)).encode()).decode().replace('\n', '')

        request.add_header("Authorization", "Basic %s" % base64string)
        if (method == "GET"):
            result = urllib2.urlopen(request, None, timeout)
        else:
            if (data == None):
                data = {}
            if (file == None):
                data = urllib.urlencode(data)
                binary_data = data.encode("ascii")
                result = urllib2.urlopen(request, binary_data, timeout)
            else:
                form = MultiPartForm()
                for k, v in data.iteritems():
                    form.add_field(k, v)
                form.add_file('file', ntpath.basename(file), fileHandle=open(file, "rb"))
                body = str(form)
                request.add_header('Content-type', form.get_content_type())
                request.add_header('Content-length', len(body))
                result = urllib2.urlopen(request, body, timeout)

        return result.read().decode("utf-8", 'ignore')

    def requestJSON(self, method, path, data = None, file = None):
        return json.loads(self.request(method, path, data, file))

    def get(self, path, data = None, file = None):
        return self.request("GET", path, data, file)

    def getJSON(self, path, data = None, file = None):
        return self.requestJSON("GET", path, data, file)

    def post(self, path, data = None, file = None):
        return self.request("POST", path, data, file)

    def postJSON(self, path, data = None, file = None):
        return self.requestJSON("POST", path, data, file)

    def delete(self, path, data = None, file = None):
        return self.request("DELETE", path, data, file)

    def deleteJSON(self, path, data = None, file = None):
        return self.requestJSON("DELETE", path, data, file)
