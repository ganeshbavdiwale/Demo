# findall function
#check multiple occurances of same pattern in the string
msg=" This is my number:022-456-7393 and this is my alternate number :456-777-9090"
# ptrn=re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
ptrn=re.compile(r"\d{3}-\d{3}-\d{4}")
list1=ptrn.findall(msg) # no need to use group, 
print(type(list1)) #it returns a list of matched pattern not object
print(list1)
