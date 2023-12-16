import py5
import numpy as np
import pandas as pd

class MapViz:
    def __init__(self, map_path, data_path, locations_path):
        self.map_path = map_path
        self.data_path = data_path
        self.locations_path = locations_path
        self.data_min = py5.MAX_FLOAT
        self.data_max = py5.MIN_FLOAT
        self.locations = pd.read_csv(
            self.locations_path,
            sep="\t",
            header=None,
            names=['name', 'x', 'y'],
            dtype={
                'x': np.float64,
                'y': np.float64
                }
            )
        self.data = pd.read_csv(
            data_path,
            sep="\t",
            header=None,
            names=['name', 'delta'],
            dtype={
                'delta': np.float64,
                }
            )
        
    def minmax(self):
        delta = self.data['delta']
        self.data_max = delta.max()
        self.data_min = delta.min()
        
    def map(self):
        usa_map = py5.load_image(self.map_path)
        return usa_map
    
    def draw(self):
        py5.smooth()
        py5.fill(192, 0, 0)
        py5.no_stroke()
        
        for index, row in self.locations.iterrows():
            abbrev = row['name']
            self.draw_data(row['x'], row['y'], abbrev, index)
    
    def draw_data(self, x, y, abbrev, index):
        value = self.data.loc[index, 'delta']
        diameter = 0
        two_color = ['#333366', '#EC5166']
        if (value > 0):
            diameter = py5.remap(value, 0, self.data_max, 3, 30)
            py5.fill(two_color[0])
        else:
            diameter = py5.remap(value, 0, self.data_min, 3, 30)
            py5.fill(two_color[1])
        
        py5.ellipse(x, y, diameter, diameter)
        
        
    
mv = MapViz("assets/map.png","data/random.tsv", "data/locations.tsv")

def setup():
    global usa_map
    py5.size(640, 400)
    mv.minmax()
    usa_map = mv.map()
    
def draw():
    py5.background(255)
    py5.image(usa_map, 0, 0)
    mv.draw()
        
py5.run_sketch()


