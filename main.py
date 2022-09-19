from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'http_access_log.txt'

# I used urlretrieve() and fetched a remote copy to save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)


amt_request_six_months = 0
print("Total Amount of Data requested within six months:", amt_request_six_months)

amt_request_total = 0
print("Total Amount of Requests for the total amount of time period:", amt_request_total)

print("Succesfully analyzed log files")
