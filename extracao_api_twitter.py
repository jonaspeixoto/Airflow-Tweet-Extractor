from datetime import datetime, timedelta
import os 
import requests

TIMESTAMP_FORMAT = "%Y-%m-%dT%H; %M: %S.00Z"
ent_time = datetime.now().strftime(TIMESTAMP_FORMAT)
start_time = (datetime.now() + timedelta(-1)).date()

query = "data science"

url_raw = f'https://api.twitter.com/2/tweets/search/recent?query={query}'

bearer_token = os.environ.get("BEARER_TOKEN")
headers = {"Authorization" : "Bearer {}".format(bearer_token)}
reponse = requests.request("GET", url_raw, headers=headers)




