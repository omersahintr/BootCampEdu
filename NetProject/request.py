import requests as req


## request method
r  = req.get('https://github.com/omersahintr/BootCampEdu/blob/main/NetProject/earth-quake.json')

print(f"Status: {r.status_code} \n" #status code:200 OK
    f"Encoding:{r.encoding} \n" #encoding: utf-8
    f"Text:{r.text} \n Headers:{r.headers}") #text: html content, headers: dictionary


if r.status_code == 200:
    print("Wonderful") #Wonderful
    print(r.status_code) #200


## request method
def pull_json(url):
    res  = req.get(url)
    #content = r.text() #text content typing
    content = res.json() #json content typing
    
    if res.status_code == 200:
        print(content) #html content typing

pull_json('https://raw.githubusercontent.com/omersahintr/BootCampEdu/main/NetProject/earth-quake.json')


## lookup for json file
def pull_json_lookup(url_json):
    resp  = req.get(url_json)   
    if resp.status_code == 200:
        for found in resp.json():
            if found["location"] == "Ege Denizi":
                print(found["location"], found["magnitude"], found["depth"])


#pull_json_lookup('https://raw.githubusercontent.com/omersahintr/BootCampEdu/main/NetProject/earth-quake.json') #for json file
pull_json_lookup("https://servisnet.afad.gov.tr/apigateway/deprem/apiv2/event/filter?start=2025-01-14%2010:00:00&end=2025-02-13%2010:00:00") #for live data
