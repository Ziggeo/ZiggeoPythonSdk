class ZiggeoStreams:

    def __init__(self, application):
        self.__application = application

    def index(self, video_token_or_key, data = None):
        return self.__application.connect.getJSON('/videos/' + video_token_or_key + '/streams', data)

    def get(self, video_token_or_key, token_or_key):
        return self.__application.connect.getJSON('/videos/' + video_token_or_key + '/streams/' + token_or_key + '')

    def download_video(self, video_token_or_key, token_or_key):
        return self.__application.connect.get('/videos/' + video_token_or_key + '/streams/' + token_or_key + '/video')

    def download_image(self, video_token_or_key, token_or_key):
        return self.__application.connect.get('/videos/' + video_token_or_key + '/streams/' + token_or_key + '/image')

    def delete(self, video_token_or_key, token_or_key):
        return self.__application.connect.delete('/videos/' + video_token_or_key + '/streams/' + token_or_key + '')

    def create(self, video_token_or_key, data = None, file = None):
        return self.__application.connect.postJSON('/videos/' + video_token_or_key + '/streams', data, file)

