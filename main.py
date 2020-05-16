#import ZODB,ZODB.FileStorage
from checksumdir import dirhash

global_signature_status = 0
"""
0 = signature status not verified
1 = signature status verified
2 = signature to be modified , previous signature not verified/ or not available(database initilize)
"""


#this is to verify the database
def verify_database_integrety():
	global global_signature_status
	directory = "database"
	current_hash = dirhash(directory , "sha512")
	
	try:
		signature_file = open("signature.txt","r")
		signature = signature_file.read()
		signature_file.close()

		if signature == current_hash:
			global_signature_status = 1
			return("database safe")
		else:
			global_signature_status = 0
			return("database not safe")
	except FileNotFoundError:
		global_signature_status = 2
		update_database_signature()

#this is to update the signature
def update_database_signature():
	global global_signature_status
	if global_signature_status == 1:
		directory = "database"
		current_hash = dirhash(directory , "sha512")
	try:
		signature_file = open("signature.txt","w")
		signature_file.write(current_hash)
		signature_file.close()
	except:
		#TODO : start working here tomorrow
		pass



#authentication process



#searches for the file system if it exists
# storage = ZODB.FileStorage.FileStorage("database/user.fs")

# #points to the db
# db = ZODB.DB(storage)

# #the connection
# connection = db.open()

# root = connection.root()
