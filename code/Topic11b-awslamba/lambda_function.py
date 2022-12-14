import airtableDAO


print('Loading function')

def lambda_handler(event, context):
    print('about to run log')
    airtableDAO.writeToLog("test from aws")
    print("airtable log done")
