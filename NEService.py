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
        
def downloadNE(host,username,password):
    print("Downloading node exporter rpm") 
    #subprocess.call(["wget","https://github.com/prometheus/node_exporter/releases/download/v1.4.0/node_exporter-1.4.0.linux-amd64.tar.gz"])
    COMMAND="wget  --no-check-certificate --directory-prefix=/home/%s/CanvasMonitoring/  https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/g/golang-github-prometheus-node-exporter-1.2.2-1.el7.x86_64.rpm"%username
    sshconnectrun(COMMAND,host,username,password)
    print("Downloaded the rpm file")

def installKSH(host,username,password):
    print("installing ksh") 
    #subprocess.call(["wget","https://github.com/prometheus/node_exporter/releases/download/v1.4.0/node_exporter-1.4.0.linux-amd64.tar.gz"])
    COMMAND="sudo yum install ksh"
    sshconnectrun(COMMAND,host,username,password)
    print("installed ksh")

def extractNE(host,username,password):
    print("install NE") 
    #subprocess.call(["tar","-xzvf","node_exporter-1.4.0.linux-amd64.tar.gz"])
    COMMAND='sudo rpm -ivh -C /home/%s/CanvasMonitoring/golang-github-prometheus-node-exporter-1.2.2-1.el7.x86_64.rpm'%username
    sshconnectrun(COMMAND,host,username,password)
    print("Extraction complete") 

def runNE(host,username,password):
    print("Running Node exporter")
    #subprocess.Popen(["nohup","./node_exporter"], cwd="/home/serveradmin/implementationauto/node_exporter-1.4.0.linux-amd64")
    COMMAND="sudo systemctl start node_exporter.service"
    sshconnectrun(COMMAND,host,username,password)
    print("Node exporter is running")
    
def get_nodeexporter(host,username,password):
    downloadNE(host,username,password)
    installKSH(host,username,password)
    extractNE(host,username,password)
    runNE(host,username,password)

#csvdata = pandas.read_csv(r'C:\Users\10686066\Desktop\python\Data.csv')
csvdata = pandas.read_excel("Canvas Workplace Machines New.xlsx", engine='openpyxl')

for index, row in csvdata.iterrows():
    if str(row["PRIVATE IP ADDRESS"]) != "10.198.181.10":
        continue
    print("Installing on hostIP: "+ row["PRIVATE IP ADDRESS"]+ " with username "+ row["Username"])
    get_nodeexporter(row["PRIVATE IP ADDRESS"],row["Username"],row["Password"])
