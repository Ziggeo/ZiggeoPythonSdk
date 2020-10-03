class ZiggeoEffectProfileProcess:

    def __init__(self, application):
        self.__application = application

    def index(self, effect_token_or_key, data = None):
        return self.__application.connect.getJSON('/v1/effects/' + effect_token_or_key + '/process', data)

    def get(self, effect_token_or_key, token_or_key):
        return self.__application.connect.getJSON('/v1/effects/' + effect_token_or_key + '/process/' + token_or_key + '')

    def delete(self, effect_token_or_key, token_or_key):
        return self.__application.connect.delete('/v1/effects/' + effect_token_or_key + '/process/' + token_or_key + '')

    def create_filter_process(self, effect_token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/effects/' + effect_token_or_key + '/process/filter', data)

    def create_watermark_process(self, effect_token_or_key, data = None, file = None):
        if (file != None):
            result = self.__application.connect.postUploadJSON('/v1/effects/' + effect_token_or_key + '/process/watermark-upload-url', 'effect_process', data, file)
            result = self.__application.connect.postJSON('/v1/effects/' + effect_token_or_key + '/process/' + result['token'] + '/confirm-watermark')
            return result
        else:
            return self.__application.connect.postJSON('/v1/effects/' + effect_token_or_key + '/process/watermark', data, file)

    def edit_watermark_process(self, effect_token_or_key, token_or_key, data = None, file = None):
        if (file != None):
            result = self.__application.connect.postUploadJSON('/v1/effects/' + effect_token_or_key + '/process/' + token_or_key + '/watermark-upload-url', 'effect_process', data, file)
            result = self.__application.connect.postJSON('/v1/effects/' + effect_token_or_key + '/process/' + token_or_key + '/confirm-watermark')
            return result
        else:
            return self.__application.connect.postJSON('/v1/effects/' + effect_token_or_key + '/process/watermark/' + token_or_key + '', data, file)

