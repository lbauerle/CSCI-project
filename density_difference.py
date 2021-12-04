# import libraries
import numpy as np
import matplotlib.pyplot as plt
import fileinfo as fi

def density_difference(dens_data1, dens_data2, integration_type, grid_spacing):
    """ 
    density_difference is the function that "integrates" out a particular axis.
    
    Inputs:
    1. dens_data1 - denotes the data you are finding the difference with respect to
    2. dens_data2 - tells you what you are subtracting from dens_data1
    3. integration_type - denotes the type of integration that will be performed
    4. grid_spacing - tells you the length of the sub-interval that is being integrated over 
    """
    
    if (integration_type == "riemann"):
        int_type = 2
        densdata_tot = dens_data2 - dens_data1
        densdata_xy = densdata_tot.sum(axis=int_type)*grid_spacing
        
    return densdata_xy
        
    
def density_difference_plot(directory, index, xx, yy, densdata_xy):
    """
    density_difference_plot plots the difference in the densities
    """
    
    i = index
    ii = str(i)
    iii = ii.zfill(7)
    plt.figure()
    
    levels = np.linspace(-1E-3, 1E-3, 1000)
    CS = plt.contourf(xx, yy, densdata_xy, levels=levels, cmap='seismic', extend='both')
    
    # plot formatting
    colorbar = plt.colorbar(CS, label=r'intensity (arb. units)')
    plt.xlim((-20,20))
    plt.ylim((-20,20))
    plt.xlabel('y [a.u.]')
    plt.ylabel('x [a.u.]')
    plt.title('Density Difference Along x-y Plane \n time = %.2f' % (int(i)*.02) + ' a.u.' )
    plt.savefig(f'{directory}/iteration3D-0000{iii}.png')
    plt.show()
    
    
"""def density_difference_calc():
    
    directory = "./13CHD/output_iter/"
    density_file = f'{directory}/td.0000000/density.dx'
    
    size_x, size_y, size_z = fi.numgridpoints(density_file)

    # needed to do this for the code to run! Should I change this in the fileinfo.py file?
    size_x = int(size_x)
    size_y = int(size_y)
    size_z = int(size_z)

    dx, dy, dz = fi.gridspacing(density_file)
    num_x, num_y, num_z = fi.numgridpoints(density_file)
    
    raw_density_data = np.genfromtxt(density_file,skip_header=7,skip_footer=5)
    dens_data_temp = np.array(raw_density_data) 
    dens_data = np.reshape(dens_data_temp,(size_x, size_y, size_z))
    
    x = [np.linspace(-39.9, 39.9, num = size_x)]
    y = [np.linspace(-39.9, 39.9, num = size_y)]
    xx, yy = np.meshgrid(x, y)
    
    # looping through the data files; for now we will just work with one file
    for i in range(0, 100, 100):
        print('working on iteration ' + str(i))
        ii = str(i)
        iii = ii.zfill(7)
        Density2 = f'{directory}/td.{iii}/density.dx'
        densdata2 = np.genfromtxt(Density2,skip_header=7,skip_footer=5)
        dens_data2 = np.array(densdata2)
        dens_data2 = np.reshape(dens_data2,(size_x, size_y, size_z))
    
        densdata_xy = density_difference(dens_data, dens_data2, "riemann", dz)
        density_difference_plot(directory, i, xx, yy, densdata_xy)"""
        
        
def main():
    #density_difference_calc()
    
        directory = "./13CHD/output_iter/"
    density_file = f'{directory}/td.0000000/density.dx'
    
    size_x, size_y, size_z = fi.numgridpoints(density_file)

    # needed to do this for the code to run! Should I change this in the fileinfo.py file?
    size_x = int(size_x)
    size_y = int(size_y)
    size_z = int(size_z)

    dx, dy, dz = fi.gridspacing(density_file)
    num_x, num_y, num_z = fi.numgridpoints(density_file)
    
    raw_density_data = np.genfromtxt(density_file,skip_header=7,skip_footer=5)
    dens_data_temp = np.array(raw_density_data) 
    dens_data = np.reshape(dens_data_temp,(size_x, size_y, size_z))
    
    x = [np.linspace(-39.9, 39.9, num = size_x)]
    y = [np.linspace(-39.9, 39.9, num = size_y)]
    xx, yy = np.meshgrid(x, y)
    
    # looping through the data files; for now we will just work with one file
    for i in range(0, 100, 100):
        print('working on iteration ' + str(i))
        ii = str(i)
        iii = ii.zfill(7)
        Density2 = f'{directory}/td.{iii}/density.dx'
        densdata2 = np.genfromtxt(Density2,skip_header=7,skip_footer=5)
        dens_data2 = np.array(densdata2)
        dens_data2 = np.reshape(dens_data2,(size_x, size_y, size_z))
    
        densdata_xy = density_difference(dens_data, dens_data2, "riemann", dz)
        density_difference_plot(directory, i, xx, yy, densdata_xy)
    
        
if __name__ == '__main__':
    main()
    
        

# denote where files are coming from
#directory = './13CHD/output_iter/'
#density_file = f'{directory}/td.0000000/density.dx'


#size_x, size_y, size_z = fi.numgridpoints(density_file)

# needed to do this for the code to run! Should I change this in the fileinfo.py file?
#size_x = int(size_x)
#size_y = int(size_y)
#size_z = int(size_z)

#dx, dy, dz = fi.gridspacing(density_file)
#num_x, num_y, num_z = fi.numgridpoints(density_file)

# number of points in x, y, and z dimensions as well as grid spacing, dz
#SizeX = np.genfromtxt(Density1, max_rows = 1, dtype = int, usecols = 8, delimiter = ' ')
#SizeY = np.genfromtxt(Density1, max_rows = 1, dtype = int, usecols = 12, delimiter = ' ')
#SizeZ = np.genfromtxt(Density1, max_rows = 1, dtype = int, usecols = 16, delimiter = ' ')
#dz = 0.3

# formatting
#densdata = np.genfromtxt(density_file,skip_header=7,skip_footer=5)
#dens_data = np.array(densdata) #, dtype = np.uint8)
#dens_data = np.reshape(dens_data,(size_x, size_y, size_z))
#x = [np.linspace(-39.9, 39.9, num = size_x)]
#y = [np.linspace(-39.9, 39.9, num = size_y)]
#xx, yy = np.meshgrid(x, y)


# looping through the data files; for now we will just work with one file
#for i in range(0, 100, 100):
#    print('working on iteration ' + str(i))
#    ii = str(i)
#    iii = ii.zfill(7)
#    Density2 = f'{directory}/td.{iii}/density.dx'
#    densdata2 = np.genfromtxt(Density2,skip_header=7,skip_footer=5)
#    dens_data2 = np.array(densdata2)
#    dens_data2 = np.reshape(dens_data2,(size_x, size_y, size_z))
    
#    densdata_xy = density_difference(dens_data, dens_data2, "riemann", dz)
#    density_difference_plot(i, xx, yy, densdata_xy)
