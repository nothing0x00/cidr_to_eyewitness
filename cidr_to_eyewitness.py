import subprocess
import ushlex as shlex

print("Simple script to output IPs in CIDR Range, Parse List and Send to Eyewitness")
print("Only scans for ports 80 and 443")

print("\n")
list = raw_input("Input CIDR Range: ")
dir = raw_input("Enter current directory (with trailing /): ")

cidr = list.replace(".", "_") + ".txt"
cidr2 = cidr.replace("/", "_")
ips = open(cidr2, "w")

cmd1 = "prips " + list
args1 = shlex.split(cmd1)
subprocess.call(args1, stdout=ips)
ips.close()
targets = open(cidr2, "r")
new_name = cidr2.strip(".txt") + "_parsed.txt"
new_file = open(new_name, "a")

for ip in targets:
    http = "http://" + ip.strip("\n")
    https = "https://" + ip.strip("\n")
   # print(http)
   # print(https)
    new_file.write(http + "\n")
    new_file.write(https + "\n")

new_file.close()

cmd2 = "eyewitness --web --threads 10 -f " + dir + new_name
print(cmd2)
args2 = shlex.split(cmd2)
subprocess.call(args2)

#To Do
#automate directory and eliminate prompt, could probably use os.cwd()
#Fancy it up with some ASCII Art and Colors
#Eliminate CIDR range prompt and add it as a commandline flag
# Add output directory as flag
