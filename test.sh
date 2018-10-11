#!/bin/bash
#Generate Test File
/usr/bin/env python3 unit_tests.py
#Plot using ez_plot 
/usr/bin/env python3 ez_plot.py test.json
#Remove test data file
rm test.json

