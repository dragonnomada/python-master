import pandas as pd

tables = pd.read_html('https://en.wikipedia.org/wiki/Minnesota')

for table in tables:
    print(table)
    print("-" * 40)