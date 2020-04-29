#!/bin/bash
# Integration testing program for the program module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Integration testing..."
test/integration/mongo_perf/mongo_stat.py
