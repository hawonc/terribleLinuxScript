import os
from pwd import getpwnam
import random
import string

print ("Users Script starting: \n\n")
pwdList = "!@#$%^&*()?"
N = 15

usrs = open('/etc/passwd', 'r').read().splitlines()
P = []
S = []
for b in range(len(usrs)):
  usrs[b] = usrs[b].split(':')[0]
for b in range(len(usrs)):
  if (getpwnam(usrs[b])[2] == 0):
    print ("WARNING: UID OF 0: " + getpwnam(usrs[b])[0])
  if (getpwnam(usrs[b])[2] > 999):
    P.append(getpwnam(usrs[b])[0])
  else:
    S.append(getpwnam(usrs[b])[0])
print (S)
print (P)

for b in range(len(P)):
  os.system("usermod -s /bin/bash" + P[b])
  res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + pwdList, k = N))
for b in range(len(S)):
  os.system("usermod -s /bin/false" + S[b])

def creation():
  input("please create a file with the names read(readme users) and root(admins)")
def userAdd():
  x = input("\nWould you like to create a user? [y/n]\n")
  while (x.lower() == "y"):
    print (" \n Please Choose What Type Of User You Would Like To Add.\n")
    os.chdir("/home")
    res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + pwdList, k = N)) 
    print ("\t[A] - Admin\n")
    print ("\t[S] - Standard\n") 
    LevelofUser = input("\tChoice:\t")
    userName = input("Enter the Name of the New User: ")
    
    if LevelofUser.lower() == "a":
      os.system("useradd " + userName)
      os.system("usermod -aG sudo,adm" + userName)
      os.system("chpasswd " + userName + " : " + "q!" +res)
    else:
      os.system("useradd " + userName)
      os.system("chpasswd " + userName + " : " + "q!" + res)
    x = input("\nContinue? [y/n]\n")
def userDel():
  x = input("\n\nWould you like to delete a user? [y/n]\n")
  while (x.lower() == "y"):
    userNome = input("Enter the Name of the User to delete: ")
    os.system("deluser " + userNome)
    x = input("\n\nContinue? [y/n]\n")

creation()
userAdd()
userDel()

print ("Check again for hidden users with bad directories\n")
os.system("cat /etc/passwd")
input("press enter to continue")
os.system("clear")
