import os
x = 0
os.system("echo \"unalias -a\" >> ~/.bashrc")
os.system("echo \"unalias -a\" >> /root/.bashrc")
def packages():
  listOfPackages = ["openssh-server","openssh-client","samba","vsftpd","apache2","mysql-server","ftp","pure-ftpd","nmap","zenmap","wireshark","telnet","netcat","netcat-openbsd","netcat-traditional", "php", 'postgresql']
  delList = ["aircrack" ,"bind9","hydra","john","medusa","nikto","iodine", "kismet", 'rsh-server', 'fcrackzip', 'ayttm', 'empathy', 'logkeys', "netris", 'nfs-kernel-server', 'vino', 'tightvncserver', 'rdesktop', 'remmina', 'vinagre' ,'ettercap', 'knocker', 'openarena-server', 'minetest', 'minetest-serve','wesnoth','minetest','minetest-server', 'nginx', 'freeciv', 'bittorrent']
  b = "y"
  os.system("echo Package Script Starting \n")

  os.system("apt-get -y install clamav chkrootkit tree bum auditd thunderbird firefox")

    # Readme exceptions
  print(listOfPackages)
  print("\n")
  while b.lower() == "y":
      critical = input("What packages are critical and therefore must not be deleted?\n\n")
      x = 0
      for temp in listOfPackages:
        if critical in temp:
          listOfPackages.remove(temp)
          x+=1
      if x == 0:
        print("Package not in List. ")

      print("\n")
      print(listOfPackages)
    
      b = input("\nPreparing to delete media. Any more critical packages? (Y/N) \n")
      x = 0

    # Actually deleting
  for pack in listOfPackages:
    os.system('apt-get -y purge '+ pack)
  for pack2 in delList:
    os.system('apt-get -y purge '+ pack2)

  print("Packages deleted ")
def usrGames():
  print ("More prohibited content")
  print ("This is the contents of /usr/games")
  os.chdir("/usr/games")
  os.system("ls -la")
  choice = input("Delete entire directory? (y/n)\n")
  if (choice.lower() == "y"):
    os.system("rm -r /usr/games")
  else: 
    print ("Lmao why not bruh \n")
  
  print("deleting cups...")
  os.system("systemctl disable cups.socket cups.path cups.service")
  os.system("systemctl kill --signal=SIGKILL cups.service")
  os.system("systemctl stop cups.socket cups.path")

  # CUPS-BROWSED
  os.system("systemctl disable cups-browsed")
  os.system("systemctl stop cups-browsed")


def pwdFile():
  print("Checking for a password file... \n")
try:
    usrGames()
except:
    pass
