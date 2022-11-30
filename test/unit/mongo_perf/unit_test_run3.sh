#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python3 ./test/unit/mongo_perf/_process_json.py
/usr/bin/python3 ./test/unit/mongo_perf/get_data.py
/usr/bin/python3 ./test/unit/mongo_perf/help_message.py
/usr/bin/python3 ./test/unit/mongo_perf/main.py
/usr/bin/python3 ./test/unit/mongo_perf/mongo_stat.py
/usr/bin/python3 ./test/unit/mongo_perf/run_program.py
