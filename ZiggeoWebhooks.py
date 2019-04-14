class ZiggeoWebhooks:

    def __init__(self, application):
        self.__application = application

    def create(self, data = None):
        return self.__application.connect.post('/v1/api/hook', data)

    def confirm(self, data = None):
        return self.__application.connect.post('/v1/api/confirmhook', data)

    def delete(self, data = None):
        return self.__application.connect.post('/v1/api/removehook', data)

