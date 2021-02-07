class ZiggeoMetaProfileProcess:

    def __init__(self, application):
        self.__application = application

    def index(self, meta_token_or_key):
        return self.__application.connect.getJSON('/v1/metaprofiles/' + meta_token_or_key + '/process')

    def get(self, meta_token_or_key, token_or_key):
        return self.__application.connect.getJSON('/v1/metaprofiles/' + meta_token_or_key + '/process/' + token_or_key + '')

    def delete(self, meta_token_or_key, token_or_key):
        return self.__application.connect.delete('/v1/metaprofiles/' + meta_token_or_key + '/process/' + token_or_key + '')

    def create_video_analysis_process(self, meta_token_or_key):
        return self.__application.connect.postJSON('/v1/metaprofiles/' + meta_token_or_key + '/process/analysis')

    def create_audio_transcription_process(self, meta_token_or_key):
        return self.__application.connect.postJSON('/v1/metaprofiles/' + meta_token_or_key + '/process/transcription')

    def create_nsfw_process(self, meta_token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/metaprofiles/' + meta_token_or_key + '/process/nsfw', data)

    def create_profanity_process(self, meta_token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/metaprofiles/' + meta_token_or_key + '/process/profanity', data)

