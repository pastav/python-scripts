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
    print("Downloading node exporter tar gz") 
    #subprocess.call(["wget","https://github.com/prometheus/node_exporter/releases/download/v1.4.0/node_exporter-1.4.0.linux-amd64.tar.gz"])
    COMMAND="wget --directory-prefix=/home/%s/CanvasMonitoring/ https://github.com/prometheus/node_exporter/releases/download/v1.4.0/node_exporter-1.4.0.linux-amd64.tar.gz"%username
    sshconnectrun(COMMAND,host,username,password)
    print("Downloaded the tar file")

def extractNE(host,username,password):
    print("Extracting node exporter tar gz") 
    #subprocess.call(["tar","-xzvf","node_exporter-1.4.0.linux-amd64.tar.gz"])
    COMMAND='tar -xzvf /home/%s/CanvasMonitoring/node_exporter-1.4.0.linux-amd64.tar.gz -C /home/%s/CanvasMonitoring'%(username,username)
    sshconnectrun(COMMAND,host,username,password)
    print("Extraction complete") 

def runNE(host,username,password):
    print("Running Node exporter")
    #subprocess.Popen(["nohup","./node_exporter"], cwd="/home/serveradmin/implementationauto/node_exporter-1.4.0.linux-amd64")
    COMMAND="sh -c 'cd /home/%s/CanvasMonitoring/node_exporter-1.4.0.linux-amd64; nohup ./node_exporter > /dev/null 2>&1 &'"%username
    sshconnectrun(COMMAND,host,username,password)
    print("Node exporter is running")
    
def get_nodeexporter(host,username,password):
    downloadNE(host,username,password)
    extractNE(host,username,password)
    runNE(host,username,password)

#csvdata = pandas.read_csv(r'C:\Users\10686066\Desktop\python\Data.csv')
csvdata = pandas.read_excel("Canvas Workplace Machines New.xlsx", engine='openpyxl')

for index, row in csvdata.iterrows():
    if str(row["PRIVATE IP ADDRESS"]) != "10.198.181.10":
        continue
    print("Installing on hostIP: "+ row["PRIVATE IP ADDRESS"]+ " with username "+ row["Username"])
    get_nodeexporter(row["PRIVATE IP ADDRESS"],row["Username"],row["Password"])
