import re 
# this program is check mail id is valid or not
n=input("Enter Your Mail:")
check=re.findall("[a-z0-9]@gmail.com$",n)
if(check):
	print("valid mail address")
else:
	print("invalid mail address")

