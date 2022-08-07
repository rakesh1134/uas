import argon2

class hasher:
    def __init__(self):
        self.argon2Hasher =  argon2.PasswordHasher(time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)

    def hashpassword(self,password):
        argon2Hasher = argon2.PasswordHasher(
        time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)
        hash = argon2Hasher.hash(password)
        print(hash)
        return hash

    def verifypassword(self,hash,password):
        try:
            verifyValid = self.argon2Hasher.verify(hash, password)
            return True
        except:
            return False
    