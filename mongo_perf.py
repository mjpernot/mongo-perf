#!/bin/sh
# Classification (U)

# Shell commands follow
# Next line is bilingual: it starts a comment in Python & is a no-op in shell
""":"

# Find a suitable python interpreter (can adapt for specific needs)
# NOTE: Ignore this section if passing the -h option to the program.
#   This code must be included in the program's initial docstring.
for cmd in python3.12 python3.9 ; do
   command -v > /dev/null $cmd && exec $cmd $0 "$@"
done

echo "OMG Python not found, exiting...."

exit 2

# Previous line is bilingual: it ends a comment in Python & is a no-op in shell
# Shell commands end here

   Program:  mongo_perf.py

    Description:  Performance monitoring program for a Mongo database.  There
        are a number of functions to include capturing database performance
        statistical data as single run or over a period of time.  The data can
        be converted to either standard format or JSON format.  In addition,
        the data can be sent to standard out, written to a file, emailed out,
        or inserted into a Mongo database.

    Usage:
        mongo_perf.py -c file -d path
            {-S [-f] [-n count] [-b seconds] [-o file [-a]]
                [-t ToEmail [ToEmail2 ...] [-s Subject Line] [-u]]
                [-i db_name:table_name [-m file]] [-p path] [-w] [-z] [-r]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c file => Mongo configuration file.
        -d dir path => Directory path to config file (-c option).

        -S => Mongo Statistics option.
            -f => Flatten the JSON data structure to file and standard out.
            -n count => Number of loops to run the program. Default = 1.
            -b seconds => Polling interval in seconds.  Default = 1.
            -t to_email [to_email2 ...] => Enables emailing capability for an
                    option if the option allows it.  Sends output to one or
                    more email addresses.
                -s Subject Line => Subject line of email.  If none is provided
                    then a default one will be used.
                -u => Override the default mail command and use mailx.
            -i [database:collection] => Name of database and collection to
                    insert the database performance statistics data into.
                    Default value:  sysmon.mongo_perf
                -m file => Mongo configuration file for inserting results into
                    a Mongo database.  This is loaded as a python module, do
                    not include the .py extension with the name.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to output file.
            -p path =>  Path to Mongo binaries.  Only required if the user
                running the program does not have the Mongo binaries in their
                path.
            -w => Suppress printing initial connection errors.
            -z => Suppress standard out.
            -r => Turn off TLS checking.

        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and/or -h overrides all other options.

    Known Bug:  The -a option is not working for the standard out format.

    Notes:
        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format is for connecting to a Mongo database or
            replica set for monitoring.  A second configuration file can also
            be used to connect to a Mongo database or replica set to insert the
            results of the performance monitoring into.

            There are two ways to connect methods:  single Mongo database or a
            Mongo replica set.

            Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "USER"
            japd = "PSWORD"
            host = "HOST_IP"
            name = "HOSTNAME"
            port = 27017
            direct_connect = True
            conf_file = None
            auth = True
            auth_db = "admin"
            auth_mech = "SCRAM-SHA-1"

            Replica set connection:  Same format as above, but with these
                additional entries at the end of the configuration file.  By
                default all these entries are set to None to represent not
                connecting to a replica set.

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

            If Mongo is set to use TLS or SSL connections, then one or more of
                the following entries will need to be completed to connect
                using TLS or SSL protocols.
                Note:  Read the configuration file to determine which entries
                    will need to be set.

                SSL:
                    auth_type = None
                    ssl_client_ca = None
                    ssl_client_key = None
                    ssl_client_cert = None
                    ssl_client_phrase = None
                TLS:
                    auth_type = None
                    tls_ca_certs = None
                    tls_certkey = None
                    tls_certkey_phrase = None

            Note:  FIPS Environment for Mongo.
              If operating in a FIPS 104-2 environment, this package will
              require at least a minimum of pymongo==3.8.0 or better.  It will
              also require a manual change to the auth.py module in the pymongo
              package.  See below for changes to auth.py.

            - Locate the auth.py file python installed packages on the system
                in the pymongo package directory.
            - Edit the file and locate the "_password_digest" function.
            - In the "_password_digest" function there is an line that should
                match: "md5hash = hashlib.md5()".  Change it to
                "md5hash = hashlib.md5(usedforsecurity=False)".
            - Lastly, it will require the Mongo configuration file entry
                auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_perf.py -c mongo -d config -S -f -n 12 -b 5 -i -m mongo2
        mongo_perf.py -c mongo -d config -S -o /data/perf_file.txt -a -n 5

":"""
# Python program follows


# Libraries and Global Variables

# Standard
import sys
import subprocess
import ast

try:
    import simplejson as json
except ImportError:
    import json

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .mongo_lib import mongo_libs
    from .mongo_lib import mongo_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import mongo_lib.mongo_libs as mongo_libs           # pylint:disable=R0402
    import mongo_lib.mongo_class as mongo_class         # pylint:disable=R0402
    import version

__version__ = version.__version__

# Global


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def get_data(cmd):

    """Function:  get_data

    Description:  Opens a system call to run the program command.

    Arguments:
        (input) cmd -> List array holding program command line
        (output) out -> Results of program command

    """

    cmd = list(cmd)
    proc1 = subprocess.Popen(                           # pylint:disable=R1732
        cmd, stdout=subprocess.PIPE)
    out, _ = proc1.communicate()

    return out


def mongo_stat(server, args, **kwargs):                 # pylint:disable=R0914

    """Function:  mongo_stat

    Description:  Creates and executes the mongostat utility program.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            req_arg -> List of options to add to cmd line
            opt_arg -> Dictionary of additional options to add
            ofile -> file name - Name of output file
            db_tbl database:table_name -> Mongo database and table name
            class_cfg -> Mongo server configuration

    """

    mail = None
    mail_body = []
    mode = "w"
    indent = 4
    outfile = kwargs.get("ofile", None)
    no_std = args.arg_exist("-z")
    cmd = mongo_libs.create_cmd(server, args, "mongostat", "-p", **kwargs)

    if args.arg_exist("-a"):
        mode = "a"

    if args.arg_exist("-f"):
        indent = None

    if args.arg_exist("-b"):
        cmd.append(args.get_val("-b"))

    if args.arg_exist("-t"):
        mail = gen_class.setup_mail(
            args.get_val("-t"),
            subj=args.get_val("-s", def_val="Mongodb_Performance"))

    data = get_data(cmd)
    data = data.decode()

    for row in data.rstrip().split("\n"):
        # Evaluate "row" to dict format.
        _, value = ast.literal_eval(row).popitem()
        time = value["time"]
        value = gen_libs.rm_key(value, "time")
        data = {
            "Server": server.name,
            "AsOf": gen_libs.get_date() + " " + time, "PerfStats": value}

        if hasattr(value, "set") and hasattr(value, "repl"):
            rep_set = value["set"]
            rep_state = value["repl"]
            value = gen_libs.rm_key(value, "set")
            value = gen_libs.rm_key(value, "repl")
            data["RepSet"] = rep_set
            data["RepState"] = rep_state

        mail_body.append(data)
        process_json(data, outfile, indent, no_std, mode, **kwargs)

        # Append to file after first loop.
        mode = "a"

    if mail:
        for line in mail_body:
            mail.add_2_msg(json.dumps(line, indent=indent))

        mail.send_mail(use_mailx=args.arg_exist("-u"))


def process_json(data, outfile, indent, no_std, mode, **kwargs):

    """Function:  process_json

    Description:  Process JSON data.

    Arguments:
        (input) data -> Dictionary of Mongo performance stat
        (input) outfile -> Name of output file
        (input) indent -> Indentation setting for JSON format
        (input) no_std -> Suppress standard out
        (input) mode -> File write mode (append|write)
        (input) **kwargs:
            db_tbl -> Mongo database and table name
            class_cfg -> Mongo server configuration

    """

    data = dict(data)

    if kwargs.get("db_tbl", False) and kwargs.get("class_cfg", False):
        dbn, tbl = kwargs.get("db_tbl").split(":")
        status = mongo_libs.ins_doc(kwargs.get("class_cfg"), dbn, tbl, data)

        if not status[0]:
            print(f"Insert error:  {status[1]}")

    if outfile:
        gen_libs.write_file(outfile, mode, json.dumps(data, indent=indent))

    if not no_std:
        gen_libs.print_data(json.dumps(data, indent=indent))


def run_program(args, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options
        (input) **kwargs:
            req_arg -> List of options to add to cmd line
            opt_arg -> Dictionary of additional options to add

    """

    authdb = "--authenticationDatabase="
    func_dict = dict(func_dict)
    outfile = args.get_val("-o", def_val=False)
    db_tbl = args.get_val("-i", def_val=False)
    cfg = None
    server = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
    req_arg = list(kwargs.get("req_arg", []))
    opt_arg = dict(kwargs.get("opt_arg", {}))

    if authdb in req_arg:
        req_arg.remove(authdb)
        req_arg.append(authdb + server.auth_db)

    if args.arg_exist("-m"):
        cfg = gen_libs.load_module(args.get_val("-m"), args.get_val("-d"))

    if server.repset and server.repset_hosts:
        config = mongo_libs.create_security_config(cfg=server)
        mongo = mongo_class.RepSet(
            server.name, server.user, server.japd, host=server.host,
            port=server.port, auth=server.auth, repset=server.repset,
            repset_hosts=server.repset_hosts, **config)

    else:
        mongo = mongo_libs.create_instance(
            args.get_val("-c"), args.get_val("-d"), mongo_class.Server)

    status = mongo.connect()

    if status[0]:
        # Call function(s) - intersection of command line and function dict.
        for item in set(args.get_args_keys()) & set(func_dict.keys()):
            func_dict[item](
                mongo, args, ofile=outfile, db_tbl=db_tbl, class_cfg=cfg,
                req_arg=req_arg, opt_arg=opt_arg)

        mongo_libs.disconnect([mongo])

    else:
        if not args.arg_exist("-w"):
            print(f"run_program: Connection failure:  {status[1]}")


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains directories and their octal permissions
        file_perm_chk -> file check options with their perms in octal
        file_crt -> contains options which require files to be created
        func_dict -> dictionary list for the function calls or other options
        opt_arg_list -> contains optional arguments for the command line
        opt_con_req_list -> contains the options that require other options
        opt_def_dict -> contains options with their default values
        opt_def_dict2 -> default values for "-S" option
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains the options that are required for the program
        opt_val_list -> contains options which require values
        req_arg_list -> contains arguments to add to command line by default

    Arguments:
        (input) argv -> Arguments from the command line

    """

    dir_perms_chk = {"-d": 5, "-p": 5}
    file_perm_chk = {"-o": 6}
    file_crt = ["-o"]
    func_dict = {"-S": mongo_stat}
    opt_arg_list = {"-n": "-n=", "-r": "--tlsInsecure"}
    opt_con_req_list = {"-i": ["-m"], "-s": ["-t"], "-u": ["-t"]}
    opt_def_dict = {"-i": "sysmon:mongo_perf", "-n": "1", "-b": "1"}
    opt_def_dict2 = {"-n": "1", "-b": "1"}
    opt_multi_list = ["-s", "-t"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-b", "-i", "-m", "-n", "-o", "-p", "-s", "-t"]
    req_arg_list = ["--authenticationDatabase=", "--json"]

    # Process argument list from command line.
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, opt_def=opt_def_dict,
        multi_val=opt_multi_list, do_parse=True)

    # Add default arguments for certain argument combinations.
    if args.arg_exist("-S"):
        args.arg_add_def(defaults=opt_def_dict2)

    if not gen_libs.help_func(args, __version__, help_message)              \
       and args.arg_require(opt_req=opt_req_list)                           \
       and args.arg_cond_req(opt_con_req=opt_con_req_list)                  \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)                    \
       and args.arg_file_chk(file_perm_chk=file_perm_chk, file_crt=file_crt):

        try:
            proglock = gen_class.ProgramLock(
                sys.argv, args.get_val("-y", def_val=""))
            run_program(
                args, func_dict, req_arg=req_arg_list, opt_arg=opt_arg_list)
            del proglock

        except gen_class.SingleInstanceException:
            print(f'WARNING:  lock in place for mongo_perf with id of:'
                  f'{args.get_val("-y", def_val="")}')


if __name__ == "__main__":
    sys.exit(main())
