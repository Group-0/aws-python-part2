from time import sleep
from urllib.request import urlretrieve
import os

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'http_access_log.txt'

# I used urlretrieve() and fetched a remote copy to save into the local file path
# left this line for better user experience
print("Loading Log File...")
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

print("\nDone Loading")
sleep(5)
os.system('clear')

amt_request_six_months = 0
print("Total Amount of Data requested within six months:", amt_request_six_months)


amt_request_total = 0
print("Total Amount of Requests for the total amount of time period:", amt_request_total)
