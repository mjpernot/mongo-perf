# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.1.0] - 2019-09-06
### Fixed
- mongo_stat:  Fixed problem with mutable default arguments issue.
- run_program:  Fixed problem with mutable default arguments issue.


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

