class ZiggeoVideos:

    def __init__(self, application):
        self.__application = application

    def index(self, data = None):
        return self.__application.connect.getJSON('/videos/', data)

    def get(self, token_or_key):
        return self.__application.connect.getJSON('/videos/' + token_or_key + '')

    def download_video(self, token_or_key):
        return self.__application.connect.get('/videos/' + token_or_key + '/video')

    def download_image(self, token_or_key):
        return self.__application.connect.get('/videos/' + token_or_key + '/image')

    def push_to_service(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/videos/' + token_or_key + '/push', data)

    def update(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/videos/' + token_or_key + '', data)

    def delete(self, token_or_key):
        return self.__application.connect.delete('/videos/' + token_or_key + '')

    def create(self, data = None, file = None):
        return self.__application.connect.postJSON('/videos/', data, file)

