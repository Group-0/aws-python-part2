from time import sleep
from urllib.request import urlretrieve
import os

# Variables to use
amt_request_six_months = 0
amt_request_total = 0

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

# Paula's Code: Calculating the requests from the past 6 months

# Irish's Code: Calculating total amount of requests

# Roxanna's Code: Outputting the requested amounts
print("Total Amount of Data requested within six months:", amt_request_six_months)

print("Total Amount of Requests for the total amount of time period:", amt_request_total)
