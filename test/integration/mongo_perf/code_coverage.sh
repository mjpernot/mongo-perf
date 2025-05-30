#!/bin/bash
# Integration test code coverage for program module.
# This will run the Python code coverage module against all integration test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_perf test/integration/mongo_perf/get_data.py
coverage run -a --source=mongo_perf test/integration/mongo_perf/main.py
coverage run -a --source=mongo_perf test/integration/mongo_perf/mongo_stat.py
coverage run -a --source=mongo_perf test/integration/mongo_perf/run_program.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
