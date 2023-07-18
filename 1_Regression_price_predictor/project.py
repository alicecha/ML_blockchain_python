import pandas as pd
df = pd.DataFrame({"A":[1608854400,1609027200]})

df["A"] = pd.to_datetime(df["A"], unit="s")

print(df)

