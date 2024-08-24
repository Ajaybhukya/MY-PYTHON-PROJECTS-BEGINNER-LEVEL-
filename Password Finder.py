# Enter passwords as only numbers and alphabets
from random import *;
from  string import *;
from time import *;
u_pass=input("Enter a password:")
letters=ascii_letters+digits
pw=""
start=time()
while(pw!=u_pass):
    pw=''
    for i in range(len(u_pass)):
        guess_letter=randint(0,len(letters)-1)
        pw=letters[guess_letter]+pw
        print(pw,end='\r')
end=time()
print("Your password:",pw)
print(f"Time Taken {end-start} Sec")