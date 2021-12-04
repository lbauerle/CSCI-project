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
                        help="This is the denisty to be parsed.")
   
    parser.add_argument('-l', '--laser', type=str,
                        action='store',
                        required=False,
                        help="This is the laser to be parsed.")
    
    parser.add_argument('-p', '--pol', type=str,
                        action='store',
                        required=False,
                        help="This is the polarization of the laser.")
    counter_inputs = parser.parse_args()

    if counter_inputs.config:
        config = configparser.ConfigParser()
        config.read("./config.ini")
        density_file = config['DENSITY']['density_name']
        laser_file = config['LASER']['laser_name']
        polarization = config['LASER']['polarization']
        
        return density_file, laser_file, polarization
    else:
        density_file = counter_inputs.dens
        laser_file = counter_inputs.laser
        polarization = counter_inputs.pol
        return density_file, laser_file, polarization