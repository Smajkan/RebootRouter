from checkconnection import *
from seleniumtest import *


# 200 = if user's not connected to internet at all / doesn't have internet enabled
# 201 = internet connection problem
current_status = None

def performAction1():
    
    
def performAction2():
    print("Some2Code")

def performAction3():
    print("Konektovan si glupane")

while True:
    current_status = check_connection()
    #if there's conn problem
    if current_status == 201:
        performAction1()
    elif current_status == 200:
        performAction2()
    else:
        performAction3()


        