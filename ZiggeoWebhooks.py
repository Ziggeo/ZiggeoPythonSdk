class ZiggeoWebhooks:

    def __init__(self, application):
        self.__application = application

    def create(self, data = None):
        return self.__application.connect.post('/api/hook', data)

    def delete(self, data = None):
        return self.__application.connect.post('/api/removehook', data)

