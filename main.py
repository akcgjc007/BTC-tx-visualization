# Data taken from: https://snap.stanford.edu/data/soc-sign-bitcoin-otc.html

# import pandas module  
import pandas as pd
from datetime import datetime
from GraphVisualization import GraphVisualization

# making dataframe  
df = pd.read_csv(
    "soc-sign-bitcoinotc.csv", 
    header=None, 
    names=["source", "target", "rating", "time"]
)
for i in df.index:
    df.at[i, "time"] = datetime.fromtimestamp(df.at[i, "time"])

df = df[:1000]

# n = max(max(df.source), max(df.target))+1
# adjList = [set() for i in range(n)]

G = GraphVisualization("Visualizing Bitcoin transaction data") 
for i in df.iterrows():
    G.addEdge(int(i[1].source), int(i[1].target))
    # adjList[int(i[1].source)].add((int(i[1].target), int(i[1].rating), i[1].time))

# print(df)


# Driver code 
G.visualize()



# 4, 8, 10, 11
