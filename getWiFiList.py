#This one works
#I just need to go through file and take list of WiFi names, check if it's available currently
# and connect to it
import subprocess
import os
data=subprocess.check_output(['netsh','wlan','show','profile']).decode('cp1252').split('\n')
profiles=[i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

os.system('cls')
path_file=os.path.dirname(os.path.abspath(__file__))

header='''
 Wifi Name                  wifi password      pass Length     
--------------------------------------------------------------------\n'''
f=open(path_file+"\saved_wifi_pass.txt","a")
f.write(header)

for i in profiles:
    results=subprocess.check_output(['netsh','wlan','show','profile',i,
                                     'key=clear']).decode('cp1252').split('\n')
    results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        psw_len = len(results[0])
        if len(results[0])>0:
            #print("{:25}  {:22}{}".format(i, results[0],psw_len))
            get_data="{:25}  {:22}{}".format(i, results[0],psw_len)
            #f = open("saved_wifi_pass.txt", "a")
            f.write(get_data+"\n")
    except IndexError:
        continue


f.close()