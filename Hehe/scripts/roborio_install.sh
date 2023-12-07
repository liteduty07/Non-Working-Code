#!/usr/bin/env bash

py -3 -m robotpy_installer install-python
py -3 -m robotpy_installer install robotpy
py -3 -m robotpy_installer install robotpy[rev]
py -3 -m robotpy_installer install robotpy[cscore]
py -3 -m robotpy_installer install robotpy[navx]
