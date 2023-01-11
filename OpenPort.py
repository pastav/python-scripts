import subprocess
import sys
import pandas

def sshconnectrun(COMMAND,host,username,password):
    print("Connecting to the host") 
    ssh = subprocess.run(["sshpass","-p",password,"ssh",username+"@"+host, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
    result = ssh.stdout
    if result == []:
        error = ssh.stderr
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print (result)

def openPort(host,username,password):
    print("Running IPtables command")
    #subprocess.Popen(["nohup","./node_exporter"], cwd="/home/serveradmin/implementationauto/node_exporter-1.4.0.linux-amd64")
    COMMAND="sh -c 'sudo iptables -I INPUT -p tcp --dport 9100 --syn -j ACCEPT; sudo service iptables save; sudo service iptables restart; sudo chkconfig iptables on'"%username
    sshconnectrun(COMMAND,host,username,password)
    print("Port opened")
    
def get_nodeexporter(host,username,password):
    openPort(host,username,password)

#csvdata = pandas.read_csv(r'C:\Users\10686066\Desktop\python\Data.csv')
csvdata = pandas.read_excel("ServerList.xlsx", engine='openpyxl')

for index, row in csvdata.iterrows():
    if str(row["PRIVATE IP ADDRESS"]) != "10.198.181.14":
        continue
    print("Installing on hostIP: "+ row["PRIVATE IP ADDRESS"]+ " with username "+ row["Username"])
    get_nodeexporter(row["PRIVATE IP ADDRESS"],row["Username"],row["Password"])
