class ZiggeoEffectProfiles:

    def __init__(self, application):
        self.__application = application

    def create(self, data = None):
        return self.__application.connect.postJSON('/v1/effects/', data)

    def index(self, data = None):
        return self.__application.connect.getJSON('/v1/effects/', data)

    def get(self, token_or_key):
        return self.__application.connect.getJSON('/v1/effects/' + token_or_key + '')

    def delete(self, token_or_key):
        return self.__application.connect.delete('/v1/effects/' + token_or_key + '')

    def update(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/effects/' + token_or_key + '', data)

