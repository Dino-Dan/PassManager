import os

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
	    ''' (None) -> None
	    Check if the directory has a text file, if not, create one
	    '''
	    
	    # Check the current directory to check if there already is a
	    # text file within that you can use. If there isn't then create one
	    files = filter(os.path.isfile, os.listdir(os.curdir))
	    if("passfile.txt" not in files):
		    file = open("passfile.txt" , "w")
		    file.close() 

	    self.file_name = "passfile.txt"

    
    def save(self, website, username, password):
	    ''' This functions will save the given website's username and 
	    password into a text file
	    '''
	
	    # Create a file variable
	    file = open(self.file_name, "a")
	    # Add the website and it's information to the text file
	    file.write(website + "[" + username + "," + password + "]\n")
	    # Close the file
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
			    # Add the information including user friendly output
			    output += ("\nUsername: " + info[0] + "\nPassword: " +
				    info[1])
	    
	    # If we can not find the website's information, tell the user
	    if(not found):
		    output.append("\nDoes not exist.")
	    
	    # Give the appropriate output and close the file
	    print(output)
	    file.close()
    
    def delete(self, website):
	    ''' This function will go through and find the saved website data and
	    delete it
	    '''
	    # Create a file variable, a seek variable, and read all the lines
	    file = open(self.file_name, "r+")
	    lines = file.readlines()
	    file.seek(0)
	    
	    # Look for the website's data
	    for line in lines:
		# If the line is not the website to be removed, add it to the file
		    open_brkt = line.find("[")	    
		    if website != (line[:open_brkt]):
			file.write(line)

	    # Truncate and close the file
	    file.truncate()
	    file.close()
    
    
    def changePass(self, website, newpassword):
	    ''' This function will go through the text file and change the website's 
	    password to a new password
	    '''
	    
	    # Create a file variable
	    file = open(self.file_name, "a")
	    file.close()
	    pass

    def changeUser(self, website, newusername):
	    ''' This function will go through the text file and change the website's
	    username to a new username
	    '''
	    pass
    
    def getAll(self):
	    ''' This function will output all of the saved usernames and passwords
	    beside their respective website names
	    '''
	    pass
	
    def __delete_helper(self, website):
	    ''' Helper function that deletes and returns the website's info
	    '''
	    # Create a file variable, a seek variable, and read all the lines
	    file = open(self.file_name, "r+")
	    lines = file.readlines()
	    website_info = ""
	    file.seek(0)
	    
	    # Look for the website's data
	    for line in lines:
		# If the line is not the website to be removed, add it to the file
		    open_brkt = line.find("[")	    
		    if website != (line[:open_brkt]):
			file.write(line)
		    else:
			website_info = line
	    # Truncate and close the file
	    file.truncate()
	    file.close()
	    return line	