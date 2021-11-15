import numpy as np

def densitydata(densfilename):
    """
    This function extracts the values from a grid-based density file.
    
    Parameters
    ------------------
    densfilename : string
        This input is the full path of the .dx file from which to get data.
    
    Returns
    ------------------
    densdata : array
        This contains all of the density information as an array. Note: the 
        data is not formatted back on the original grid.
    """
    
    file_handle = open(densfilename, mode='r')
    filedata = []
    
    for line in file_handle:
        new_line = line.strip()
        filedata.append(new_line)
    file_handle.close()
    
    start = 7 - len(filedata) # get rid of header
    end = len(filedata) - 5   # get rid of footer
    
    densdata = np.asarray(filedata[start:end])
    
    return densdata

def gridsize(densfilename):
    """
    This function extracts the size of the grid from a .dx file type.
    
    Parameters
    ------------------
    densfilename : string
        This input is the full path of the .dx file from which to get data.
    
    Returns
    ------------------
    sizex : float
        This is the size maximum value of the grid along the x-axis for 
        symmetric axes. A symmetric x-axis would have values ranging from 
        +/- sizex.
        
    sizey : float
        This is the size maximum value of the grid along the y-axis for 
        symmetric axes. A symmetric y-axis would have values ranging from 
        +/- sizey.
        
    sizez : float
        This is the size maximum value of the grid along the z-axis for 
        symmetric axes. A symmetric z-axis would have values ranging from 
        +/- sizez.
    """
    
    file_handle = open(densfilename, mode='r')
    print(file_handle.readlines())

    
    return sizex, sizey, sizez

def gridspacing(densfilename):
    """
    This function extracts the spacing of points in each axis of the grid 
    from a .dx file type.
    
    Parameters
    ------------------
    densfilename : string
        This input is the full path of the .dx file from which to get data.
    
    Returns
    ------------------
    dx : float
        This output is the grid spacing in the x-direction.
    
    dy : float
        This output is the grid spacing in the x-direction.

    dz : float
        This output is the grid spacing in the x-direction.
        
    """
    
    return dx, dy, dz

def numgridpoints(densfilename):
    """
    This function extracts the number of points in each cartesian direction.
    
    Parameters
    ------------------
    densfilename : string
        This input is the full path of the .dx file from which to get data.
    
    Returns
    ------------------
    numx : int
        This output is the number of points in the x-directions.
    
    numy : int
        This output is the number of pointsg in the x-direction.

    numz : int
        This output is the number of points in the x-direction.
    """
    
    return numx, numy, numz

def lasertime(laserfilename):
    """
    This function extracts the time information for the laser output from 
    Octopus.
    
    Parameters
    ------------------
    laserfilename : string
        This input is the full path of the laser file from octopus.
    
    Returns
    ------------------
    lasertime : array
        This output is the time data for the electric field in atomic 
        units.
    """
    
    return lasertime

def laserdata(laserfilename):
    """
    This function extracts the time information for the laser output from 
    Octopus.
    
    Parameters
    ------------------
    laserfilename : string
        This input is the full path of the laser file from octopus.
    
    Returns
    ------------------
    laserdata : array
        This output is the field amplitude data for the electric field in atomic 
        units.
    """
    
    return laserdata