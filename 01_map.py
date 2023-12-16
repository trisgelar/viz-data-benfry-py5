import py5
import numpy as np
import pandas as pd

def setup():
    global usamap
    global locations   
    py5.size(640, 400) 
    usamap = py5.load_image("assets/map.png")
    #locations = pd.read_csv("data/locations.tsv", sep="\t", header=None)
    locations = pd.read_csv("data/locations.tsv",
                            sep="\t",
                            header=None,
                            names=['name', 'x', 'y'],
                            dtype={
                                'x': np.float64,
                                'y': np.float64
                                }
                            )
    
def draw():
    py5.background(255)
    py5.image(usamap, 0, 0)
    
    py5.smooth()
    py5.fill(192, 0, 0)
    py5.no_stroke()
    
    for i in range(len(locations)):
        py5.ellipse(locations.loc[i, 'x'], locations.loc[i, 'y'], 9, 9)
        #print(locations.loc[i, "name"], locations.loc[i, "x"], locations.loc[i, "y"]):
        #print(locations.iloc[i, 0], locations.iloc[i, 2])
        
        #for ind in df.index:
        #    print(df['Name'][ind], df['Stream'][ind])
        
        #for index, row in df.iterrows():
        #    print(row["Name"], row["Age"])
        
        #for row in df.itertuples(index=True, name='Pandas'):
        #    print(getattr(row, "Name"), getattr(row, "Percentage"))
        
        #print(df.apply(lambda row: row["Name"] + " " +
        #    str(row["Percentage"]), axis=1))
        
        
py5.run_sketch()