# Python project for monitoring performance on a Mongo database.
# Classification (U)

# Description:
  This program is used to monitor performance on a Mongo database, to include capturing database statistical data and formatting the output of the performance report


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Capture database performance statistical data.
  * Convert performance output into a number of formats or send to a database.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - mongo_lib/mongo_class
    - mongo_lib/mongo_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-perf.git
```

Install/upgrade system modules.

```
cd mongo-perf
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create Mongodb configuration file.

```
cd config
cp mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```


# Program Descriptions:
### Program: mongo_perf.py
##### Description: Performance monitoring program for a Mongo database.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mongo-perf/mongo_perf.py -h
```


# Help Message:
  Below is the help message for the program.  Recommend running the -h option on the command line to see the latest help message.

    Program:  mongo_perf.py

    Description:  Performance administration program for Mongo database servers.
        Has a number of functions to include capturing database performance
        statistical data and sending the data out in a number of formats or to
        the database.

    Usage:
        mongo_perf.py -c file -d path {-S {-j | -n count | -b seconds |
            -o dir_path/file | -i db_name:table_name [-m file] |  -p path}}

    Arguments:
        -c file => Mongo server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -S => Mongo Statistics option.
        -j => Return output in JSON format.  Required for -i option.
        -n {count} => Number of loops to run the program. Default = 1.
        -b {seconds} => Polling interval in seconds.  Default = 1.
        -i {database:collection} => Name of database and collection to
            insert the database statistics data into.
            Requires options:  -m and -j
            Default value:  sysmon.mongo_perf
        -m file => Mongo config file.  Is loaded as a python, do not
            include the .py extension with the name.
            Required for -i option.
        -o path/file => Directory path and file name for output.  Can be
            used with -S option.
            Format compability:
                -S option => JSON and standard.
        -p path =>  Path to Mongo binaries.  Only required if the user
            running the program does not have the Mongo binaries in their path.
        -v => Display version of this program.
        -h => Help and usage message.
            NOTE 1:  -v and/or -h overrides all other options.

    Notes:
        Mongo configuration file format (mongo.py).  The configuration
            file format for the Mongo connection used for inserting data into
            a database.  There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 27017)
            conf_file = None
            auth = True

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:
            
            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_perf.py -c mongo -d config -S -j -n 12 -b 5 -i -m mongo2


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mongo_perf.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-perf.git
```

Install/upgrade system modules.

```
cd mongo-perf
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for mongo_perf.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-perf
```


### Unit:  help_message
```
test/unit/mongo_perf/help_message.py
```

### Unit:  
```
test/unit/mongo_perf/
```

### Unit:  
```
test/unit/mongo_perf/
```

### Unit:  run_program
```
test/unit/mongo_perf/run_program.py
```

### Unit:  main
```
test/unit/mongo_perf/main.py
```

### All unit testing
```
test/unit/mongo_perf/unit_test_run.sh
```

### Code coverage program
```
test/unit/mongo_perf/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the mongo_perf.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-perf.git
```

Install/upgrade system modules.

```
cd mongo-perf
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.

```
cd test/integration/mongo_perf/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Integration test runs for mongo_perf.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-perf
```


### Integration:  
```
test/integration/mongo_perf/
```

### All integration testing
```
test/integration/mongo_perf/integration_test_run.sh
```

### Code coverage program
```
test/integration/mongo_perf/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the mongo_perf.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-perf.git
```

Install/upgrade system modules.

```
cd mongo-perf
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.
```
cd test/blackbox/mongo_perf/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, also set these variables.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Blackbox test run for mongo_perf.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-perf
```

### Blackbox:  
```
test/blackbox/mongo_perf/blackbox_test.sh
```

