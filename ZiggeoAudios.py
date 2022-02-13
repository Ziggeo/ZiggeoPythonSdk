class ZiggeoAudios:

    def __init__(self, application):
        self.__application = application

    def index(self, data = None):
        return self.__application.api_connect.getJSON('/server/v1/audios/', data)

    def count(self, data = None):
        return self.__application.api_connect.getJSON('/server/v1/audios/count', data)

    def get(self, token_or_key):
        return self.__application.api_connect.getJSON('/server/v1/audios/bytoken/' + token_or_key + '')

    def get_bulk(self, data = None):
        return self.__application.api_connect.postJSON('/server/v1/audios/get-bulk', data)

    def download_audio(self, token_or_key):
        return self.__application.connect.get('/v1/server/v1/audios/bytoken/' + token_or_key + '/video')

    def update(self, token_or_key, data = None):
        return self.__application.api_connect.postJSON('/server/v1/audios/bytoken/' + token_or_key + '', data)

    def update_bulk(self, data = None):
        return self.__application.api_connect.postJSON('/server/v1/audios/update-bulk', data)

    def delete(self, token_or_key):
        return self.__application.api_connect.delete('/server/v1/audios/bytoken/' + token_or_key + '')

    def create(self, data = None, file = None):
        if (file != None):
            result = self.__application.connect.postUploadJSON('/server/v1/audios/audios-upload-url', 'audio', data, file, 'audio_type')
            result['default_stream'] = self.__application.connect.postJSON('/server/v1/audios/' + result['token'] + '/streams/' + result['default_stream']['token'] + '/confirm-audio')
            return result
        else:
            return self.__application.api_connect.postJSON('/server/v1/audios/', data, file)

