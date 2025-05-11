import os
import re

root = "marketsim"

for dirpath, _, filenames in os.walk(root):
    for filename in filenames:
        if filename.endswith(".py"):
            path = os.path.join(dirpath, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            # Replace top-level imports like 'from fourheap' or 'import fourheap'
            updated = re.sub(
                r"(?<=from\s)(fourheap|simulator|market)(\b)",
                r"marketsim.\1",
                content,
            )
            updated = re.sub(
                r"(?<=import\s)(fourheap|simulator|market)(\b)",
                r"marketsim.\1",
                updated,
            )
            if updated != content:
                print(f"Updated imports in: {path}")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(updated)
