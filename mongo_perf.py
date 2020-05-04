#!/usr/bin/python
# Classification (U)

"""Program:  mongo_perf.py

    Description:  Performance monitoring program for a Mongo database.  There
        are a number of functions to include capturing database performance
        statistical data as single run or over a period of time.  The data can
        be converted to either standard format or JSON format.  In addition,
        the data can be sent to standard out, file, or a Mongo database.

    Usage:
        mongo_perf.py -c file -d path {-S [ -j | -n count | -b seconds |
            -o file [-a] | -f | -i db_name:table_name -m file | -p path ]}
            [-v | -h]

    Arguments:
        -c file => Mongo configuration file.  Required argument.
        -d dir path => Directory path to config file (-c option).
            Required argument.
        -S => Mongo Statistics option.
        -n {count} => Number of loops to run the program. Default = 1.
        -b {seconds} => Polling interval in seconds.  Default = 1.
        -j => Return output in JSON format.
            This option is required for -i option.
        -f => Flatten the JSON data structure to file and standard out.
        -i {database:collection} => Name of database and collection to
            insert the database performance statistics data into.
            Default value:  sysmon.mongo_perf
            This option requires options:  -m and -j
        -m file => Mongo configuration file for inserting results into a
            Mongo database.  This is loaded as a python module, do not
            include the .py extension with the name.
            This option is required for -i option.
        -o directory_path/file => Directory path and file name for output.
            Default is to overwrite the file.
            Use the -a option to append to an existing file.
        -a => Append output to output file.
        -p path =>  Path to Mongo binaries.  Only required if the user
            running the program does not have the Mongo binaries in their path.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and/or -h overrides all other options.
        NOTE 2:  -o option:  Only the last entry will be written to file
            unless the -a option is selected which will append the entries.

    Known Bug:  The -a option is not working for the standard out format.

    Notes:
        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format is for connecting to a Mongo database or
            replica set for monitoring.  A second configuration file can also
            be used to connect to a Mongo database or replica set to insert the
            results of the performance monitoring into.

            There are two ways to connect methods:  single Mongo database or a
            Mongo replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 27017)
            conf_file = None
            auth = True

            2.)  Replica set connection:  Same format as above, but with these
                additional entries at the end of the configuration file.
                Note:  If not connecting, just set these entries to None.

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_perf.py -c mongo -d config -S -j -n 12 -b 5 -i -m mongo2
        mongo_perf.py -c mongo -d config -S -o /data/perf_file.txt -a -n 5

"""


# Libraries and Global Variables

# Standard
import sys

# Third party
import ast
import json

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

    mode = "w"
    indent = 4
    args_array = dict(args_array)
    cmd = mongo_libs.create_cmd(server, args_array, "mongostat", "-p",
                                **kwargs)

    if args_array.get("-a", False):
        mode = "a"

    if args_array.get("-f", False):
        indent = None

    if "-b" in args_array:
        cmd.append(args_array["-b"])

    if "-j" in args_array:

        for row in cmds_gen.run_prog(cmd, retdata=True).rstrip().split("\n"):

            # Evaluate "row" to dict format.
            _, value = ast.literal_eval(row).popitem()
            data = {"Server": server.name,
                    "AsOf": gen_libs.get_date() + " " + value["time"],
                    "PerfStats": value}

            if kwargs.get("db_tbl", False) and kwargs.get("class_cfg", False):
                db, tbl = kwargs.get("db_tbl").split(":")
                mongo_libs.ins_doc(kwargs.get("class_cfg"), db, tbl, data)

            else:
                gen_libs.print_data(json.dumps(data, indent=indent), mode=mode,
                                    **kwargs)

                # Any other entries in the loop will append to file.
                mode = "a"

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
    server = gen_libs.load_module(args_array["-c"], args_array["-d"])

    if args_array.get("-m", False):
        cfg = gen_libs.load_module(args_array["-m"], args_array["-d"])

    if server.repset:
        mongo = mongo_class.RepSet(server.name, server.user, server.passwd,
                                   host=server.host, port=server.port,
                                   auth=server.auth, repset=server.repset)

    else:
        mongo = mongo_libs.create_instance(args_array["-c"], args_array["-d"],
                                           mongo_class.Server)

    mongo.connect()

    # Call function(s) - intersection of command line and function dict.
    for x in set(args_array.keys()) & set(func_dict.keys()):
        func_dict[x](mongo, args_array, ofile=outfile, db_tbl=db_tbl,
                     class_cfg=cfg, **kwargs)

    cmds_gen.disconnect([mongo])


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
        opt_def_dict2 -> default values for "-S" and "-j" options combination.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        req_arg_list -> contains arguments to add to command line by default.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-d", "-p"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-S": mongo_stat}
    opt_arg_list = {"-j": "--json", "-n": "-n="}
    opt_con_req_list = {"-i": ["-m", "-j"]}
    opt_def_dict = {"-i": "sysmon:mongo_perf", "-n": "1", "-b": "1"}
    opt_def_dict2 = {"-n": "1", "-b": "1"}
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-b", "-i", "-m", "-n", "-o", "-p"]
    req_arg_list = ["--authenticationDatabase=admin"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list,
                                       opt_def_dict)

    # Add default arguments for certain argument combinations.
    if "-S" in args_array.keys() and "-j" in args_array.keys():
        args_array = arg_parser.arg_add_def(args_array, opt_def_dict2)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                       file_crt_list):
        run_program(args_array, func_dict, req_arg=req_arg_list,
                    opt_arg=opt_arg_list)


if __name__ == "__main__":
    sys.exit(main())
