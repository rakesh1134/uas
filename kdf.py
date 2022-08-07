# import argon2

# class hasher:
#     def __init__(self):
#         self.argon2Hasher =  argon2.PasswordHasher()

#     def hashpassword(self,password):
#         hash = self.argon2Hasher.hash(password)
#         #print(hash)
#         return hash

#     def verifypassword(self,hash,password):
#         try:
#             self.argon2Hasher
#             self.argon2Hasher.verify(hash, password)
#             return True
#         except:
#             return False
    