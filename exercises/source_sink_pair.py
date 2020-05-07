import math
import numpy
from matplotlib import pyplot


"""
For this kind of flow, where we assume that flow is irrotational, incompressible and potential,
we have that for a source/sink, the tangential velocity is 0 (only radial flow) 
while the radial one is  mass / 2 * pi * r.

The potential (phi) function is then m / 2*pi * ln(r) and the stream (psi) function is m / 2*pi * theta
"""

"""MESH DEFINITION"""
N = 50  # Number of points in each direction
x_start, x_end = -2, 2  # Boundaries in x-direction
y_start, y_end = -2, 2  # Boundaries in y-direction
x = numpy.linspace(x_start, x_end, N)  # 1-D array of x-coordinates
y = numpy.linspace(y_start, y_end, N)  # 1-D array of y-coordinates

X, Y = numpy.meshgrid(x, y)


"""PROBLEM CONSTANTS"""
strength_source = 5  # Source strength
strength_sink = -5  # Sink streng - same as source but negative
x_source, y_source = -1, 0  # Position of the sourse
x_sink, y_sink = 1, 0  # Position of the sink


"""COMPUTATIONS"""

# Compute horizontal and vertical velocity (u, v) due to the source
u_source = (strength_source / (2 * math.pi) * (X - x_source) /
            ((X - x_source) ** 2 + (Y - y_source) ** 2))
v_source = (strength_source / (2 * math.pi) * (Y - y_source) /
            ((X - x_source) ** 2 + (Y - y_source) ** 2))

# Compute potential function due to the source
phi_source = strength_source / \
    (2 * math.pi) * numpy.log((X - x_source) ** 2 + (Y - y_source) ** 2)

# Compute horizontal and vertical velocity (u, v) due to the sink
u_sink = (strength_sink / (2 * math.pi) * (X - x_sink) /
          ((X - x_sink) ** 2 + (Y - y_sink) ** 2))
v_sink = (strength_sink / (2 * math.pi) * (Y - y_sink) /
          ((X - x_sink) ** 2 + (Y - y_sink) ** 2))

# Compute potential function due to the sink
phi_sink = strength_sink / \
    (2 * math.pi) * numpy.log((X - x_sink) ** 2 + (Y - y_sink) ** 2)

# Compute horizontal and vertical velocity (u, v) due to the pair source-sink
u_pair = u_source + u_sink
v_pair = v_source + v_sink

# Compute potential function due to the pair source-sink
phi_pair = phi_sink + phi_source


def plot_grid():
    # Set dimensions of figure
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))

    # Axis definition
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)

    # Axis limits
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)

    # Create plot
    pyplot.scatter(X, Y, s=5, color='#CD2305', marker='o')

    # Show plot
    pyplot.show()


def plot_source_streamlines():
    # Set dimensions of figure
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))

    # Axis definition
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)

    # Axis limits
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)

    # Plot streamlines with streamplot lib
    pyplot.streamplot(X, Y, u_source, v_source, density=2,
                      linewidth=1, arrowsize=2, arrowstyle='->')

    # Plot source position
    pyplot.scatter(x_source, y_source, color='#CD2305', s=80, marker='o')

    # Show plot
    pyplot.show()


def plot_sink_streamlines():
    # Set dimensions of figure
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))

    # Axis definition
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)

    # Axis limits
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)

    # Plot streamlines with streamplot lib
    pyplot.streamplot(X, Y, u_sink, v_sink, density=2,
                      linewidth=1, arrowsize=2, arrowstyle='->')

    # Plot sink position
    pyplot.scatter(x_sink, y_sink, color='#CD2305', s=80, marker='o')

    # Show plot
    pyplot.show()


def plot_pair_streamlines():
    # Set dimensions of figure
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))

    # Axis definition
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)

    # Axis limits
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)

    # Plot streamlines with streamplot lib
    pyplot.streamplot(X, Y, u_pair, v_pair, density=2,
                      linewidth=1, arrowsize=2, arrowstyle='->')

    # Plot source position
    pyplot.scatter(x_source, y_source, color='#CD2305', s=80, marker='o')

    # Plot sink position
    pyplot.scatter(x_sink, y_sink, color='#CD2305', s=80, marker='o')

    # Show plot
    pyplot.show()


def plot_pair_potential():
    # Set dimensions of figure
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))

    # Axis definition
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)

    # Axis limits
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)

    # Plot potential function with contour lib
    pyplot.contour(X, Y, phi_pair, 50)

    # Plot source position
    pyplot.scatter(x_source, y_source, color='#CD2305', s=80, marker='o')

    # Plot sink position
    pyplot.scatter(x_sink, y_sink, color='#CD2305', s=80, marker='o')

    # Show plot
    pyplot.show()
