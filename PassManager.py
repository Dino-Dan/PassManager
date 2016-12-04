class PassManager():
	'''(None) -> None
	This is a class that will manage passwords by storing them in a text 
	file. They will be in a format that follows this:
	WEBSITE:[USERNAME, PASSWORD]
	This will also be able to read the passwords within the text file and
	output them if the user so wishes. This can also delete passwords and 
	change stored passwords
	'''

	def __init__(self):
		''' Check if the directory has a text file, if not, create one
		'''
		file = open("passfile.txt" , "w")
		self.file_name = "passfile.txt"
		file.close() 

	def save(self, website, username, password):
		''' This functions will save the given website's username and 
		password into a text file
		'''
		file = open(self.file_name, "a")
		file.write(website + "[" + username + "," + password + "]\n")
		file.close()

	def read(self, website):
		''' This function will read the website's username and password
		from a text file
		'''

		# Create a output and create a local variable for file and a
		# variable to check if the website has any information saved
		file = open(self.file_name, "r")		
		output = website + "'s login information:"
		found = False

		# Loop through the text file to find the website's information
		for line in file:
			
			# Find the index of the brackets 
			open_brkt = line.find("[")
			close_brkt = line.find("]")
			
			if(line[:open_brkt] == website):

				# We found the website's login information
				found = True

				# Get the information from the line and split 
				# it into an array for referencing
				info = line[open_brkt + 1:close_brkt]
				info = info.split(",")
				# Add all the information including a user friendly output
				output += ("\nUsername: " + info[0] + "\nPassword: " +
					info[1])
		
		# If we can not find the website's information, tell the user
		if(not found):
			output.append("\nDoes not exist.")

		print(output)
		file.close()




	def changePass(self, website, newpassword):
		''' This function will go through the text file and change the website's 
		password to a new password
		'''
		pass

	def changeUser(self, website, newusername):
		''' This function will go through the text file and change the website's
		username to a new username
		'''
		pass

	def getAll(self):
		''' This function will output all of the saved usernames and passwords beside
		their respective website names
		'''
		pass