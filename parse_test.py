import configparser
import argparse


def input_parser():
    """
    This function parses through flags or a config file to get input
    parameters for the state and hour information desired.

    Returns
    ------------
    """

    parser = argparse.ArgumentParser(
        description='')

    parser.add_argument('-d', '--dens', type=str,
                        action='store',
                        required=False,
                        help="This is the directory containing the density file to be parsed.")
   
    parser.add_argument('-l', '--laser', type=str,
                        action='store',
                        required=False,
                        help="This is the directory for the laser file to be parsed.")
    
    parser.add_argument('-p', '--pol', type=str,
                        action='store',
                        required=False,
                        help="This is the polarization of the laser.")
    parser.add_argument('-m', '--maxiter', type=str,
                        action='store',
                        required=False,
                        help="This is the maximum number of iterations to be processed.")
    parser.add_argument('-i', '--iter', type=str,
                        action='store',
                        required=False,
                        help="This is the iteration step for outputs.")
    parser.add_argument('-p', '--plane', type=str,
                        action='store',
                        required=False,
                        help="This is the plane to plot density difference.")
    parser.add_argument('-n', '--int', type=str,
                        action='store',
                        required=False,
                        help="This is the integration method to use.")
    parser.add_argument('-t', '--time', type=str,
                        action='store',
                        required=False,
                        help="This is units to use for time.")
    parser.add_argument('-c', '--cmap', type=str,
                        action='store',
                        required=False,
                        help="This is the colormap to use for plotting.")
    parser.add_argument('-s', '--save', type=str,
                        action='store',
                        required=False,
                        help="This is directory to save plots in.")
    parser.add_argument('-l', '--level', type=str,
                        action='store',
                        required=False,
                        help="This is maximum intensity levle to use for the contour plots.")
    counter_inputs = parser.parse_args()

    if counter_inputs.config:
        config = configparser.ConfigParser()
        config.read("./config.ini")
        density_file = config['DENSITY']['density_directory']
        max_iteration = config['DENSITY']['max_iteration']
        iteration_step = config['DENSITY']['iteration_step']
        plane = config['DENSITY']['plane']
        integration_method = config['DENSITY']['integration_method']
        
        laser_file = config['LASER']['laser_directory']
        polarization = config['LASER']['polarization']
        time_units = config['LASER']['time_units']
        
        cmap = config['PLOTTING']['cmap']
        level_max = config['PLOTTING']['level_max']
        save_directory = config['PLOTTING']['save_directory']
        
        return density_file, laser_file, polarization, max_iteration, \
               iteration_step, plane, integration_method, time_units, \
               cmap, level_max, save_directory
    else:
        density_file = counter_inputs.dens
        laser_file = counter_inputs.laser
        polarization = counter_inputs.pol
        max_iteration = counter_inputs.maxiter
        iteration_step = counter_inputs.iter
        plane = counter_inputs.plane
        integration_method = counter_inputs.int
        time_units = counter_inputs.time
        cmap = counter_inputs.cmap
        level_max  = counter_inputs.level
        save_directory = counter_inputs.save
        return density_file, laser_file, polarization, max_iteration, \
               iteration_step, plane, integration_method, time_units, \
               cmap, level_max, save_directory