from time import sleep
from urllib.request import urlretrieve
import os

# Variables to use
amt_request_six_months = 0
amt_request_total = 0

# Paula's Code: the function to calculate the requests made in 6 months
def getSixMonths(file):
    global amt_request_six_months
    # Reading from file
    Content = file.read()
    line_list = Content.split("\n")
    # startMonAndDay: "24/Oct/1994"

    for line in line_list:
        if line:
            amt_request_six_months += 1
            if "24/May/1995" in line:
                return (amt_request_six_months - 1)

# Claire's Code: Fetching the log file from the Apache server
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'http_access_log.txt'

# I used urlretrieve() and fetched a remote copy to save into the local file path
# left this line for better user experience
print("Loading Log File...")
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

print("\nDone Loading.")
sleep(3)
os.system('clear')

# Paula's Code: Calculating the requests from the first 6 months
file = open(local_file, "r")
amt_request_six_months = getSixMonths(file)

# Irish's Code: Calculating total amount of requests

# opens & reads LOCAL_FILE as filehead file
with open(LOCAL_FILE, "r") as file:
    # stores each line in list & counts list length
    amt_request_total= len(file.readlines())

# Roxanna's Code: Outputting the requested amounts
print("Total Amount of Data requested within six months:", amt_request_six_months)

print("Total Amount of Requests for the total amount of time period:", amt_request_total)

print("Done analyzing log files.")
