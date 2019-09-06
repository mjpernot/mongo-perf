#!/usr/bin/python
# Classification (U)

"""Program:  mongo_perf.py

    Description:  Performance administration program for Mongo database
        servers.  Has a number of functions to include capturing database
        performance statistical data and sending the data out in a number of
        formats or to the database.

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

"""


# Libraries and Global Variables

# Standard
import sys
import datetime

# Third party
import ast

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.cmds_gen as cmds_gen
import mongo_lib.mongo_libs as mongo_libs
import mongo_lib.mongo_class as mongo_class
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def mongo_stat(server, args_array, **kwargs):

    """Function:  mongo_stat

    Description:  Creates and executes the mongostat utility program.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            req_arg -> List of options to add to cmd line.
            opt_arg -> Dictionary of additional options to add.
            ofile -> file name - Name of output file.
            db_tbl database:table_name -> Mongo database and table name.
            class_cfg -> Mongo server configuration.

    """

    args_array = dict(args_array)
    cmd = mongo_libs.create_cmd(server, args_array, "mongostat", "-p",
                                **kwargs)

    # Is Polling present
    if "-b" in args_array:
        cmd.append(args_array["-b"])

    if "-j" in args_array:

        for row in cmds_gen.run_prog(cmd, retdata=True).rstrip().split("\n"):

            # Evaluate "row" to dict format.
            key, value = ast.literal_eval(row).popitem()

            # Add date as mongostat --json only provides time value.
            value.update({"Date":
                          datetime.datetime.strftime(datetime.datetime.now(),
                                                     "%Y-%m-%d")})
            mongo_libs.json_2_out(value, **kwargs)

    else:
        cmds_gen.run_prog(cmd, **kwargs)


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.
        (input) **kwargs:
            req_arg -> List of options to add to cmd line.
            opt_arg -> Dictionary of additional options to add.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    outfile = args_array.get("-o", False)
    db_tbl = args_array.get("-i", False)
    cfg = None
    server = mongo_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mongo_class.Server)
    server.connect()

    if args_array.get("-m", False):
        cfg = gen_libs.load_module(args_array["-m"], args_array["-d"])

    # Call function(s) - intersection of command line and function dict.
    for x in set(args_array.keys()) & set(func_dict.keys()):
        func_dict[x](server, args_array, ofile=outfile, db_tbl=db_tbl,
                     class_cfg=cfg, **kwargs)

    cmds_gen.disconnect([server])


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        file_chk_list -> contains the options which will have files included.
        file_crt_list -> contains options which require files to be created.
        func_dict -> dictionary list for the function calls or other options.
        opt_arg_list -> contains optional arguments for the command line.
        opt_con_req_list -> contains the options that require other options.
        opt_def_dict -> contains options with their default values.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        req_arg_list -> contains arguments to add to command line by default.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-d", "-p"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-S": mongo_stat}
    opt_arg_list = {"-j": "--json", "-n": "-n="}
    opt_con_req_list = {"-i": ["-m", "-j"]}
    opt_def_dict = {"-i": "sysmon:mongo_perf", "-n": "1", "-b": "1"}
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-b", "-i", "-m", "-n", "-o", "-p"]
    req_arg_list = ["--authenticationDatabase=admin"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list, opt_def_dict)

    if not gen_libs.help_func(args_array, __version__, help_message):
        if not arg_parser.arg_require(args_array, opt_req_list) \
           and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
           and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
           and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
           and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                           file_crt_list):
            run_program(args_array, func_dict, req_arg=req_arg_list,
                        opt_arg=opt_arg_list)


if __name__ == "__main__":
    sys.exit(main())
