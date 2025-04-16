"""script: CIS131 - Mat_Bakarich_lab_shodan.py
   action: a. query shodan for "'in-tank inventory' state:'AZ'"
           b. convert the results to JSON
           c. convert to dictionary
		   d. iterate over dictionary to write to txt file
		   e. iterate over dictionary again to print contents to user
   author: Mat Bakarich
   date:   04/15/2025 
"""

# import shodan
import shodan
# import json
import json



# configuration
API_KEY = "IRl88Dz4eDxfU09VEcWJZdwWYh6a0EeC"

# create shodan object
api = shodan.Shodan(API_KEY)

# set query for search
query = "'in-tank inventory' state:'AZ'"

# assign search results to 'result'
result = api.search(query)

# json string returned by shodan
matches = result["matches"]

# convert to json
input_data = json.dumps(matches)

# convert json to dictionary
dict_list = json.loads(input_data)

# iterate over the list of dictionaries and write the result to a file "report"
with open('report.txt', mode='w') as report:
    for item in dict_list:
	    for key,value in item.items():
		    report.write(item["data"])

# iterate over the list of dictionaries to print each result
for item in dict_list:
	    for key,value in item.items():
		    print(item["data"])

