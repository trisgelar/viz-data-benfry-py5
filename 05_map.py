import py5
import numpy as np
import pandas as pd

class MapViz:
    def __init__(self, map_path, data_path, locations_path, names_path):
        self.map_path = map_path
        self.font_path = "assets/Univers-Bold-12.vlw"
        self.data_min = py5.MAX_FLOAT
        self.data_max = py5.MIN_FLOAT
        self.locations = pd.read_csv(
            locations_path,
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
        
        self.names = pd.read_csv(
            names_path,
            sep="\t",
            header=None,
            names=['abbrev', 'name'],
            dtype={
                'name': "string",
                }
            )
       
    def font(self):
        return py5.load_font(self.font_path)
    
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
            self.draw_data(
                row['x'], row['y'], abbrev, index)
    
    def draw_data(self, x, y, abbrev, index):
        value = self.data.loc[index, 'delta']
        name = self.names.loc[index, 'name']
        radius = 0
        two_color = ['#333366', '#EC5166']
        if (value > 0):
            radius = py5.remap(
                value, 0, self.data_max, 1.5, 15)
            py5.fill(two_color[0])
        else:
            radius = py5.remap(
                value, 0, self.data_min, 1.5, 15)
            py5.fill(two_color[1])
        py5.ellipse_mode(py5.RADIUS);
        py5.ellipse(x, y, radius, radius)
        
        if(py5.dist(x, y, py5.mouse_x, py5.mouse_y) < radius+2):
            py5.fill(0)
            py5.text_align(py5.CENTER)
            py5.text(f"{name} ( {value} )", x, y-radius-4);
    
mv = MapViz("assets/map.png","data/random.tsv", "data/locations.tsv", "data/names.tsv")

def setup():
    global usa_map
    py5.size(640, 400)
    mv.minmax()
    font = mv.font()
    py5.text_font(font)
    usa_map = mv.map()
    
def draw():
    py5.background(255)
    py5.image(usa_map, 0, 0)
    mv.draw()
        
py5.run_sketch()