import time, os, requests


url = 'https://www.google.com/'
timeout = 2
sleep_time = 10
op = None
status_cody = None

# 450 = connected
# 200 = if user's not connected to internet at all / doesn't have internet enabled
# 201 = internet connection problem

def check_connection():
    try:
        op = requests.get(url, timeout=timeout).status_code
        if op == 200:
            status_cody = int(450)
            return status_cody
            sleep_time = 10
        else:
            status_cody = int(201)
            return status_cody
    except:
            status_cody = 200
            return status_cody
            time_sleep(sleep_time)


