#!/bin/bash

# To regenerate the documentation, you must have pdoc installed
# pip3 install pdoc

PYTHONPATH=../
pdoc --html --overwrite --html-no-source core
