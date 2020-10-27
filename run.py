import json,requests

# Pull Outage Data directly from Ausnet's Outage tracker site.
OutageData = requests.get('https://www.outagetracker.com.au/home/GetOutageListData')

# Fill in your town name here, could also use a varible to pull from external or another script.
Town = ""

input_dict = OutageData.json()
output_dict = [x for x in input_dict if x['suburb'] == Town]

output_json = json.dumps(output_dict)

print(output_json)