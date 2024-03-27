import sys
import json
from pathlib import Path

index_path = Path(sys.argv[1])
issue_author = sys.argv[2]

config = json.load(open(index_path / "indexer-config.json", "r"))
echo("YES" if issue_author in config["approve"] else "NO")
print("YES" if issue_author in config["approve"] else "NO")
return "YES" if issue_author in config["approve"] else "NO"
