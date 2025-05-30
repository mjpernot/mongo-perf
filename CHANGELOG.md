# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.1.2] - 2025-05-20
- Updated to work with pymongo v4.X
- Updated python-lib to v4.0.1
- Updated mongo-lib to v4.5.2

### Changes
- Documentation changes.


## [3.1.1] - 2025-03-11
- Added support for Mongo 7.0
- Updated mongo-libs to v4.5.1

### Fixed
- Fixed pre-header where to determine which python version to use.

### Removed
- Mongo 3.4 support.


## [3.1.0] - 2025-02-07
- Added capability to connect directly to single server in replica set.
- Updated mongo-lib v4.5.0

### Changed
- Added direct_connect to config/mongo.py configuration file.
- Documentation changes.

### Removed
- Mongo 3.4 support.


## [3.0.0] - 2025-01-31
Breaking Changes

- Removed support for Python 2.7.
- Removing non-json output - all output will now be in JSON format by default.
- Add pre-header check on allowable Python versions to run.
- Added pymongo==4.10.1 for Python 3.9 and Python 3.12.
- Added dnspython==2.7.0 for Python 3.9 and Python 3.12.
- Updated python-lib v4.0.0
- Updated mongo-lib v4.4.0

### Added
- process_json: Process JSON data.

### Changed
- main: Removed "-j" option and added "--json" as a default argument to the command.
- mongo_stat: Removed non-json output and removed "-j" option.
- mongo_stat: Replaced \_process_json call with process_json call.
- Converted strings to f-strings.
- Documentation changes.

### Deprecated
- Support for Mongo 3.4

### Removed
- \_process_json function.


## [2.4.9] - 2024-11-20
- Updated distro==1.9.0 for Python 3
- Updated psutil==5.9.4 for Python 3
- Updated python-lib to v3.0.8
- Updated mongo-lib to v4.3.4

### Deprecated
- Support for Python 2.7


## [2.4.8] - 2024-09-27
- Updated python-lib to v3.0.5


## [2.4.7] - 2024-09-25
- Set pymongo to 4.1.1 for Python 3.6.
- Set simplejson to 3.13.2 for Python 3.
- Updated mongo-lib to v4.3.2
- Updated python-lib to v3.0.4

### Changed
- run_program: Called mongo_libs.create_security_config to replace passing TLS/SSL manually.


## [2.4.6] - 2024-09-10
- Minor changes.


## [2.4.5] - 2024-04-22
- Updated mongo-lib to v4.3.0
- Added TLS capability
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- run_program: Added TLS parameters to database instance call.
- Set pymongo to 3.12.3 for Python 2 and Python 3.
- config/mongo.py.TEMPLATE: Added TLS entries.
- Documentation updates.


## [2.4.4] - 2024-03-22
### Fixed
- mongo_stat: Decoded data from get_data() call if Python 3.

### Changed
- mongo_stat: Add in replication items to JSON if part of a replica set.


## [2.4.3] - 2024-02-26
- Updated to work in Red Hat 8
- Updated mongo-lib to v4.2.9
- Updated python-lib to v3.0.3

### Fixed
- main:  Changed the -p option in the dir_perm_chk variable to an octal 5.

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [2.4.2] - 2023-10-11
- Upgraded mongo-lib to v4.2.7 to fix an error in the create_cmd call.


## [2.4.1] - 2023-10-04
- Upgraded mongo-lib to v4.2.6


## [2.4.0] - 2023-09-07
- Upgraded python-lib to v2.10.1
- Upgraded mongo-lib to v4.2.5
- Replaced the arg_parser code with gen_class.ArgParser code.

### Changed
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main: Removed gen_libs.get_inst call.


## [2.3.3] - 2023-06-05
- Added -r option to turn off TLS checking if using SSL.

### Fixed
- main: Added "-r" option to the opt_arg_list list.


## [2.3.2] - 2022-11-30
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded mongo-lib to v4.2.2
 
### Fixed:
- run_program: Added SSL entries to the mongo_class instance calls and removed the use_arg and use_uri arguments.

### Changed
- run_program: Made auth_mech a required parameter, cannot be passed as an empty argument anymore.
- Converted imports to use Python 2.7 or Python 3.
- main: Converted dictionary keys() call to list.
- mongo_stat: Replaced open() with io.open() call.


## [2.3.1] - 2022-06-28
- Upgrade mongo-libs to v4.2.1
- Upgrade python-lib to v2.9.2

### Changed
- config/mongo.py.TEMPLATE: Removed old entries.
- Documentation updates.


## [2.3.0] - 2020-07-21
- Updated to use pymongo v3.8.0.
- Updated to be used in FIPS 140-2 environment.
- Updated to work in Mongo 4.2.14 environment.
- Updated to work in a SSL environment.

### Fixed
- mongo_stat:  Fixed problem with mutable default arguments issue, add append mode to writing to file for standard out and fixed writing to file and inserting into a Mongo database at the same time.
- main:  Refactored "Add default arguments for certain argument combinations" section to ensure "-n" is added, added "-s" and "-t" to the opt_val_list which require the option to be passed with value(s) and added "-s" and "-t" to the opt_con_req_list variable to require "-t" if "-s" is used and set "-j" option if "-i" option selected.
- run_program:  Allow authentication database to be set from configuration file instead of being hardcoded.

### Added
- Added -w option to suppress printing the inital connection error.
- Added email capability with the -t, -u, and -s options.
- Added -y option for adding flavor id for program lock.
- Added -z option for standard out suppression.
- get_data:  Opens a system call to run the program command.
- \_process_json:  Private function for mongo_stat to process JSON data.

### Changed
- mongo_stat:  Removed "time" key from the "PerfStats" dictionary, replaced cmds_gen.run_prog with get_data call, replaced rm_key with gen_libs.rm_key call, replaced cmds_gen.run_prog with Popen calls for writing to standard out, writing to file and added email capability for JSON formatted reports and replaced section of code with call to private function \_process_json, add standard out suppression option and reformatted performance stats dictionary, moved "set" and "repl" up one level in dictionary.
- run_program:  Process status of mongo connection call, replaced cmds_gen.disconnect with mongo_libs.disconnect call, added authorization mechanism to the mongo_class.RepSet class instance call, added check for -w option to ignore initial connection error and added new args to mongo_class creation instance, updated to refect update in configuration file and changed variable name to standard naming convention and added repset_hosts to mongo_class.RepSet instance call.
- main:  Added -t and -s options and multiple value options check and added gen_class.ProgamLock code for locking of program run.
- config/mongo.py.TEMPLATE:  Added three new configuration entries and SSL connection entries and update a configuration entry.
- Documentation updates.

### Removed
- rm_key function.
- cmds_gen module.


## [2.2.0] - 2020-04-08
### Added
- Added "-f" option to allow the flattening of the JSON data structure to file and standard out.
- Added "-a" option to allow for appending of data to existing output file.

### Fixed
- mongo_stat:  Fixed multiline output from command will not overwrite previous entry in file.
- main:  Fixed handling command line arguments from SonarQube scan finding.
- main:  Added "-n" argument for "-S" and "-j" argument combination.

### Changed
- run_program:  Added ability to connect to Mongo replica set based on configuration settings.
- run_program:  Changed "server" to "mongo" to be standardized naming convention.
- mongo_stat:  Added -f option to set the indentation setting for the JSON structure.
- mongo_stat:  Changed "key" variable to throwaway variable "\_".
- mongo_stat:  Added -a option to set the file mode for writing to out file.
- mongo_stat:  Restructured the JSON document so as to be used for Filebeat.
- Documentation updates.


## [2.1.0] - 2019-09-10
### Fixed
- main:  Removed duplicate code:  arg_parser.arg_cond_req check.
- run_program, mongo_stat:  Fixed problem with mutable default arguments issue.

### Changed
- mongo_stat:  Replaced "mongo_libs.json_2_out" with own internal code.
- main:  Refactored "if" statements.
- mongo_stat:  Converted JSON to PascalCase format.
- run_program, mongo_stat:  Changed variable name to standard naming convention.


## [2.0.1] - 2018-11-28
### Changed
- run_program:  Changed "MONGO_SVR" to "cfg" to reflect usage.


## [2.0.0] - 2018-04-20
Breaking Change

### Changed
- Changed function names from uppercase to lowercase.
- Changed "mongo_libs", "cmds_gen", "gen_libs", and "arg_parser" calls to new naming schema.
- Setup single-source version control.


## [1.5.0] - 2018-04-20
### Added
- Changed "svr_mongo" to "mongo_class" module reference.
- Changed "cmds_mongo" to "mongo_libs" module reference.
- Added single-source version control.


## [1.4.0] - 2017-08-17
### Changed
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.
- Change single quotes to double quotes.
- Convert program to use local libraries from ./lib directory.


## [1.3.0] - 2017-01-20
### Changed
- Mongo_Stat:  Changed prog_gen to cmds_gen.  Changed mongo_prog to cmds_mongo.
- Help_Message:  Updated documentation.


## [1.2.0] - 2016-05-13
### Changed
- Mongo_Stat:  Added date to "value" dictionary as mongostat --json only provides a time and not a date.

### Added
- Import of datetime module.


## [1.1.0] - 2016-05-12
### Changed
- Mongo_Stat:  Removed the first key from the dictionary and passed the value of the key (another dictionary) to output.  The key was not required and contained duplicate data.


## [1.0.0] - 2016-05-10
- Initial creation.

