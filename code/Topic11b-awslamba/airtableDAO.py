from datetime import datetime
import requests
from config import airtable_config
from datetime import datetime
baseURL = airtable_config["baseURL"]

def getHeaders():
    headers = {}
    headers["Authorization"] = "Bearer " + airtable_config["apikey"]
    headers["Content-Type"] = "application/json"
    return headers

def writeToLog(message, level="INFO"):
    url = baseURL+ airtable_config["logtable"]["urlendpoint"]
    now = str(datetime.now())
    data = {
        "records" : [
            {
                "fields": {
                    "message": message,
                    "level" : level,
                    "timestamp": now
                }
            }
        ]
    }
    print (data)
    response = requests.post(url, headers= getHeaders(), json= data)
    print(response.json())
    return response.json()

if __name__ == "__main__":
    writeToLog("from my machine")

