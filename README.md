# Python Scripts for linux

These scripts utilize Subprocess module to run commands remotely on a CentOS 7 server and run on a linux environment.
They iterate over an excel file containing the credentials for a list of server and execute the commands on the linux servers.
## Steps
- Fill the data in the excel file
- Save the scripts in a linux env from where the servers are accessible
- Install the relevant python modules
- Run the script

Modules required:

- Subprocess
- Sys
- Pandas
- Openpyxl

### NEService.py
- Connects to a linux server using Subprocess.run 
- Downloads Prometheus Node Exporter rpm 
- Installs ksh to set the node exporter to run as a service 
- Extracts the rpm 
- Starts the node exporter as a service

### OpenPort.py

- Connects to a linux server using Subprocess.run 
- Runs IPtables command to open port 9100 from the firewall
- Saves and restarts the IPtables

