from urllib.request import urlretrieve
import os
from os.path import exists
import re

""" 
  Dictionaries to use
""" 
file_count = {}
month_count = {}
day_count = {}

week_count = {}
week_count_avg = {}

""" 
  Variables to use
""" 
amt_request_six_months = 0
amt_request_total = 0
amt_of_least_requested = 0 

""" 
  Functions to use
""" 
#   Paula's Code: the function to calculate the requests made in 6 months
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

#   Irish's Code: function to get the percent of requests for a particular request code starting with string num (i.e., 4xx, 3xx)
def getRequestsPercent(file, num): 
  global amt_request_total
  # Append first digit of request code we're looking for (num) to the regex pattern
  pattern = ".*\[([0-9]+/[a-zA-Z]+/[0-9]{4}):(.*) \-[0-9]{4}\] \"(.*)\" " + num + ".*"
  amt_requests = 0

  # Loop through each line of file
  for line in file:
    # Read line of file one by one and temporarily store as one_line
    one_line = file.readline()

    # Use regex function re.search() to check if current line matches with regex pattern
    if re.search(pattern, one_line):
      # If it matches, increment amt_requests by 1
      amt_requests += 1
  
  # Get percentage; divide amt_requests by amt_request_total
  requests_percent = (amt_requests / amt_request_total) * 100
  return round(requests_percent, 2)

# Finds the count per month
def findCountMonth():
  global month_count
  for line in open('http_access_log.txt'):
    pieces = re.split(
      ".*\[[0-9]+/([a-zA-Z]+)/[0-9]{4}:.* \-[0-9]{4}\] \".*\" .*", line)
    if len(pieces) > 1:
      month = pieces[1]
      if month in month_count:
        month_count[month] += 1
      else:
        month_count[month] = 1

# Finds the count per day
def findCountDay():
  global day_count
  for line in open('http_access_log.txt'):
    pieces = re.split(
      ".*\[([0-9]+/[a-zA-Z]+)/[0-9]{4}:.* \-[0-9]{4}\] \".*\" .*", line)
    if len(pieces) > 1:
      day = pieces[1]
      if day in day_count:
        day_count[day] += 1
      else:
        day_count[day] = 1
        
def findCountWeek():
  global day_count
  global week_count
  
  week_amt = 1
  day_amt = 1
  sum = 0
  
  for key, value in day_count.items():
    if day_amt <= 7:
      sum += int(value)
      day_amt += 1
    else:
      # assigns week as key and sum/sum avg as its value
      weekname = "Week " + str(week_amt)
      week_count[weekname] = sum
      week_count_avg[weekname] = sum/7
      # resets values
      week_amt += 1
      day_amt = 1
      sum = int(value)

#Code for counting both most & least requested Files: 
def getFileCount():
  global file_count
  for line in open('http_access_log.txt'):
    pieces = re.split(
      ".*\[([0-9]+/[a-zA-Z]+/[0-9]{4}):(.*) \-[0-9]{4}\] \"(?:GET )(.*)(?: HTTP/1.0)\" .*",
      line)
      
    if len(pieces) > 3:
      filename = pieces[3]
      if filename in file_count:
        file_count[filename] += 1
      else:
        file_count[filename] = 1
""" 
  Essentially, main() function
""" 
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

# Paula's code: Calculates requests per month
findCountMonth()
print("Requests made per month:")
for k, v in month_count.items():
    print(k, v)
    
print("-"*20)

# Paula's code: Calculates requests per day
findCountDay()
print("Requests made per day:")
for k, v in day_count.items():
  print(k, v)
print("Average requests per day is: ", sum(day_count.values()) / len(day_count))
print("-"*20)

# Paula's code: Calculates requests per week and average
findCountWeek()

print("Requests made per week:")
for k, v in week_count.items():
  print(k, v)
  
print("\nAverage requests made per week:")
for k, v in week_count_avg.items():
  print(k, v)
  
print("-"*20)
# Roxanna & Claire: Most and least requested files
amt_request_six_months = getFileCount()

print("This is the most requested file: ", max(file_count, key=file_count.get))
print("This is the least requested file: ", min(file_count, key=file_count.get))

print("-"*20)

# Irish's Code: Percentage of requests that were unsuccessful (4xx request codes)
# Open and read file
with open(log_file, "r") as file:
  # Call function with correct parameters and print results
  print("Percent of Unsuccessful Requests: ", getRequestsPercent(file, "4"), "%")

# Juan's Code: Percentage of requests that were redirected elsewhere (any 3xx request codes)
# Open and read file
with open(log_file, "r") as file:
  # Call function with correct parameters and print results
  print("Percent of Redirected Requests: ", getRequestsPercent(file, "3"), "%")
    
print("-"*20)
