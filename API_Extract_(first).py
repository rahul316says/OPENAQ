#Retriveing data using OPEN AQ API. JSON file and CSV file are created and stored locally.

import json
from urllib.error import URLError
import urllib.request, urllib.parse
import pandas as pd



url = "https://api.openaq.org/v1/measurements/"

#List of API parameters which can be accquired
values = {'location'  : 'IGI Airport (T3), Delhi - IMD',
          'parameter' : ['pm25','pm10','no2','co','o3'],
          'limit' :  '600' ,}

        
url_values = urllib.parse.urlencode(values,True)  #creating the extended url using API parameters
url = url + '?' + url_values                      #concatenating url
print(url)

try:
    response = urllib.request.urlopen(url)
    data_read = response.read().decode()                       #decoding the unicode data to string
    json_text = json.loads(data_read)                          #parsing the string as JSON for reading
    with open('OpenAQ_data.json', 'w') as files:
        json.dump(json_text["results"], files , indent=2)      #we are intersted in the Results section.

    pm25,pm10,co,o3 = ([] for i in range(4))                   #empty list creation for gas parameters
    
    for i in json_text["results"]:
        eval(i['parameter']).append(i['value'])                #the values were appended to the list
        
    df= pd.DataFrame({'PM25': pm25,'PM10': pm10,'CO':co,'O3':o3})             #Dataframe cretion using the list as the headers
    export_csv = df.to_csv(r'OpenAQ_data.csv', index = None, header=True)     #Exported the dataframe to csv stored locally


#Error handling        
except URLError as e:                              
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)




