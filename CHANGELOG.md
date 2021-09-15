# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


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

