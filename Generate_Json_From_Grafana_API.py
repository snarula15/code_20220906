# import urllib library
from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://api.github.com/repos/grafana/grafana/pulls?state=all"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
grafana_test = json.loads(response.read())
  
# print the json response
print(grafana_test)