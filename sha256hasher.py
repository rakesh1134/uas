import hashlib, binascii

class sha256hasher:
  
    def hashpassword(self,password):
        hasspw = hashlib.sha3_256(bytes(password,'ascii')).digest()
        hasspw = binascii.hexlify(hasspw)
        return hasspw

    def verifypassword(self,hash,password):
        hasspw = hashlib.sha3_256(bytes(password,'ascii')).digest()
        hasspw = binascii.hexlify(hasspw)

        if hash == hasspw:
            return True
        else:
            return False