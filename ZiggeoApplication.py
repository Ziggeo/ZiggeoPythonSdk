class ZiggeoApplication:

    def __init__(self, application):
        self.__application = application

    def get(self):
        return self.__application.connect.getJSON('/v1/application')

    def update(self, data = None):
        return self.__application.connect.postJSON('/v1/application', data)

    def get_stats(self, data = None):
        return self.__application.api_connect.getJSON('/server/v1/application/stats', data)

