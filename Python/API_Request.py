import requests
# store in a variable 
r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

# Access data as JSON string 
#.text: turns the data into a string 
r_text=r.text
print(r_text)

#.json()decode JSON data into python object 
r_json=r.json()
print(r_json)