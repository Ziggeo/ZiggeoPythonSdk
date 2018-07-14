class ZiggeoMetaProfiles:

    def __init__(self, application):
        self.__application = application

    def create(self, data = None):
        return self.__application.connect.postJSON('/metaprofiles/', data)

    def index(self, data = None):
        return self.__application.connect.getJSON('/metaprofiles/', data)

    def get(self, token_or_key):
        return self.__application.connect.getJSON('/metaprofiles/' + token_or_key + '')

    def delete(self, token_or_key):
        return self.__application.connect.delete('/metaprofiles/' + token_or_key + '')

