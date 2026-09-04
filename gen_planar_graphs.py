import os
from sage.all import graphs
from tqdm import tqdm
# Use Sage's built-in generator
os.makedirs("out_misc_graphs", exist_ok=True)
counter=0
iterator = graphs.planar_graphs(12,minimum_degree=5)
for i,G in tqdm(enumerate(iterator)):
        if G.is_connected() and G.is_regular(5):
                counter+=1
                G.plot(layout='planar').save(os.path.join("out_misc_graphs", f"my_graph_{i}.png"))
print(counter)