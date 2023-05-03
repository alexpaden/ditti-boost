# authentication.py
from farcaster import Warpcast

class Authenticator:
    def __init__(self, access_token=None, mnemonic_phrase=None):
        self.access_token = access_token
        self.mnemonic_phrase = mnemonic_phrase

    def authenticate(self):
        if self.access_token:
            wcc = Warpcast(access_token=self.access_token)
        else:
            wcc = Warpcast(mnemonic=self.mnemonic_phrase)
        return wcc
