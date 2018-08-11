from ZiggeoConfig import ZiggeoConfig
from ZiggeoConnect import ZiggeoConnect
from ZiggeoAuth import ZiggeoAuth
from ZiggeoVideos import ZiggeoVideos
from ZiggeoStreams import ZiggeoStreams
from ZiggeoAuthtokens import ZiggeoAuthtokens
from ZiggeoEffectProfiles import ZiggeoEffectProfiles
from ZiggeoEffectProfileProcess import ZiggeoEffectProfileProcess
from ZiggeoMetaProfiles import ZiggeoMetaProfiles
from ZiggeoMetaProfileProcess import ZiggeoMetaProfileProcess
from ZiggeoWebhooks import ZiggeoWebhooks
from ZiggeoAnalytics import ZiggeoAnalytics

class Ziggeo:

    def __init__(self, token, private_key, encryption_key = None):
        self.token = token
        self.private_key = private_key
        self.encryption_key = encryption_key
        self.config = ZiggeoConfig()
        self.connect = ZiggeoConnect(self)
        self.__auth = None
        self.__videos = None
        self.__streams = None
        self.__authtokens = None
        self.__effectProfiles = None
        self.__effectProfileProcess = None
        self.__metaProfiles = None
        self.__metaProfileProcess = None
        self.__webhooks = None
        self.__analytics = None

    def auth(self):
        if (self.__auth == None):
            self.__auth = ZiggeoAuth(self)
        return self.__auth
    def videos(self):
        if (self.__videos == None):
            self.__videos = ZiggeoVideos(self)
        return self.__videos
    def streams(self):
        if (self.__streams == None):
            self.__streams = ZiggeoStreams(self)
        return self.__streams
    def authtokens(self):
        if (self.__authtokens == None):
            self.__authtokens = ZiggeoAuthtokens(self)
        return self.__authtokens
    def effectProfiles(self):
        if (self.__effectProfiles == None):
            self.__effectProfiles = ZiggeoEffectProfiles(self)
        return self.__effectProfiles
    def effectProfileProcess(self):
        if (self.__effectProfileProcess == None):
            self.__effectProfileProcess = ZiggeoEffectProfileProcess(self)
        return self.__effectProfileProcess
    def metaProfiles(self):
        if (self.__metaProfiles == None):
            self.__metaProfiles = ZiggeoMetaProfiles(self)
        return self.__metaProfiles
    def metaProfileProcess(self):
        if (self.__metaProfileProcess == None):
            self.__metaProfileProcess = ZiggeoMetaProfileProcess(self)
        return self.__metaProfileProcess
    def webhooks(self):
        if (self.__webhooks == None):
            self.__webhooks = ZiggeoWebhooks(self)
        return self.__webhooks
    def analytics(self):
        if (self.__analytics == None):
            self.__analytics = ZiggeoAnalytics(self)
        return self.__analytics

