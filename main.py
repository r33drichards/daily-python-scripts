import requests
from datetime import datetime
import os
import json
import argparse
import sys

import pytz


# https://airtable.com/appgA2YK85EpXbOOF/tblKRaKSLb00NhPCp/viwUWHsIHz0XHh5xj?blocks=hide

base_id = "appgA2YK85EpXbOOF"
table_name = "tblKRaKSLb00NhPCp"

api_key = os.environ.get("AIRTABLE_API_KEY")

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
}


def create_airtable_column(args):
    data = get_date(args)
    api_url = f"https://api.airtable.com/v0/{args.base_id}/{args.table_name}"
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Record added successfully!")
    else:
        print(f"Error: {response.status_code}")


def parse_args(args):
    parser = argparse.ArgumentParser(description="Add new field to airtable as current date in specified format and timezone")
    parser.add_argument("--format", type=str, default="%Y-%m-%d", help="strftime format")
    parser.add_argument("--timezone", type=str, default="America/Los_Angeles", help="timezone")
    # base id and table name
    parser.add_argument("--base-id", type=str, default=base_id, help="airtable base id")
    parser.add_argument("--table-name", type=str, default=table_name, help="airtable table name")
    return parser.parse_args(args)


def get_date(args):
    return datetime.now(
        tz=pytz.timezone(args.timezone)
    ).strftime(args.format)


def get_data(args):
    return {
        "fields": {
            "date": get_date(args)
        }
    }


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    create_airtable_column(args)
