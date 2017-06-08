import base64
from Crypto.Cipher import AES


class GibberishAES:

    def __init__(self, password):
        self._password = password.encode('utf-8')

    def decrypt(self, cipher):
        crypt_arr = base64.b64decode(cipher)
        salt = crypt_arr[8:16]
        key, iv = self._get_key_and_iv(self._password, salt)
        crypt_arr = crypt_arr[16:]
        aes = AES.new(key, AES.MODE_CBC, iv)
        return aes.decrypt(crypt_arr)[:-11].decode('utf-8')

    @classmethod
    def _get_key_and_iv(cls, password, salt, klen=32, ilen=16, msgdgst='md5'):
        '''
        Derive the key and the IV from the given password and salt.
    
        This is a niftier implementation than my direct transliteration of
        the C++ code although I modified to support different digests.
    
        CITATION: http://stackoverflow.com/questions/13907841/implement-openssl-aes-encryption-in-python
    
        @param password  The password to use as the seed.
        @param salt      The salt.
        @param klen      The key length.
        @param ilen      The initialization vector length.
        @param msgdgst   The message digest algorithm to use.
        '''
        # equivalent to:
        #   from hashlib import <mdi> as mdf
        #   from hashlib import md5 as mdf
        #   from hashlib import sha512 as mdf
        mdf = getattr(__import__('hashlib', fromlist=[msgdgst]), msgdgst)

        try:
            maxlen = klen + ilen
            keyiv = mdf(password + salt).digest()
            tmp = [keyiv]
            while len(tmp) < maxlen:
                tmp.append(mdf(tmp[-1] + password + salt).digest())
                keyiv += tmp[-1]  # append the last byte
            key = keyiv[:klen]
            iv = keyiv[klen:klen + ilen]
            return key, iv
        except UnicodeDecodeError:
            return None, None