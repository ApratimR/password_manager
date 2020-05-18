import ZODB,ZODB.FileStorage
from checksumdir import dirhash


global_signature_status = False
#True = signature verified
#False = signature not verified


#this is to verify the database
def verify_database_integrety():
	global global_signature_status
	directory = "database"
	current_hash = dirhash(directory , "sha512")
	
	try:

		#read file
		signature_file = open("signature.txt","r")
		signature = signature_file.read()
		signature_file.close()

		#hash verify
		if signature == current_hash:
			global_signature_status = True
			return("database safe")
		else:
			global_signature_status = False
			return("database not safe")

	# if the signature file is deleted
	except FileNotFoundError:
		global_signature_status = False
		print("signature or database not found")
		decision_sign_deleted()

def decision_sign_deleted():
	print("""would you like to :
	1.would you like to resign
	2.or check the database""")
	try:
		option_input = int(input())
		if option_input == 1:
			update_database_signature()
		else:
			#NOTE work on manual check of database
			pass
	pass


#this is to update the signature
def update_database_signature():
	global global_signature_status

	directory = "database"
	current_hash = dirhash(directory , "sha512")
	try:
		signature_file = open("signature.txt","w")
		signature_file.write(current_hash)
		signature_file.close()
	except:
		 
		pass



#authentication process



#searches for the file system if it exists
# storage = ZODB.FileStorage.FileStorage("database/user.fs")

# #points to the db
# db = ZODB.DB(storage)

# #the connection
# connection = db.open()

# root = connection.root()
