#!/bin/bash

.venv/Scripts/activate

cd src
pylint .
cd ..