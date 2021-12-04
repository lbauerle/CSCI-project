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
        description='Get state counts filtered by year.')

    parser.add_argument('-f', '--file', type=str,
                        action='store',
                        required=False,
                        help="This is the file to be parsed.")
    counter_inputs = parser.parse_args()

    if counter_inputs.config:
        config = configparser.ConfigParser()
        config.read("./config.ini")
        filename = config['FILES']['filename']
        return filename
    else:
        filename = counter_inputs.file
        return filename