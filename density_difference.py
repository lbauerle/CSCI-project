# import libraries
import numpy as np
import matplotlib.pyplot as plt
import fileinfo as fi
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import os
import imageio


def density_difference(dens_data1, dens_data2, integration_type, grid_spacing):
    """
    density_difference is the function that "integrates" out a particular axis.

    Inputs:
    1. dens_data1 - denotes the data you are finding the difference with
       respect to
    2. dens_data2 - tells you what you are subtracting from dens_data1
    3. integration_type - denotes the type of integration that will be
       performed
    4. grid_spacing - tells you the length of the sub-interval that is being
       integrated over
    """

    if (integration_type == "riemann"):
        int_type = 2
        densdata_tot = dens_data2 - dens_data1
        densdata_xy = densdata_tot.sum(axis=int_type)*grid_spacing

    return densdata_xy


def density_difference_plot(density_directory, index, xx, yy, densdata_xy):
    """
    density_difference_plot plots the difference in the densities
    """

    i = index
    ii = str(i)
    iii = ii.zfill(7)
    plt.figure()
    levels = np.linspace(-1E-3, 1E-3, 1000)
    CS = plt.contourf(xx, yy, densdata_xy, levels=levels, cmap='seismic',
                      extend='both')

    # plot formatting
    colorbar = plt.colorbar(CS, label=r'intensity (arb. units)')
    plt.xlim((-10, 10))
    plt.ylim((-10, 10))
    plt.xlabel('y [a.u.]')
    plt.ylabel('x [a.u.]')
    plt.title('Density Difference Along x-y Plane \n time = %.2f'
              % (int(i)*.02) + ' a.u.')
    plt.savefig(f'{density_directory}/iteration3D-0000{iii}.png')
    plt.show()


def density_difference_laser_plot(density_directory, laser_file_name, polarization,
                                  index, xx, yy, densdata_xy):
    """
    This function plots the density difference with the laser and point
    during the pulse at which the density difference is taken.
    Parameters
    ------------------
    density_file_name : string
        This input is the full path of the .dx file from which to get data.
    laser_file_name : string
        This input is the full path of the laser file from which to get data.
    Returns
    ------------------

    """
    # get laser information
    laser_amplitude = fi.laser_data(laser_file_name, polarization)
    laser_time = fi.laser_time(laser_file_name)

    # index formatting for iterations
    i = index
    ii = str(i)
    iii = ii.zfill(7)

    # make figure with subplots
    fig = plt.figure(figsize=(15, 20))
    gs = mpl.gridspec.GridSpec(2, 1, height_ratios=[1, 2],
                               width_ratios=[2])
    # density difference subplot
    ax1 = fig.add_subplot(gs[1, 0])
    # laser subplot
    ax2 = fig.add_subplot(gs[0, 0])
    axins = inset_axes(ax1, width='5%', height='100%', loc=6,
                       bbox_to_anchor=(1.05, 0., 1, 1),
                       bbox_transform=ax1.transAxes, borderpad=0)

    # plotting density difference
    levels = np.linspace(-1E-3, 1E-3, 1000)
    CS = ax1.contourf(xx, yy, densdata_xy, levels=levels, cmap='seismic',
                      extend='both')
    plt.tick_params(which='both', top=False, right=False)
    colorbar = plt.colorbar(CS, label=r'intensity (arb. units)', cax=axins)
    ax1.set_ylim((-10, 10))
    ax1.set_xlim((-10, 10))
    ax1.set_xlabel('y [a.u.]')
    ax1.set_ylabel('x [a.u.]')
    ax1.title.set_text('Density Difference Along x-y Plane')

    # plotting laser
    ax2.set_autoscalex_on(False)
    ax2.plot(laser_time, laser_amplitude, 'k')
    ax2.plot(laser_time[i], laser_amplitude[i], marker='X', color='r')
    ax2.set_xlim((0, max(laser_time)))
    ax2.set_ylim((-max(laser_amplitude)-0.001, max(laser_amplitude)+0.001))
    ax2.set_xlabel('time [a.u.]')
    ax2.set_ylabel('amplitude [a.u.]')

    # save figure
    plt.savefig(f'{density_directory}/iteration3D-laser-0000{iii}.png',
                bbox_inches='tight')
    plt.show()


def density_difference_calc():
    """
    Inputs
    Returns
    """

    directory = "./N2+/output_iter"
    density_file = f'{density_directory}/td.0000000/density.dx'

    num_x, num_y, num_z = fi.num_grid_points(density_file)
    size_x, size_y, size_z = fi.grid_size(density_file)
    dx, dy, dz = fi.grid_spacing(density_file)

    raw_density_data = np.genfromtxt(density_file, skip_header=7,
                                     skip_footer=5)
    dens_data_temp = np.array(raw_density_data)
    dens_data = np.reshape(dens_data_temp, (num_x, num_y, num_z))

    x = [np.linspace(-size_x, size_x, num=num_x)]
    y = [np.linspace(-size_y, size_y, num=num_y)]
    xx, yy = np.meshgrid(x, y)

    # looping through the data files; for now we will just work with one file
    for i in range(0, 300, 200):
        print('working on iteration ' + str(i))
        ii = str(i)
        iii = ii.zfill(7)
        Density2 = f'{directory}/td.{iii}/density.dx'
        dens_data2 = fi.density_data(Density2)
        dens_data2 = np.reshape(dens_data2, (num_x, num_y, num_z))

        # densdata2 = np.genfromtxt(Density2, skip_header=7, skip_footer=5)
        # dens_data2 = np.array(densdata2)

        densdata_xy = density_difference(dens_data, dens_data2, "riemann", dz)
        density_difference_plot(density_directory, i, xx, yy, densdata_xy)
        density_difference_laser_plot(density_directory,
                                      '/home/jovyan/CSCI-project/laser',
                                      'x', i, xx, yy, densdata_xy)


def movie(figure_directory, file_type, fps):
    """
    This function turns the plots of the density difference to a movie 
    in time. Note: The order of the movie will coincide with the 
    alphabetical order of the density or density difference plots.

    Parameters
    ------------------
    figure_directory : string
        This input is the full path of the .png saved plots.
    file_type: string
        This is the file type for the plots. The default is '.png'.
    fps : int
        This is the frames per second. The default value is 400.   
    """
    images = []
    for file_name in os.listdir(figure_directory):
        if file_name.endswith(file_type):
            file_path = os.path.join(figure_directory, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave(f'{figure_directory}\\density_difference_movie.gif', images, fps=fps)


def main():
    density_difference_calc()


if __name__ == '__main__':
    main()
