import requests

url = "https://dark-sky.p.rapidapi.com/%7Blatitude%7D,%7Blongitude%7D"

querystring = {"units":"auto","lang":"en"}

headers = {
	"X-RapidAPI-Key": "244e0f2e0bmsh47fbd082f3edfa5p1649b2jsnd9eb3928926f",
	"X-RapidAPI-Host": "dark-sky.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)