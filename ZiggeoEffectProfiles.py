class ZiggeoEffectProfiles:

    def __init__(self, application):
        self.__application = application

    def create(self, data = None):
        return self.__application.connect.postJSON('/effects/', data)

    def index(self, data = None):
        return self.__application.connect.getJSON('/effects/', data)

    def get(self, token_or_key):
        return self.__application.connect.getJSON('/effects/' + token_or_key + '')

    def delete(self, token_or_key):
        return self.__application.connect.delete('/effects/' + token_or_key + '')

