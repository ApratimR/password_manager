#import ZODB,ZODB.FileStorage
from checksumdir import dirhash

#this is to verify the database
def verify_integrety():
    directory = "database"
    current_hash = dirhash(directory , "sha512")
    
    try:
        signature_file = open("signature.txt","r")
        signature = signature_file.read()
        if signature == current_hash:
            return("database safe")
        else:
            return("database not safe")
    except FileNotFoundError:
        return("signature file does not exist")

#this is to update the signature
def update_database_signature():
    if verify_integrety()=="database safe":
        directory = "database"
        current_hash = dirhash(directory , "sha512")
    
        pass


#authentication process
print(verify_integrety())



#searches for the file system if it exists
# storage = ZODB.FileStorage.FileStorage("database/user.fs")

# #points to the db
# db = ZODB.DB(storage)

# #the connection
# connection = db.open()

# root = connection.root()
