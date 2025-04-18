
- `scrape_companies.py`: Crawls and collects basic information on all companies beginning with "X".
- `scrape_details.py`: Uses each company’s ID to fetch detailed information (e.g., registered agents, parties).
- `graph_builder.py`: Uses `NetworkX` and `matplotlib` to plot a graph of companies and their associated entities.
- `companies_basic.json`: JSON output of all company metadata from the initial scrape.
- `companies_detailed.json`: Intended output of the detail scraper (partially complete or mocked if blocked).
- `graph_output.png`: Visualization of the data showing entities as nodes (companies, agents, owners).
