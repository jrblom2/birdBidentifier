# Bird Bidentifier
Authors: Joseph Blom, Logan Boswell, Grayson Snyder

This project uses the python wrapper for the birdNET identification model birdLib to record and identify common North American birds.
The defualt flow stores the sampled birds in a CSV format to be uploaded to Microsoft Azure.

## Usage
The shell script `./acquireBirds.sh` will listen on a hard coded mic input using `arecord`. This file will be cut after 30 sec, then birdLib is called
on the result to analyze the audio. 