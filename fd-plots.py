import pandas as pd
from manim import *

# file parameters

csvFile = {
        'name': 'spiral_15_low.csv', # name of csv file
        'x': 'missn_time', # x axis
        'y': '_roll__deg', # y axis
        'x_label': 'Mission Time', # x axis label
        'y_label': 'Roll Angle', # y axis label
        'title': 'Spiral Mode: Low Altitude', # title of the plot       
}

# config.background_color = WHITE
df = pd.read_csv(csvFile['name']) # add csv file
missn_time = df.get(csvFile['x']).to_list()
roll_deg = df.get(csvFile['y']).to_list()

class Plot(Scene):
        def construct(self):
                ax = Axes(
                        x_range = [min(missn_time), max(missn_time)+10,5],
                        y_range = [min(roll_deg), max(roll_deg),5],
                        axis_config = {
                                'include_numbers': True,
                                'tip_shape': StealthTip,
                                # 'color': BLACK
                        },
                        y_length = 7,
                )
                x_axis_label = Tex(csvFile['x_label'])
                y_axis_label = Tex(csvFile['y_label'])
                
                
                x_label = ax.get_x_axis_label(x_axis_label.scale(0.7))
                y_label = ax.get_y_axis_label(y_axis_label.scale(0.7))
                
                                      
                plot = ax.plot_line_graph(missn_time, roll_deg, add_vertex_dots=False, line_color=WHITE)
                
                x_value = roll_deg.index(max(roll_deg))
                point = ax.c2p(missn_time[x_value], max(roll_deg))
                label = Tex("Max. Amplitude")
                dot = Dot(point)
                label.next_to(dot, DR, buff=SMALL_BUFF) 
                
                graph_group = VGroup(ax, plot, dot, label)
                graph_group.scale(0.9)
                graph_group.to_edge(UP, buff=0.5)               
                
                self.play(Create(ax),Create(x_label), Create(y_label))
                self.wait(1)
                
                self.play(Create(plot), run_time=5)
                self.wait(1)
                self.play(Create(dot), Create(label))
                self.wait(1)
                
                title = Title(csvFile['title'])
                title.to_edge(DOWN, buff=-0.1)
                self.play(Write(title)) 
                
                # self.play(Create())
                self.wait(4)