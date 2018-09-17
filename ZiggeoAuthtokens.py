class ZiggeoAuthtokens:

    def __init__(self, application):
        self.__application = application

    def get(self, token):
        return self.__application.connect.getJSON('/v1/authtokens/' + token + '')

    def update(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/authtokens/' + token_or_key + '', data)

    def delete(self, token_or_key):
        return self.__application.connect.delete('/v1/authtokens/' + token_or_key + '')

    def create(self, data = None):
        return self.__application.connect.postJSON('/v1/authtokens/', data)

