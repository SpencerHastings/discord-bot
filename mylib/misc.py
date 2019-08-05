from datetime import datetime

def get_time():
    now = datetime.now()
    currenttime = now.strftime("%m/%d/%Y, %H:%M:%S")
    return currenttime