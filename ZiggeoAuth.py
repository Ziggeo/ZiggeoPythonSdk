from Crypto import Random
from Crypto.Cipher import AES
import hashlib, os, binascii, random, sys, json, time

class ZiggeoAuth:

    def __init__(self, application):
        self.__application = application

    def _encrypt(self, plaintext):
        BS = 16
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

        try:
            hashed_key = hashlib.md5(self.__application.encryption_key.encode('utf-8')).hexdigest()
            iv = binascii.b2a_hex(os.urandom(8))
            encrypted = binascii.hexlify(AES.new(hashed_key.encode('utf-8'), AES.MODE_CBC, iv).encrypt(pad(plaintext).encode('utf-8')))
            return str(iv + encrypted, 'utf-8')
        except TypeError:
            md=hashlib.md5()
            md.update(self.__application.encryption_key.encode('utf-8'))
            hashed_key=md.hexdigest()
            iv = binascii.b2a_hex(os.urandom(8))
            encrypted = binascii.hexlify(AES.new(hashed_key, AES.MODE_CBC, iv).encrypt(pad(plaintext)))
            return str(iv + encrypted, 'utf-8')


    def generate(self, options={}):
        options["application_token"] = self.__application.token
        options["nonce"] = self._generateNonce()
        return self._encrypt(json.dumps(options))

    def _generateNonce(self):
        try:
            max_int = sys.maxint
        except AttributeError:
            max_int = sys.maxsize
        return str(int(time.time())) + str(random.randint(0, max_int))
