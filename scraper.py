import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "what": "data analyst",
    "results_per_page": 50,
    "content-type": "application/json"
}

response = requests.get(url, params=params, timeout=30)

print("Status Code:", response.status_code)

if response.status_code == 200:

    data = response.json()
    jobs = []

    for job in data.get("results", []):

        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "created": job.get("created"),
            "category": job.get("category", {}).get("label")
        })

    df = pd.DataFrame(jobs)

    # Save as CSV
    df.to_csv("data/raw_jobs.csv", index=False)

    # Save as Excel
    df.to_excel("data/raw_jobs.xlsx", index=False)

    print("\nTotal jobs collected:", len(df))
    print("CSV saved: data/raw_jobs.csv")
    print("Excel saved: data/raw_jobs.xlsx")
    print("Data saved successfully!")

else:
    print("Error:", response.text)