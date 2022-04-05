#!/usr/bin/env python3
import os
import fileinput

def firewall():
  os.system("sudo apt-install ufw")
  os.system("sudo ufw enable" )
  IPv6Allow = input("Should IPv6 be enabled?\n")

  if(IPv6Allow.lower() == "yes" or IPv6Allow.lower() == "y"):
    os.system("sudo echo \'net.ipv6.conf.all.disable_ipv6 = 0\' >> /etc/sysctl.conf")
    os.system("sudo echo \'net.ipv6.conf.default.disable_ipv6 = 0\' >> /etc/sysctl.conf")
    os.system("sudo echo \'net.ipv6.conf.alo.disable_ipv6 = 0\' >> /etc/sysctl.conf")
  elif(IPv6Allow.lower() == "no" or IPv6Allow.lower() == "n"):
    os.system("sudo echo \'net.ipv6.conf.all.disable_ipv6 = 1\' >> /etc/sysctl.conf")
    os.system("sudo echo \'net.ipv6.conf.default.disable_ipv6 = 1\' >> /etc/sysctl.conf")
    os.system("sudo echo 'net.ipv6.conf.alo.disable_ipv6 = 1' >> /etc/sysctl.conf")
	else:
		print("Please type in a yes or a no")

	os.system("sysctl -n net.ipv4.tcp_syncookies")
	os.system("sudo echo 0 > /proc/sys/net/ipv4/ip_forward")
	os.system("sudo echo \"nospoof on\" >> /etc/host.conf")

	print("Should gufw be on the system?")

	gufwResponse = input()

	if(gufwResponse.lower() = "yes" or gufwResponse.lower() = "y"):
		os.system("sudo apt install gufw")
	elif(gufwResponse.lower() = "no" or gufwResponse.lower() = "n"):
		os.system("sudo apt purge gufw")
	else:
		print("Please type in a yes or a no")

	os.system("sudo ufw deny 23")
    os.system("sudo ufw deny 2049")
    os.system("sudo ufw deny 515")
    os.system("sudo ufw deny 111")

	sshResponse = input("Should ssh be installed?\n")

	if(sshResponse.lower() = "yes" or sshResponse.lower() = "y"):
		os.system("sudo apt install openssh-server")
		os.system("sudo apt install openssh-client")
		os.system("sudo ufw allow ssh")

		sshdConfig = open("/etc/ssh/sshd_config", "a+")
		sshdConfig.write("PermitRootLogin = no")
		sshdConfig.write("ServerKeyBits 1024")

	elif(sshResponse.lower() = "no" or sshResponse.lower() = "n"):
		os.system("sudo ufw deny ssh")
		os.system("sudo apt purge openssh-server")
		os.system("sudo apt purge openssh-client")
	else:
		print("Please enter in a yes or a no")
