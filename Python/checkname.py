  

def checkName(name):  
	checkName = input("Is your name " + name + "? ") 
    
	if checkName.lower() == "yes":    
		print("Hello,", name)  
	else:    
		print("We're sorry about that.")

checkName("Nate")

input('Please hit enter to exit:')