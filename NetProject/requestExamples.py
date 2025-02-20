import requests as req

def do_request(url):
    try:
        return req.get(url)
    except req.exceptions.ConnectionError:
        pass
        

with open("domainList.txt","r") as f:
    for key in f:
        url = "https://"+key.strip()+"."+"google.com" # strip is clear space in data
        response = do_request(url)
        if response:   #response is not None         
            print(url, response)
        else:
            print(url, "Connection Error")
            #https://admin.google.com <Response [200]>
            #https://drive.google.com <Response [200]>
            #https://wp.google.com Connection Error
            #https://login.google.com Connection Error
            #https://gpt.google.com Connection Error
            #https://ai.google.com <Response [200]>
            #https://buy.google.com Connection Error
            #https://video.google.com <Response [200]>
            #https://image.google.com <Response [200]>
            #https://code.google.com <Response [200]>
                        