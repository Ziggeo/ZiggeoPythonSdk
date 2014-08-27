import urllib, urllib2, base64, json, ntpath

from MultiPartForm import MultiPartForm 

class ZiggeoConnect:
    def __init__(self, application):
        self.__application = application
        
    def request(self, method, path, data = None, file = None):
        if (method == "GET" and data != None):
            path = path + "?" + urllib.urlencode(data)
        request = urllib2.Request(self.__application.config.server_api_url + "/v1" + path)
        base64string = base64.encodestring('%s:%s' % (self.__application.token, self.__application.private_key)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        if (method == "GET"):   
            result = urllib2.urlopen(request)
        else:
            if (data == None):
                data = {}
            if (method != "POST"):
                path = path + "?_method=" + method
            if (file == None):
                result = urllib2.urlopen(request, urllib.urlencode(data))
            else:
                form = MultiPartForm()
                for k, v in data.iteritems():
                    form.add_field(k, v)
                form.add_file('file', ntpath.basename(file), fileHandle=open(file)) 
                body = str(form)
                request.add_header('Content-type', form.get_content_type())
                request.add_header('Content-length', len(body))
                result = urllib2.urlopen(request, body)
        return result.read()
        
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
    