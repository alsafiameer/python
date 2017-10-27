import getpass
import sys
import telnetlib

#Username and Passwords
user = raw_input("Enter your Username: ")
login_pass = getpass.getpass("Type your login password: ")
enable_pass = getpass.getpass("Type your enable password: ")


CORE_CONFIG = ["CORE_1","CORE_2"]
ROUTER_CONFIG = ["R1","R2","R3"]
ALL_HOSTS=[]
CORE=[]
ROUTER=[]

with open("hosts") as hosts:
	for H in hosts:
 		ALL_HOSTS.append(H.strip())

for C in ALL_HOSTS[0:2]:
	CORE.append(C)
for R in ALL_HOSTS[2:6]:
	ROUTER.append(R)




print "\n\n ***** Configuring the COREs now! *****\n" 
for HOST, CONFIG in zip(CORE, CORE_CONFIG):	
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if login_pass:
		tn.read_until("Password: ")
		tn.write(login_pass + "\n")

	tn.write("enable\n")
	tn.write(enable_pass + "\n")

	# pushing the configurations
	tn.write("config t \n")
	with open(CONFIG) as configs:
		for config in configs:
			tn.write(config.strip() + "\n")
	configs.close()
	tn.write("router ospf 1 \n passive-interface G3/3 \n")
	tn.write("end\n")
	tn.write("exit\n")

	print tn.read_all()




print "\n\n ***** Configuring the ROUTERs now! *****\n" 
for HOST,CONFIG in zip(ROUTER, ROUTER_CONFIG):
	tn = telnetlib.Telnet(HOST)
	tn.read_until("Username: ")
	tn.write(user + "\n")
	if login_pass:
		tn.read_until("Password: ")
		tn.write(login_pass + "\n")

	tn.write("ena \n")
	tn.write(enable_pass + "\n")
	tn.write("config t \n")

	with open(CONFIG) as R_COFI:
		for line in R_COFI:
			tn.write(line.strip() + "\n")
	R_COFI.close()
	tn.write("router ospf 1 \n passive-interface f0/0 \n")
	tn.write("end\n")
	tn.write("exit\n")

	print tn.read_all()
