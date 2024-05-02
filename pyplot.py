# Import necessary libraries
from matplotlib import pyplot as plt 
import numpy as np

def plot_line(x, y):
    # Create a figure and axes
    fig = plt.figure()
    axes = plt.axes()
    
    # Drawing a continuous line
    axes.plot(x, y)  # Drawing a line using axes
    plt.plot(x, y)    # Drawing a line using the built-in pyplot
    
    # Drawing multiple lines in one figure
    axes.plot(x, np.sin(x))
    axes.plot(x, np.cos(x))
    
    # Adjusting the color of the lines
    plt.plot(x, np.sin(x - 0), color='blue')         # Specify color by name
    plt.plot(x, np.sin(x - 1), color='g')            # Short color code (rgbcmyk)
    plt.plot(x, np.sin(x - 2), color='0.75')         # Grayscale between 0 and 1
    plt.plot(x, np.sin(x - 3), color='#FFDD44')      # Hex code (RRGGBB, 00 to FF)
    plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3)) # RGB tuple, values 0 to 1
    plt.plot(x, np.sin(x - 5), color='chartreuse')   # HTML color names supported
    
    # Adjusting the line style
    plt.plot(x, x + 0, linestyle='solid')
    plt.plot(x, x + 1, linestyle='dashed')
    plt.plot(x, x + 2, linestyle='dashdot')
    plt.plot(x, x + 3, linestyle='dotted')
    
    # Using short notation for line styles
    plt.plot(x, x + 4, '-')    # Solid
    plt.plot(x, x + 5, '--')   # Dashed
    plt.plot(x, x + 6, '-.')   # Dashdot
    plt.plot(x, x + 7, ':')    # Dotted
    
    # Mix of line style and color notation
    plt.plot(x, x + 0, '-g')   # Solid green
    plt.plot(x, x + 1, '--c')  # Dashed cyan
    plt.plot(x, x + 2, '-.k')  # Dashdot black
    plt.plot(x, x + 3, ':r')   # Dotted red
    
    # Adjusting axes limits
    plt.xlim(10, 15)
    plt.ylim(10, 15)
    
    # Labeling the plot
    plt.title('joe amin')
    plt.xlabel('current')
    plt.ylabel('volt')
    
    # Labeling with axes using set method
    axes.set(title='joe amin', xlim=(0, 10), ylim=(0, 10), xlabel='current', ylabel='volt')
    
    # Labeling with multiple plots and creating a legend
    plt.plot(x, y, label='joe amin')
    plt.plot(x, y, label='hhh')
    plt.title('simple graph')  # Title for the overall plot
    plt.legend()  # Display legend for labeled plots
def scatter_plot(x, y):
    """
    Create a scatter plot using both 'plot' and 'scatter' methods.

    Parameters:
    - x: array-like, x-axis data
    - y: array-like, y-axis data

    Returns:
    None
    """
    # Using plot method
    fig = plt.figure()
    ax = plt.axes()

    # Scatter plot with points only
    ax.plot(x, y, 'o', color='k')

    # Scatter plot with a continuous line and points
    ax.plot(x, y, '-ok')  # Continuous line with points

    # Using scatter method directly
    ax.scatter(x, y, s=np.random.random(100) * 100, c=np.random.random(100), alpha=0.3)
    # s: size, c: color (0 to 1), alpha: transparency (0 to 1)

def contour_plot(x, y):
    """
    Create a contour plot based on given x and y values.

    Parameters:
    - x: array-like, x-axis data
    - y: array-like, y-axis data

    Returns:
    None
    """
    # Creating a meshgrid
    X, Y = np.meshgrid(x, y)

    # Generating Z values based on a function (example: X^2 + Y^2)
    Z = X**2 + Y**2

    # Creating a contour plot with a colormap 'RdGy'
    plt.contour(X, Y, Z, cmap='RdGy')

    # Adding a colorbar for reference
    plt.colorbar()

def custom_histogram(freq):
    """
    Create a custom histogram with multiple overlays.

    Parameters:
    - freq: array-like, input data for the histogram

    Returns:
    None
    """
    # Basic histogram
    plt.hist(freq, color='b', bins=20, edgecolor='k', alpha=0.68, label='Blue Histogram')

    # Overlays
    plt.hist(freq, color='b', bins=20, edgecolor='k', alpha=0.6)
    plt.hist(freq, color='r', bins=20, edgecolor='k', alpha=0.45)
    plt.hist(freq, color='g', bins=20, edgecolor='k', alpha=0.55)

    # Get frequency and bin edges using numpy
    count, bin_edge = np.histogram(freq)

    # Additional customization if needed
    plt.legend()
    plt.title('Custom Histogram')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

