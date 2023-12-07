#!/usr/bin/env bash

# Computer libs
# Add `-U` after `pip install` to update packages instead of installing them
py -3 -m pip install robotpy -U
py -3 -m pip install coverage -U
py -3 -m pip install robotpy[rev] -U
py -3 -m pip install robotpy[cscore] -U
py -3 -m pip install robotpy[navx] -U

# roboRIO libs
py -3 -m robotpy_installer download-python
py -3 -m robotpy_installer download robotpy
py -3 -m robotpy_installer download robotpy[rev]
py -3 -m robotpy_installer download robotpy[cscore]
py -3 -m robotpy_installer download robotpy[navx]