import json,requests

# Currently unused, need to figure out how to pull directly from site and use that data.
response = requests.get('https://www.outagetracker.com.au/home/GetOutageListData')

with open('GetOutageListData.json') as OutageListData:
    OutageData = json.load(OutageListData)

for suburb in OutageData:
    print(suburb['suburb'])