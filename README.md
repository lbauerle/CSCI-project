# CSCI-project
1. fileinfo.py
* This file reads in the parameters from a given density file. It is able to read in the density data, find the size of the grid that was used, the grid spacing, number of grid points, and the duration of the laser pulse as well as the corresponding measurements of the laser intensity.

2. config.ini
* This file is where the user will add their inputs for their code. This package is compatible with TDDFT outputs of most types, meaning that the user just needs to feed in their specific parameters and it should run on their density.dx files.

3. density_difference.py
* This file utilizes parameters which are specified from the fileinfo.py file. It is able to read in argumnets specified from an config.ini file, compute the difference between a density plot at an arbitrary time (within the laser pulse) and a reference density plot (at time zero). It is able to plot these differences at each time step while integrating out a third axis to form a heat map representing the electron density within the given molecule. This function is also able to plot the laser pulse as a function of time and use each of the snapshots acquired to form a movie which was the goal of this project!

4. output.txt
* This is a sample output file so that the user can see what is being computed in the code. This is a nice benchmark for other users to be sure that they are running this code properly for the N2+ system.

5. run.sh
* This file is responsible for reading in the inputs from the parameter file and using them to run the density_difference.py file. An output.txt file is specified to let the user know what iterations have been computed.

6. project_env.yml 
* Records the conda environment that was used in the development of this project.
