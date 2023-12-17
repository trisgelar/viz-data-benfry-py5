import py5
import pandas as pd
import numpy as np

class Times:
    def __init__(self, data_path):
        self.year_interval = 10
        self.volume_interval = 10
        self.volume_interval_minor = 5
        self.bar_width = 4
        self.plot_x1 = 120
        self.plot_x2 = py5.width - 80
        self.plot_y1 = 60
        self.plot_y2 = py5.height - 70
        self.label_x = 50
        self.label_y = py5.height - 25
        
        self.data = pd.read_csv(
            data_path,
            sep="\t",
            header=0,
            names=['year', 'milk', 'tea', 'coffe'],
            dtype={
                'year': 'int32',
                'milk': 'float32',
                'tea': 'float32',
                'coffe': 'float32',  
                }
            )
        self.minmax = {
                'data_min': 0,
                'data_max': py5.ceil(
                    max(
                        self.data[['milk', 'tea', 'coffe']].max()
                        ) / self.volume_interval) * self.volume_interval,
                'year_min': self.data['year'].min(),
                'year_max': self.data['year'].max(),
            }
        self.names = ['milk', 'tea', 'coffe']
        self.current_col = 0
        
    def data_points_by_name(self, name):
        return self.data[name]
    
    def incr_col(self):
        if(self.current_col >= 2):
            self.current_col = 2
        else:
            self.current_col += 1
            
    def decr_col(self):
        if(self.current_col <= 0):
            self.current_col = 0
        else:
            self.current_col -= 1
    
    def years(self):
        return self.data_points_by_name('year')
    
    def font(self):
        return py5.create_font("SansSerif", 20)
    
    def setup(self):
        py5.smooth()
        py5.text_font(self.font())
    
    def draw(self):
        self.draw_background()        
        self.draw_data_areas()
        self.draw_highlight()
        
        self.draw_title()
        self.draw_year_labels()
        self.draw_volume_labels()
        self.draw_axis_label()
        
    def draw_background(self):
        py5.fill(255);
        py5.rect_mode(py5.CORNERS);
        py5.no_stroke( );
        py5.rect(self.plot_x1, self.plot_y1,
                 self.plot_x2, self.plot_y2);
        
    def draw_title(self):
        py5.fill(0)
        py5.text_size(20)
        py5.text_align(py5.LEFT)
        py5.text(
            self.names[self.current_col],
            self.plot_x1,
            self.plot_y1-10)
        
    def draw_axis_label(self):
        py5.fill(0)
        py5.text_size(13)
        py5.text_leading(15)
        
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text("Gallons\nconsumed\nper capita", self.label_x, (self.plot_y1+self.plot_y2)/2)
        py5.text_align(py5.CENTER)
        py5.text("Year", (self.plot_x1+self.plot_x2)/2, self.label_y)
        
    def draw_year_labels(self):
        py5.fill(0)
        py5.text_size(10)
        py5.text_align(py5.CENTER, py5.TOP)
        
        py5.stroke(225);
        py5.stroke_weight(1);
        
        years = self.years()
        for index in range(len(years)):
            if(years[index] % self.year_interval == 0):
                x = py5.remap(
                    years[index],
                    self.minmax['year_min'],
                    self.minmax['year_max'],
                    self.plot_x1, self.plot_x2)
                py5.text(f"{years[index]}", x, self.plot_y2 + 10)
                py5.line(x, self.plot_y1, x, self.plot_y2);
                
    
    def draw_volume_labels(self):
        py5.fill(0)
        py5.text_size(10)
        py5.stroke(128)
        py5.stroke_weight(1)
        
        volume_range = np.arange(
            self.minmax['data_min'],
            self.minmax['data_max']+1, self.volume_interval_minor)
        
        for v in volume_range:
            if(v % self.volume_interval_minor == 0):
                y = py5.remap(v, self.minmax['data_min'],
                              self.minmax['data_max'],
                              self.plot_y2, self.plot_y1)
                if(v % self.volume_interval == 0):
                    if(v == self.minmax['data_min']):
                        py5.text_align(py5.RIGHT)
                    elif (v == self.minmax['data_max']):
                        py5.text_align(py5.RIGHT, py5.TOP)
                    else:
                        py5.text_align(py5.RIGHT, py5.CENTER)
                    py5.text(f"{v}", self.plot_x1 - 10, y)
                    py5.line(self.plot_x1 - 4, y, self.plot_x1, y)
                else:
                    py5.line(self.plot_x1 - 2, y, self.plot_x1, y)

    def draw_data_points(self):
        py5.no_fill()
        py5.stroke_weight(2)
        py5.stroke('#5679C1')
        data = self.data_points_by_name(self.names[self.current_col])
        years = self.years()
        for index in range(len(data)):
            x = py5.remap(years[index], self.minmax['year_min'], self.minmax['year_max'], self.plot_x1, self.plot_x2)
            y = py5.remap(data[index], self.minmax['data_min'], self.minmax['data_max'], self.plot_y2, self.plot_y1)
            py5.point(x,y)
            
    def draw_data_lines(self):
        py5.no_fill()
        py5.stroke_weight(0.5)
        py5.stroke('#5679C1')
        py5.begin_shape()
        data = self.data_points_by_name(self.names[self.current_col])
        years = self.years()
        for index in range(len(data)):
            x = py5.remap(years[index], self.minmax['year_min'], self.minmax['year_max'], self.plot_x1, self.plot_x2)
            y = py5.remap(data[index], self.minmax['data_min'], self.minmax['data_max'], self.plot_y2, self.plot_y1)
            py5.vertex(x,y)
        py5.end_shape()
        
    def draw_data_curves(self):
        py5.no_fill()
        py5.stroke_weight(2)
        py5.stroke('#5679C1')
        py5.begin_shape()
        data = self.data_points_by_name(self.names[self.current_col])
        years = self.years()
        for index in range(len(data)):
            x = py5.remap(years[index], self.minmax['year_min'], self.minmax['year_max'], self.plot_x1, self.plot_x2)
            y = py5.remap(data[index], self.minmax['data_min'], self.minmax['data_max'], self.plot_y2, self.plot_y1)
            
            py5.curve_vertex(x,y)
            if ((index == 0) or index == len(data)-1):
                py5.curve_vertex(x,y)
                
        py5.end_shape()
        
    def draw_data_areas(self):
        py5.no_stroke( );
        py5.fill('#5679C1');
        py5.begin_shape()
        data = self.data_points_by_name(self.names[self.current_col])
        years = self.years()
        for index in range(len(data)):
            x = py5.remap(years[index], self.minmax['year_min'], self.minmax['year_max'], self.plot_x1, self.plot_x2)
            y = py5.remap(data[index], self.minmax['data_min'], self.minmax['data_max'], self.plot_y2, self.plot_y1)
            py5.vertex(x,y)
        
        py5.vertex(self.plot_x2, self.plot_y2)
        py5.vertex(self.plot_x1, self.plot_y2)
                
        py5.end_shape(py5.CLOSE)
        
    def draw_data_bars(self):
        py5.no_stroke( );
        py5.fill('#5679C1');
        py5.rect_mode(py5.CORNERS)
        
        data = self.data_points_by_name(self.names[self.current_col])
        years = self.years()
        for index in range(len(data)):
            x = py5.remap(years[index], self.minmax['year_min'], self.minmax['year_max'], self.plot_x1, self.plot_x2)
            y = py5.remap(data[index], self.minmax['data_min'], self.minmax['data_max'], self.plot_y2, self.plot_y1)
            py5.rect(x-self.bar_width/2,y, x+self.bar_width/2, self.plot_y2)
        
    def draw_highlight(self):
        data = self.data_points_by_name(
            self.names[self.current_col])
        years = self.years()
        for index in range(len(data)):
            x = py5.remap(years[index],
                          self.minmax['year_min'],
                          self.minmax['year_max'],
                          self.plot_x1, self.plot_x2)
            y = py5.remap(data[index],
                          self.minmax['data_min'],
                          self.minmax['data_max'],
                          self.plot_y2, self.plot_y1)
            if(py5.dist(py5.mouse_x, py5.mouse_y, x, y) < 3):
                py5.stroke_weight(10)
                py5.point(x, y)
                py5.fill(0)
                py5.text_size(10)
                py5.text_align(py5.CENTER)
                
                value = '{:.2f}'.format(data[index])
                
                py5.text(f"{value} ({years[index]})", x, y-10)
                
font_list = py5.Py5Font.list()

def setup():
    global tm
    py5.size(720, 405)
    tm = Times('data/milk-tea-coffee.tsv')
    tm.setup()
    
def draw():
    py5.background(225);
    tm.draw()
    
def key_pressed():
    if(py5.key == ']'):
        tm.incr_col()
    elif(py5.key == '['):
        tm.decr_col()

py5.run_sketch()