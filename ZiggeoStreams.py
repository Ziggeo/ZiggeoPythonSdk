class ZiggeoStreams:

    def __init__(self, application):
        self.__application = application

    def index(self, video_token_or_key, data = None):
        return self.__application.connect.getJSON('/v1/videos/' + video_token_or_key + '/streams', data)

    def get(self, video_token_or_key, token_or_key):
        return self.__application.connect.getJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '')

    def download_video(self, video_token_or_key, token_or_key):
        return self.__application.cdn_connect.get('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/video')

    def download_image(self, video_token_or_key, token_or_key):
        return self.__application.cdn_connect.get('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/image')

    def push_to_service(self, video_token_or_key, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/push', data)

    def delete(self, video_token_or_key, token_or_key):
        return self.__application.connect.delete('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '')

    def create(self, video_token_or_key, data = None, file = None):
        if (file != None):
            result = self.__application.connect.postUploadJSON('/v1/videos/' + video_token_or_key + '/streams-upload-url', 'stream', data, file, 'video_type')
            result = self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams/' + result['token'] + '/confirm-video')
            return result
        else:
            return self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams', data, file)

    def attach_image(self, video_token_or_key, token_or_key, data = None, file = None):
        if (file != None):
            result = self.__application.connect.postUploadJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/image-upload-url', 'stream', data, file)
            result = self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/confirm-image')
            return result
        else:
            return self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/image', data, file)

    def attach_video(self, video_token_or_key, token_or_key, data = None, file = None):
        if (file != None):
            result = self.__application.connect.postUploadJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/video-upload-url', 'stream', data, file, 'video_type')
            result = self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/confirm-video')
            return result
        else:
            return self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/video', data, file)

    def attach_subtitle(self, video_token_or_key, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/subtitle', data)

    def bind(self, video_token_or_key, token_or_key):
        return self.__application.connect.postJSON('/v1/videos/' + video_token_or_key + '/streams/' + token_or_key + '/bind')

