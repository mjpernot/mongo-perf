# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


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
- mongo_stat:  Fixed problem with mutable default arguments issue.
- run_program:  Fixed problem with mutable default arguments issue.

### Changed
- mongo_stat:  Replaced "mongo_libs.json_2_out" with own internal code.
- main:  Refactored "if" statements.
- mongo_stat:  Converted JSON to CamelCase format.
- mongo_stat:  Changed variable name to standard naming convention.
- run_program:  Changed variable name to standard naming convention.


## [2.0.1] - 2018-11-28
### Changed
- run_program:  Changed "MONGO_SVR" to "cfg" to reflect usage.


## [2.0.0] - 2018-04-20
Breaking Change

### Changed
- Changed function names from uppercase to lowercase.
- Changed "mongo_libs" calls to new naming schema.
- Changed "cmds_gen" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
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

