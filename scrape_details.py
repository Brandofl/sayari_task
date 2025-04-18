import requests
import json
import time

# Load companies from step 1
with open("companies_basic.json") as f:
    companies = json.load(f)

headers = {"Content-Type": "application/json"}
detail_url = "https://firststop.sos.nd.gov/api/Records/businessrecord"

detailed = []

for i, company in enumerate(companies):
    print(f"[{i+1}/{len(companies)}] {company['name']}")

    payload = {
        "BusinessId": company["id"],
        "FilingId": None
    }

    try:
        r = requests.post(detail_url, headers=headers, json=payload)
        data = r.json()

        company["registered_agent"] = data.get("Agent", {}).get("AgentName", "N/A")
        company["commercial_registered_agent"] = data.get("CommercialRegisteredAgent", {}).get("AgentName", "N/A")

        # Optional: pull out officer/party names
        parties = data.get("Parties", [])
        company["associated_parties"] = [p.get("Name") for p in parties if "Name" in p]

        detailed.append(company)

        # Be kind to the server!
        time.sleep(0.5)

    except Exception as e:
        print(f"❌ Failed to fetch {company['name']}: {e}")

# Save detailed version
with open("companies_detailed.json", "w") as f:
    json.dump(detailed, f, indent=2)

print(f"\n✅ Saved detailed info for {len(detailed)} companies to 'companies_detailed.json'")
