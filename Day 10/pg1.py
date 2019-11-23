#This function checks if all the characters are alpha-numeric or not
#It returns true if all the characters are alphanumeric or false otherwise
x,y = "121dklk","12345hjehe#"
print(x.isalnum(),y.isalnum()) #true #false
#passion -> pAsSiOn
x,y = "Hello","Hello1"
print(x.isalpha(),y.isalpha())

x,y = "1234","1234h"
print(x.isdigit(),y.isdigit())

x,y = "  ","  8"
print(x.isspace(),y.isspace())

x,y,z,a = "hello","Hello1","ello1","123"
print(x.islower(),y.islower(),z.islower(),a.islower())

x,y,z,a = "HELLO","Hello1","HELLO1","123"
print(x.isupper(),y.isupper(),z.isupper(),a.isupper())