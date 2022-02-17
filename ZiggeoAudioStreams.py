class ZiggeoAudioStreams:

    def __init__(self, application):
        self.__application = application

    def index(self, audio_token_or_key, data = None):
        return self.__application.api_connect.getJSON('/v1/audios/' + audio_token_or_key + '/streams', data)

    def get(self, audio_token_or_key, token_or_key):
        return self.__application.api_connect.getJSON('/v1/audios/' + audio_token_or_key + '/streams/' + token_or_key + '')

    def download_audio(self, audio_token_or_key, token_or_key):
        return self.__application.js_cdn_connect.get('/v1/audios/' + audio_token_or_key + '/streams/' + token_or_key + '/audio')

    def delete(self, audio_token_or_key, token_or_key):
        return self.__application.api_connect.delete('/v1/audios/' + audio_token_or_key + '/streams/' + token_or_key + '')

    def create(self, audio_token_or_key, data = None, file = None):
        if (file != None):
            result = self.__application.connect.postUploadJSON('/v1/audios/' + audio_token_or_key + '/streams-upload-url', 'stream', data, file, 'audio_type')
            result = self.__application.connect.postJSON('/v1/audios/' + audio_token_or_key + '/streams/' + result['token'] + '/confirm-audio')
            return result
        else:
            return self.__application.api_connect.postJSON('/v1/audios/' + audio_token_or_key + '/streams', data, file)

