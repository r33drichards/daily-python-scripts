import requests
from datetime import datetime
import os
import json
import pytz



api_key = os.environ.get("AIRTABLE_API_KEY")

# https://airtable.com/appgA2YK85EpXbOOF/tblKRaKSLb00NhPCp/viwUWHsIHz0XHh5xj?blocks=hide

base_id = "appgA2YK85EpXbOOF"
table_name = "tblKRaKSLb00NhPCp"
api_url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

api_key = os.environ.get("AIRTABLE_API_KEY")

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
}

# today_date = (
#     datetime.now()
# ).strftime("%Y-%m-%d")
# as califonia time

today_date = datetime.now(
    tz=pytz.timezone("America/Los_Angeles")
).strftime("%Y-%m-%d")


data = {
    "records": [
        {
            "fields": {
                "date": today_date
            }
        }
    ]
}


def create_airtable_column():
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Record added successfully!")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    create_airtable_column()
