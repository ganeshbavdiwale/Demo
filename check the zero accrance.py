#Check zero or one occurances in the string
# Use ? to check this   
import re

msg1= "My dad is Superman"
msg2= "My mom is Superwoman"
msg3= "My grandma is Superwowoman"
msg4= "My grandpa is Supermaman"

ptrn=re.compile(r"Super(wo)?man")    
obj=ptrn.search(msg1)      # check for msg2, msg2, msg3
#print(obj)
print(f"Your message found as :{obj.group()}")



#Check one or more occurances in the string
# Use + to check this   
import re

msg1= "My dad is Superman"
msg2= "My mom is Superwoman"
msg3= "My grandma is Superwowoman"
msg4= "My grandpa is Supermaman"

ptrn=re.compile(r"Super(wo)+man")    
obj=ptrn.search(msg3)      # check for msg2, msg2, msg3
#print(obj)
print(f"Your message found as :{obj.group()}")
