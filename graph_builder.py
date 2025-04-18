import json
import networkx as nx
import matplotlib.pyplot as plt

# Load detailed data
with open("companies_detailed.json") as f:
    companies = json.load(f)

G = nx.Graph()

for company in companies:
    company_name = company["name"]

    # Add the company node
    G.add_node(company_name, type="company")

    # Link to Registered Agent
    agent = company.get("registered_agent", "N/A")
    if agent and agent != "N/A":
        G.add_node(agent, type="agent")
        G.add_edge(company_name, agent)

    # Link to Commercial Registered Agent
    commercial_agent = company.get("commercial_registered_agent", "N/A")
    if commercial_agent and commercial_agent != "N/A" and commercial_agent != agent:
        G.add_node(commercial_agent, type="commercial_agent")
        G.add_edge(company_name, commercial_agent)

    # Link to Associated Parties
    for party in company.get("associated_parties", []):
        if party:
            G.add_node(party, type="party")
            G.add_edge(company_name, party)

# Draw graph
plt.figure(figsize=(20, 15))
pos = nx.spring_layout(G, k=0.5)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color='lightblue',
    font_size=8,
    edge_color='gray'
)

plt.title("ND Companies (X*) - Entity Relationship Graph")
plt.tight_layout()
plt.savefig("company_graph.png")
plt.show()
