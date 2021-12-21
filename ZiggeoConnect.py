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
    def __init__(self, application, baseuri):
        self.__application = application
        self.__baseuri = baseuri

    def request(self, method, path, data = None, file = None, timeout = None):
        if timeout is None:
            timeout = self.__application.config.request_timeout
        
        for trying in range(0, self.__application.config.resilience_factor) :
            request_result = self.singleRequest(method, path, data, file, timeout)

            if (request_result.code < 500 and request_result.code >= 200):
                if request_result.code >= 300:
                    return "{\"code\": \""+str(request_result.code)+"\", \"msg\": \""+request_result.msg+"\"}"

                try:
                    accept_ranges = request_result.getheader('Accept-Ranges')
                    if (accept_ranges == 'bytes'):
                        return request_result.read()
                    else:
                        return request_result.read().decode('ascii')

                except AttributeError as e:
                    return request_result.read()
                break
                
        return "{\"code\": \""+str(request_result.code)+"\", \"msg\": \""+request_result.msg+"\"}"            

    def singleRequest(self, method, path, data, file, timeout):
        path = path.encode("ascii", "ignore")

        if (method == "GET" and data != None):
            path = path.decode('ascii', 'ignore') + "?" + urllib.urlencode(data)

        if (method != "GET" and method != "POST"):
            path = path.decode('ascii', 'ignore') + "?_method=" + method

        if not isinstance(path, basestring):
            path = path.decode("ascii", "ignore")

        if (path.split(":")[0] == 'https'): #S3 based upload
            request = urllib2.Request(path)
        else:
            request = urllib2.Request(self.__baseuri + path)
            base64string = base64.encodebytes(('%s:%s' % (self.__application.token, self.__application.private_key)).encode()).decode().replace('\n', '')
            request.add_header("Authorization", "Basic %s" % base64string)

        if (method == "GET"):
            try: 
                result = urllib2.urlopen(request, None, timeout)
                return result
            except urllib2.HTTPError as e:
                return e

        else:
            if (data == None):
                data = {}

            if (file == None):
                data = urllib.urlencode(data)
                binary_data = data.encode("ascii")

                try:
                    result = urllib2.urlopen(request, binary_data, timeout)
                    return result
                except urllib2.HTTPError as e:
                    return e
            else:
                form_file = [('file', ntpath.basename(file), open(file, "rb"))]
                content_type, body = MultiPartForm().encode(data, form_file)

                request.add_header('Content-type', content_type)
                request.add_header('Content-length', len(body))

                try:
                    result = urllib2.urlopen(request, body, timeout)
                    return result
                except urllib2.HTTPError as e:
                    return e
        

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

    def postUploadJSON(self, path, scope, data = None, file = None, type_key = None):
        if (data == None):
            data={}

        data[type_key] = file.split(".")[-1]

        result = self.requestJSON("POST", path, data, None)

        self.request("POST", result['url_data']['url'], result['url_data']['fields'], file)
        return result[scope]

    def delete(self, path, data = None, file = None):
        return self.request("DELETE", path, data, file)

    def deleteJSON(self, path, data = None, file = None):
        return self.requestJSON("DELETE", path, data, file)
