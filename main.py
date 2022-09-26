from urllib.request import urlretrieve
import os
from os.path import exists
import re

# Variables to use
amt_request_six_months = 0
amt_request_total = 0
amt_of_least_requested = 0 

# Paula's Code: the function to calculate the requests made in 6 months
def getSixMonths(file):
    global amt_request_six_months
    
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

if os.path.exists('http_access_log.txt'):  
    log_file = 'http_access_log.txt'
else:
    print("Loading Log File...")
    log_file, headers = urlretrieve(URL_PATH, 'http_access_log.txt', lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

print("\nDone Loading.")
os.system('clear')

# Paula's Code: Calculating the requests from the first 6 months
file = open(log_file, "r")
amt_request_six_months = getSixMonths(file)

# Irish's Code: Calculating total amount of requests
# opens & reads log file as filehead file
with open(log_file, "r") as file:
    # stores each line in list & counts list length
    amt_request_total= len(file.readlines())

# Roxanna's Code: Outputting the requested amounts
print("Done analyzing log files.")
print("-"*20)
print("Total amount of data requested within the first six months: \t", amt_request_six_months)
print("Total amount of requests for the total amount of time period: \t",  amt_request_total)
print("-"*20)

#Code for counting both most & least requested Files: 
import re

file_count = {}

def getFileCount():
  global file_count
  for line in open('http_access_log.txt'):
    pieces = re.split(
      ".*\[([0-9]+/[a-zA-Z]+/[0-9]{4}):(.*) \-[0-9]{4}\] \"(?:GET )(.*)(?: HTTP/1.0)\" .*",
      line)
      # Let's further say that we can get the filename part at the 4th list element

    if len(pieces) > 3:
      filename = pieces[3]
      
      if filename in file_count:
        file_count[filename] += 1
      else:
        
        file_count[filename] = 1

amt_request_six_months = getFileCount()

print("File max seen in log file: ", max(file_count, key=file_count.get))
print("File min seen in log file: ", min(file_count, key=file_count.get))


