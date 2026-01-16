import json

notebook_path = "covid19_impact_visualization.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Remove widgets metadata from notebook-level
nb.get("metadata", {}).pop("widgets", None)

# Remove widgets metadata from every cell
for cell in nb.get("cells", []):
    cell.get("metadata", {}).pop("widgets", None)

# Save cleaned notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2)
