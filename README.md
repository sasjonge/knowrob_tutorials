# KnowRob Tutorials

## Start-Up

Please install docker and docker-compose to your system.

To install and start jupyer-lab and run the notebooks follow this steps:

1. Clone this repository and move into the directory: `git clone https://github.com/knowrob/knowrob_tutorials.git && cd knowrob_tutorials`
2. Run `docker-compose up`
3. Wait till the knowrob_container is ready
4. Open the Jupyter-Lab using the link shown in your terminal

## Run the exercises

To open the notebooks you can choose them from the left sidebar. You can find the first exercise in fs-ex1-robot-structure.ipynb  and the second exercise in fs-ex2-episode-structure.ipynb

## Unit Testing

This container contains two scripts to create and use Unit Tests for jupyer-knowrob notebooks.

The unit tests can be run by executing (only tested on Ubuntu 20.0 with Python3):

`python3 scripts/test_notebooks.py`

