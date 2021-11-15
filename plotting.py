import matplotlib.pyplot as plt
import numpy as np


def timecontourplot(timedata, axisdata, contourdata, axis, maxint, cmap, 
                    imagetype='png'):
    """
    This function takes time-dependent contourdata and plots it for density
    information along a single axis.
    
    Parameters
    ------------------
    timedata : string
        This input is the full path to the time data for the laser pulse
        as a 1D array.
        
    axisdata : string
        This input is the full path to the file containing values of axis1 
        as a 1D array.
        
    contourdata : string
        This input is the full path to the array that has the contourdata.
        Contourdata needs to have the dimensions of axis1data x axis2data.
           
    axis : string
        This input is the cartesian axis label for the axis. Options are 'x',
        'y', and 'z'.
        
    maxint: float
        This input is the maximum value of the contourdata. This value is 
        used to set the range of values for the contour intensity.

    cmap : string
        This input is the colormap for the contour plot. The default is 
        'seismic'. Other options can be found at 
        https://matplotlib.org/stable/tutorials/colors/colormaps.html

    imagetype : string
        This input is the imagetype to save figure as. Default is 'png'.

    Returns
    ------------------
    Figure : figure
        This output is the time-dependent contour plot of the data specified. 
    """
    return figure


def twodimcontourplot(axis1data, axis2data, contourdata, axis1, axis2, 
                      maxint, cmap='seismic', imagetype='png'):
    """
    This function takes contourdata and plots it for density information in 
    a single plane.
    
    Parameters
    ------------------
    axis1data : string
        This input is the full path to the file containing values of axis1 
        as a 1D array.
        
    axis2data : string
        This input is the full path to the file containing values of axis2 
        as a 1D array.       

    contourdata : string
        This input is the full path to the array that has the contourdata.
        Contourdata needs to have the dimensions of axis1data x axis2data.
    
    axis1 : string
        This input is the cartesian axis label for axis1. Options are 'x',
        'y', and 'z'.
        
    axis2 : string
        This input is the cartesian axis label for axis2. Options are 'x',
        'y', and 'z'.

    maxint: float
        This input is the maximum value of the contourdata. This value is 
        used to set the range of values for the contour intensity.
        
    cmap : string
        This input is the colormap for the contour plot. The default is 
        'seismic'. Other options can be found at 
        https://matplotlib.org/stable/tutorials/colors/colormaps.html

    imagetype : string
        This input is the imagetype to save figure as. Default is 'png'.

    Returns
    ------------------
    Figure : figure
        This output is the contour plot with laser pulse of the data specified.    
    """
    return figure


def timelasercontourplot(timedata, axisdata, contourdata, laserdata, axis, 
                         maxint, cmap='seismic', imagetype='png'):
    """
    This function takes time-dependent contourdata and plots it for density
    information along a single axis with plot of laser field.
    
    Parameters
    ------------------
    timedata : string
        This input is the full path to the time data for the laser pulse
        as a 1D array.
        
    axisdata : string
        This input is the full path to the file containing values of axis1 
        as a 1D array.
        
    contourdata : string
        This input is the full path to the array that has the contourdata.
        Contourdata needs to have the dimensions of axis1data x axis2data.
        
    laserdata : string
        This input is the full path to the amplitude data for the laser
        pulse as a 1D array.
    
    axis : string
        This input is the cartesian axis label for the axis. Options are 'x',
        'y', and 'z'.
        
    maxint: float
        This input is the maximum value of the contourdata. This value is 
        used to set the range of values for the contour intensity.

    cmap : string
        This input is the colormap for the contour plot. The default is 
        'seismic'. Other options can be found at 
        https://matplotlib.org/stable/tutorials/colors/colormaps.html

    imagetype : string
        This input is the imagetype to save figure as. Default is 'png'.

    Returns
    ------------------
    Figure : figure
        This output is the contour plot with laser pulse of the data specified.    
    """
    return figure

def twodimlasercontourplot(axis1data, axis2data, contourdata, timedata, 
                           laserdata, axis1, axis2, maxint, cmap='seismic', 
                           imagetype='png'):
    """
    This function takes contourdata and plots it for density information in 
    a single plane with plot of laser indicating the field amplitude at the 
    time of the contour data.
    
    Parameters
    ------------------
    axis1data : string
        This input is the full path to the file containing values of axis1 
        as a 1D array.
        
    axis2data : string
        This input is the full path to the file containing values of axis2 
        as a 1D array.       

    contourdata : string
        This input is the full path to the array that has the contourdata.
        Contourdata needs to have the dimensions of axis1data x axis2data.
    
    timedata : string
        This input is the full path to the time data for the laser pulse
        as a 1D array.
        
    laserdata : string
        This input is the full path to the amplitude data for the laser
        pulse as a 1D array.
    
    axis1 : string
        This input is the cartesian axis label for axis1. Options are 'x',
        'y', and 'z'.
        
    axis2 : string
        This input is the cartesian axis label for axis2. Options are 'x',
        'y', and 'z'.

    maxint: float
        This input is the maximum value of the contourdata. This value is 
        used to set the range of values for the contour intensity.
        
    cmap : string
        This input is the colormap for the contour plot. The default is 
        'seismic'. Other options can be found at 
        https://matplotlib.org/stable/tutorials/colors/colormaps.html

    imagetype : string
        This input is the imagetype to save figure as. Default is 'png'.

    Returns
    ------------------
    Figure : figure
        This output is the contour plot with laser pulse of the data specified.    
    """
    return figure


def makegif(figurefolder, figuretype='png'):
    """
    This function takes a series of figures and turns them into a movie 
    (.gif) to see time dependence of 2D contour plots.
    
    Parameters
    ------------------
    figurefolder : string
        This input is the location of the figures to turn into a gif. 
        Default is .png file type.
    
    Returns
    ------------------
    gif : figure
        This output is the .gif of the figures from the folder specified.    
    """
    return gif