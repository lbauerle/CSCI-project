import numpy as np


def density_data(density_file_name):
    """
    This function extracts the values from a grid-based density file.
    Parameters
    ------------------
    density_file_name : string
        This input is the full path of the .dx file from which to get data.
    Returns
    ------------------
    density_data : array
        This contains all of the density information as an array. Note: the
        data is not formatted back on the original grid.
    """

    file_handle = open(density_file_name, mode='r')
    file_data = []

    for line in file_handle:
        new_line = line.strip()
        file_data.append(new_line)
    file_handle.close()

    # get rid of header
    start = 7 - len(file_data)
    # get rid of footer
    end = len(file_data) - 5

    density_data = np.asarray(file_data[start:end], float)

    return density_data


def grid_size(density_file_name):
    """
    This function extracts the size of the grid from a .dx file type.
    Parameters
    ------------------
    density_file_name : string
        This input is the full path of the .dx file from which to get data.
    Returns
    ------------------
    size_x : float
        This is the size maximum value of the grid along the x-axis for
        symmetric axes. A symmetric x-axis would have values ranging from
        +/- size_x.
    size_y : float
        This is the size maximum value of the grid along the y-axis for
        symmetric axes. A symmetric y-axis would have values ranging from
        +/- size_y.
    size_z : float
        This is the size maximum value of the grid along the z-axis for
        symmetric axes. A symmetric z-axis would have values ranging from
        +/- size_z.
    """

    file_handle = open(density_file_name, mode='r')
    size_line = file_handle.readlines()[1]
    data = size_line.split()
    size_x = abs(float(data[1]))
    size_y = abs(float(data[2]))
    size_z = abs(float(data[3]))

    return size_x, size_y, size_z


def grid_spacing(density_file_name):
    """
    This function extracts the spacing of points in each axis of the grid
    from a .dx file type.
    Parameters
    ------------------
    density_file_name : string
        This input is the full path of the .dx file from which to get data.
    Returns
    ------------------
    dx : float
        This output is the grid spacing in the x-direction.
    dy : float
        This output is the grid spacing in the y-direction.
    dz : float
        This output is the grid spacing in the z-direction.
    """

    file_handle = open(density_file_name, mode='r')
    xline = file_handle.readlines()[2]
    dx = float(xline.split()[1])

    file_handle = open(density_file_name, mode='r')
    yline = file_handle.readlines()[3]
    dy = float(yline.split()[2])

    file_handle = open(density_file_name, mode='r')
    zline = file_handle.readlines()[4]
    dz = float(zline.split()[3])

    return dx, dy, dz


def num_grid_points(density_file_name):
    """
    This function extracts the number of points in each cartesian direction.
    Parameters
    ------------------
    density_file_name : string
        This input is the full path of the .dx file from which to get data.
    Returns
    ------------------
    num_x : int
        This output is the number of points in the x-directions.
    num_y : int
        This output is the number of pointsg in the y-direction.
    num_z : int
        This output is the number of points in the z-direction.
    """

    file_handle = open(density_file_name, mode='r')
    size_line = file_handle.readlines()[0]
    data = size_line.split()

    num_x = int(data[5])
    num_y = int(data[6])
    num_z = int(data[7])

    return num_x, num_y, num_z


def laser_time(laser_file_name):
    """
    This function extracts the time information for the laser output from
    Octopus.
    Parameters
    ------------------
    laser_file_name : string
        This input is the full path of the laser file from octopus.
    Returns
    ------------------
    lasertime : array
        This output is the time data for the electric field in atomic
        units.
    """

    file_handle = open(laser_file_name, mode='r')
    file_data = []

    for line in file_handle:
        new_line = line.strip()
        file_data.append(new_line)
    file_handle.close()

    # line number where data starts (for octopus inputs)
    start = 6
    # line number where data ends (for octopus inputs)
    end = len(file_data)

    data = file_data[start:end]
    time_data = []

    # extract only time information from file
    for i in range(len(data)):
        time_data.append(data[i].split()[1])
        
    time_data = np.array(time_data, float)

    return time_data


def laser_data(laser_file_name, polarization):
    """
    This function extracts the time information for the laser output from
    Octopus.
    Parameters
    ------------------
    laser_file_name : string
        This input is the full path of the laser file from octopus.
    polarization : string
        This input denotes the polarization direction of the laser field.
        Options are 'x', 'y', and 'z'.
    Returns
    ------------------
    amplitude_data : array
        This output is the field amplitude data for the electric field in
        atomic units.
    """

    file_handle = open(laser_file_name, mode='r')
    file_data = []

    for line in file_handle:
        new_line = line.strip()
        file_data.append(new_line)
    file_handle.close()

    # line number where data starts (for octopus inputs)
    start = 6
    # line number where data ends (for octopus inputs)
    end = len(file_data)

    data = file_data[start:end]
    amplitude_data = []

    if polarization == 'x':
        pol = 2
    elif polarization == 'y':
        pol = 3
    elif polarization == 'z':
        pol = 4

    # extract only laser information from file
    for i in range(len(data)):
        amplitude_data.append(data[i].split()[pol])

    amplitude_data = np.array(amplitude_data, float)
    return amplitude_data
