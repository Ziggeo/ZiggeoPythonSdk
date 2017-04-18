from ZiggeoConfig import ZiggeoConfig
from ZiggeoConnect import ZiggeoConnect
from ZiggeoVideos import ZiggeoVideos
from ZiggeoStreams import ZiggeoStreams
from ZiggeoEffectProfiles import ZiggeoEffectProfiles
from ZiggeoEffectProfileProcess import ZiggeoEffectProfileProcess
from ZiggeoAuthtokens import ZiggeoAuthtokens
from ZiggeoAuth import ZiggeoAuth
        
class Ziggeo:
    def __init__(self, token, private_key, encryption_key = None):
        self.token = token
        self.private_key = private_key
        self.encryption_key = encryption_key
        self.config = ZiggeoConfig()
        self.connect = ZiggeoConnect(self)
        self.__videos = None
        self.__streams = None
        self.__effectProfiles = None
        self.__effectProfileProcess = None
        self.__authtokens = None
        self.__auth = None
        
    def videos(self):
        if (self.__videos == None):
            self.__videos = ZiggeoVideos(self)
        return self.__videos

    def streams(self):
        if (self.__streams == None):
            self.__streams = ZiggeoStreams(self)
        return self.__streams

    def effectProfiles(self):
        if (self.__effectProfiles == None):
            self.__effectProfiles = ZiggeoEffectProfiles(self)
        return self.__effectProfiles

    def effectProfileProcess(self):
        if (self.__effectProfileProcess == None):
            self.__effectProfileProcess = ZiggeoEffectProfileProcess(self)
        return self.__effectProfileProcess

    def authtokens(self):
        if (self.__authtokens == None):
            self.__authtokens = ZiggeoAuthtokens(self)
        return self.__authtokens

    def auth(self):
        if (self.__auth == None):
            self.__auth = ZiggeoAuth(self)
        return self.__auth
