#!/bin/bash

docker run -it --rm -v ./volume:/usr/src/app/volume/ --name my-running-app my-python-app
