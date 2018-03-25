#!/bin/bash

# To regenerate the documentation, you must have pdoc installed
# pip3 install pdoc

cd ../core
pdoc --html --overwrite --html-no-source --html-dir ../doc .
cd ~-
