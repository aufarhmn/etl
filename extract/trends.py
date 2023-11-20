import os
import csv
import datetime as dt
from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()
client = ApifyClient(os.getenv('APIFY_TOKEN'))

def ExtractTrends() -> None:
    run_input = {
        "searchTerms": ["Blackpink"],
        "timeRange": "today 1-m",
        "viewedFrom": "",
        "outputAsISODate": True,
        "csvOutput": True,
    }

    FILE_NAME = f"../frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}.csv"

    run = client.actor("emastra/google-trends-scraper").call(run_input=run_input)

    with open(FILE_NAME, mode='w', newline='') as csv_file:
        fieldnames = ['date', 'Blackpink']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            writer.writerow(item)

    print(f"Data saved to {FILE_NAME}")