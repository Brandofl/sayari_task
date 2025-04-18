import requests
import json

search_url = "https://firststop.sos.nd.gov/api/Records/businesssearch"
headers = {"Content-Type": "application/json"}
payload = {
    "SEARCH_VALUE": "X",
    "STARTS_WITH_YN": "true",
    "ACTIVE_ONLY_YN": False
}

resp = requests.post(search_url, json=payload, headers=headers)
rows = resp.json().get("rows", {})

companies = []
for _, item in rows.items():
    companies.append({
        "name": item["TITLE"][0],
        "type": item["TITLE"][1],
        "record_num": item["RECORD_NUM"],
        "id": item["ID"]
    })

with open("companies_basic.json", "w") as f:
    json.dump(companies, f, indent=2)

print(f"✅ Saved {len(companies)} companies to 'companies_basic.json'.")
