from checkconnection import *
from seleniumtest import *
import os.path
from os import path
from datetime import datetime


# 200 = if user's not connected to internet at all / doesn't have internet enabled
# 201 = internet connection problem

#GLOBAL_VARIABLES
current_status = None
no_actions = 0
restartsDone = 0


#Currently in development since I realized that it'd be pretty handy if it finds available SSIDs and then checks 
#if there's connection with the same name and then connect on it
"""
#This restarts WiFi
def restart_wifi_adapterWin():
    # scan available Wifi networks
    os.system('cmd /c "netsh wlan show networks"')
 
    # input Wifi name
    SSID_name = "SmajkanNET"
 
    # connect to the given wifi network
    os.system(f'''cmd /c "netsh wlan connect name={SSID_name}"''')
"""

#Vraca trenutno vrijeme
def currentTime():
    return datetime.now().strftime('[%Y-%m-%d %H:%M]')

#This function is used to write to files
def writeToFile(WriteToFileResets,logFile):
    mrkp1 = "===================="
    logFile.write(mrkp1 + "Reboot performed at: " + str(currentTime()) + mrkp1 + "\n" )
    logFile.write(mrkp1 + "Numbers of reboots performed:" + str(WriteToFileResets) + mrkp1 + "\n")
    

#This function is used to createLogFile, in case there's LogFile that exist it will just proceed with writing to file
def createLogFile(restartsDone):
    if path.exists("LogFile.txt") == True:  #U slucaju da vec postoji "LogFile.txt" nastavljamo praviti log na taj fajl
        myLogFile = open("LogFile.txt","a")
        writeToFile(restartsDone,myLogFile)
    else: #U slucaju da log file ne postoji, kreiramo fajl i onda pisemo u njega
        myLogFile = open("LogFile.txt","w+")
        writeToFile(restartsDone,myLogFile)

#performAction: 1. Reboots router ; 2. Counts how many times restarts're done;
def performAction1():
    restartRouter()
    global restartsDone
    restartsDone = countAction()
    createLogFile(restartsDone)

#Currently in development: Will try to add option to automatically re-enable connection and connect to available network    
def performAction2():
    #restart_wifi_adapterWin()
    print("Konekcija nije ostvarena")


#There'll be GUI, so we'll do something with this, probably make some stuff green
def performAction3():
    print("Konekcija uspostavljena i radi")
    
#This one checks how many times something is executed    
def countAction():
    global no_actions
    no_actions += 1
    return no_actions

#It checks if connection is back (had to use this because if we get our wifi off)
def ConnectionBack():
    current_status2 = check_connection()
    return current_status2


#This is kinda main function for now

while True:
    current_status = int(check_connection())
    #if there's conn problem
    if current_status == 201: #jeste 201 == ima problem sa internetom
        performAction1() #performAction(1)
        #uradio je action
        timesexecuted = 0 # setuj ovo na nula
        timesexecuted = countAction() 
        #provjerio je koliko se puta executovo kod
        if timesexecuted >= 1:
            #ukoliko je broj executovanja veci od jedan
            time.sleep(180)
            #stavi aplikaciju da spava
        else:
            continue         
    elif current_status == 200:
        performAction2()
        counter = countAction()
        if counter >= 1: #counter = 1
            stats = ConnectionBack() #200
            while stats == 200:
                time.sleep(1)
                stats = ConnectionBack()  
        else:
            continue        
                
    else:
        performAction3()