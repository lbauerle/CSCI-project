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
    counter_inputs = parser.parse_args()
    
    parser.add_argument('-l', '--laser', type=str,
                        action='store',
                        required=False,
                        help="This is the laser to be parsed.")
    counter_inputs = parser.parse_args()

    if counter_inputs.config:
        config = configparser.ConfigParser()
        config.read("./config.ini")
        density_file = config['FILES']['density_name']
        laser_file = config['FILES']['laser_name']
        
        return density_file, laser_file
    else:
        density_file = counter_inputs.dens
        laser_file = counter_inputs.laser
        return density_file, laser_file