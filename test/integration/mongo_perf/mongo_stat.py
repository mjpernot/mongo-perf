#!/usr/bin/python
# Classification (U)

"""Program:  mongo_stat.py

    Description:  Integration testing of mongo_stat in mongo_perf.py.

    Usage:
        test/intergration/mysql_db_admin/mongo_stat.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import filecmp

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_perf
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"
        self.host = "Hostname"
        self.port = 27017
        self.passwd = None
        self.auth = False


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_json -> Test option to standard JSON data structure.
        test_flatten_json -> Test option to flatten JSON data structure.
        test_append_file -> Test option to append to file.
        test_write_file -> Test option to write to file.
        test_mongo -> Test with sending data to mongo.
        test_dict_format -> Test with converting output data to dictionary.
        test_polling -> Test with polling option.
        test_default_args_array -> Test with default options.
        test_empty_args_array -> Test with empty args_array.
        tearDown -> Clean up of testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.req_arg = ["--authenticationDatabase=admin"]
        self.basepath = "./test/integration/mongo_perf/baseline"
        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"
        self.outfile = os.path.join(self.basepath, "mongo_stat_outfile.txt")
        self.outfile2 = os.path.join(self.basepath, "mongo_stat_outfile2.txt")
        self.outfile3 = os.path.join(self.basepath, "mongo_stat_outfile3.txt")
        self.server = Server()
        self.args_array = {"-c": "mongo", "-d": "config", "-S": True}
        self.args_array2 = {"-c": "mongo", "-d": "config", "-S": True,
                            "-j": True}
        self.args_array3 = {"-c": "mongo", "-d": "config", "-S": True,
                            "-j": True, "-a": True}
        self.args_array4 = {"-c": "mongo", "-d": "config", "-S": True,
                            "-j": True, "-f": True}
        self.args_array5 = {"-c": "mongo", "-d": "config", "-S": True, "-b": 1}
        self.db_tbl = "database:table"
        self.class_cfg = "mongo_config"
        self.results = \
            "{1:{1: 11, 'time': 'timestamp'}, 2: {2: 22, 'time': 'timestamp'}}"

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    def test_json(self, mock_cmds):

        """Function:  test_json

        Description:  Test option to standard JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results

        mongo_perf.mongo_stat(
            self.server, self.args_array2, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    def test_flatten_json(self, mock_cmds):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results

        mongo_perf.mongo_stat(
            self.server, self.args_array4, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    def test_append_file(self, mock_cmds):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        mock_cmds.return_value = self.results

        mongo_perf.mongo_stat(
            self.server, self.args_array3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)
        mongo_perf.mongo_stat(
            self.server, self.args_array3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile2, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    def test_write_file(self, mock_cmds):

        """Function:  test_write_file

        Description:  Test option to write to file.

        Arguments:

        """

        mock_cmds.return_value = self.results

        mongo_perf.mongo_stat(
            self.server, self.args_array3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    def test_mongo(self, mock_mongo, mock_cmds):

        """Function:  test_mongo

        Description:  Test with sending data to mongo.

        Arguments:

        """

        mock_mongo.return_value = True
        mock_cmds.return_value = self.results

        self.assertFalse(mongo_perf.mongo_stat(
            self.server, self.args_array2, db_tbl=self.db_tbl,
            class_cfg=self.class_cfg, req_arg=self.req_arg))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    def test_dict_format(self, mock_cmds):

        """Function:  test_dict_format

        Description:  Test with converting output data to dictionary.

        Arguments:

        """

        mock_cmds.return_value = self.results

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.mongo_stat(
                self.server, self.args_array2, req_arg=self.req_arg))

    @mock.patch("mongo_perf.cmds_gen.run_prog", mock.Mock(return_value=True))
    def test_polling(self):

        """Function:  test_polling

        Description:  Test with polling option.

        Arguments:

        """

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array5,
                                               req_arg=self.req_arg))

    @mock.patch("mongo_perf.cmds_gen.run_prog", mock.Mock(return_value=True))
    def test_default_args_array(self):

        """Function:  test_default_args_array

        Description:  Test with default options.

        Arguments:

        """

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array,
                                               req_arg=self.req_arg))

    @mock.patch("mongo_perf.cmds_gen.run_prog", mock.Mock(return_value=True))
    def test_empty_args_array(self):

        """Function:  test_empty_args_array

        Description:  Test with empty args_array.

        Arguments:

        """

        self.assertFalse(mongo_perf.mongo_stat(self.server, {},
                                               req_arg=self.req_arg))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
