from Crypto import Random
from Crypto.Cipher import AES
import hashlib, os, binascii, random, sys, json, time

class ZiggeoAuth:

    def __init__(self, application):
        self.__application = application

    def _encrypt(self, plaintext):
        BS = 16
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
        hashed_key = hashlib.md5(self.__application.encryption_key).hexdigest()
        iv = binascii.b2a_hex(os.urandom(8))
        encrypted = binascii.hexlify(AES.new(hashed_key, AES.MODE_CBC, iv).encrypt(pad(plaintext)))
        return iv + encrypted
        
    def generate(self, options={}):
        options["application_token"] = self.__application.token
        options["nonce"] = self._generateNonce()
        return self._encrypt(json.dumps(options))
    
    def _generateNonce(self):
        return str(int(time.time())) + str(random.randint(0, sys.maxint))
