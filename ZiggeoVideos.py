class ZiggeoVideos:

    def __init__(self, application):
        self.__application = application

    def index(self, data = None):
        return self.__application.connect.getJSON('/videos/', data)

    def count(self, data = None):
        return self.__application.connect.getJSON('/videos/count', data)

    def get(self, token_or_key):
        return self.__application.connect.getJSON('/videos/' + token_or_key + '')

    def get_bulk(self, data = None):
        return self.__application.connect.postJSON('/videos/get_bulk', data)

    def stats_bulk(self, data = None):
        return self.__application.connect.postJSON('/videos/stats_bulk', data)

    def download_video(self, token_or_key):
        return self.__application.connect.get('/videos/' + token_or_key + '/video')

    def download_image(self, token_or_key):
        return self.__application.connect.get('/videos/' + token_or_key + '/image')

    def get_stats(self, token_or_key):
        return self.__application.connect.getJSON('/videos/' + token_or_key + '/stats')

    def push_to_service(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/videos/' + token_or_key + '/push', data)

    def apply_effect(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/videos/' + token_or_key + '/effect', data)

    def update(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/videos/' + token_or_key + '', data)

    def update_bulk(self, data = None):
        return self.__application.connect.postJSON('/videos/update_bulk', data)

    def delete(self, token_or_key):
        return self.__application.connect.delete('/videos/' + token_or_key + '')

    def create(self, data = None, file = None):
        return self.__application.connect.postJSON('/videos/', data, file)

    def analytics(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/videos/' + token_or_key + '/analytics', data)

