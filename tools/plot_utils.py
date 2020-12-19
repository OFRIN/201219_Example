import numpy as np
import matplotlib.pyplot as plt

def line_data(data, color):
    if color == 'red':
        color = 'r--'
        
    plt.plot(data, data, color)

def bar_data(x_data, y_data):
    plt.bar(x_data, y_data)

def plot_show():
    plt.show()
