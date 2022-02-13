class ZiggeoAudio_streams:

    def __init__(self, application):
        self.__application = application

    def index(self, audio_token_or_key, data = None):
        return self.__application.api_connect.getJSON('/server/v1/audios/bytoken/' + audio_token_or_key + '/streams', data)

    def get(self, audio_token_or_key, token_or_key):
        return self.__application.api_connect.getJSON('/server/v1/audios/bytoken/' + audio_token_or_key + '/streams/bytoken/' + token_or_key + '')

    def download_audio(self, audio_token_or_key, token_or_key):
        return self.__application.connect.get('/v1/server/v1/audios/bytoken/' + audio_token_or_key + '/streams/bytoken/' + token_or_key + '/audio')

    def delete(self, audio_token_or_key, token_or_key):
        return self.__application.api_connect.delete('/server/v1/audios/bytoken/' + audio_token_or_key + '/streams/bytoken/' + token_or_key + '')

    def create(self, audio_token_or_key, data = None, file = None):
        if (file != None):
            result = self.__application.connect.postUploadJSON('/server/v1/audios/' + audio_token_or_key + '/streams-upload-url', 'stream', data, file, 'audio_type')
            result = self.__application.connect.postJSON('/server/v1/audios/' + audio_token_or_key + '/streams/' + result['token'] + '/confirm-video')
            return result
        else:
            return self.__application.api_connect.postJSON('/server/v1/audios/bytoken/' + audio_token_or_key + '/streams', data, file)

