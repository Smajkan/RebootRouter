from checkconnection import *
from seleniumtest import *


# 200 = if user's not connected to internet at all / doesn't have internet enabled
# 201 = internet connection problem
current_status = None


def performAction1():
    restartRouter()
    
def performAction2():
    print("Konekcija nije ostvarena")

def performAction3():
    print("Konekcija uspostavljena i radi")

  
def countAction():
    global no_actions
    no_actions = 0
    no_actions += 1
    return no_actions

def ConnectionBack():
    current_status2 = check_connection()
    return current_status2

while True:
    current_status = int(check_connection())
    #if there's conn problem
    if current_status == 201:
        performAction1()
        counter = countAction()
        if counter >= 1:
            time.sleep(180)
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


        