# ecology/network_analysis.py
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import networkx as nx
import os

infile = "abundance/relative_by_genus.csv"
out_edges = "results/cooccurrence_edges.csv"
out_graph = "results/cooccurrence_graph.gml"

df = pd.read_csv(infile, index_col=0).transpose()  # transpose so rows=samples, cols=genus (depends on input)
corr = df.corr(method="spearman").fillna(0)

# threshold edges
thr = 0.6
edges = []
for i in corr.index:
    for j in corr.columns:
        if i < j and abs(corr.loc[i,j]) >= thr:
            edges.append([i,j,corr.loc[i,j]])

edges_df = pd.DataFrame(edges, columns=["node1","node2","weight"])
edges_df.to_csv(out_edges, index=False)
print("Saved edges:", out_edges)

G = nx.Graph()
for _, row in edges_df.iterrows():
    G.add_edge(row["node1"], row["node2"], weight=row["weight"])
nx.write_gml(G, out_graph)
print("Saved graph:", out_graph)
