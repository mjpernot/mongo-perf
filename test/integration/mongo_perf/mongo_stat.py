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
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "ServerName"
        self.host = "Hostname"
        self.port = 27017
        self.japd = None
        self.auth = False
        self.auth_db = "admin"
        self.use_arg = True
        self.use_uri = False
        self.config = {"authMechanism": "SCRAM-SHA-1"}


class SubProcess(object):

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        wait

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

        pass

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_insert_fail
        test_insert_success
        test_no_suppress
        test_suppress
        test_json
        test_flatten_json
        test_append_file
        test_write_file
        test_mongo
        test_dict_format
        test_polling
        test_std_out_file
        test_default_args_array
        test_empty_args_array
        tearDown

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
        self.subproc = SubProcess()
        self.args_array = {"-c": "mongo", "-d": "config", "-S": True,
                           "-z": True}
        self.args_array2 = {"-c": "mongo", "-d": "config", "-S": True,
                            "-j": True, "-z": True}
        self.args_array3 = {"-c": "mongo", "-d": "config", "-S": True,
                            "-j": True, "-a": True, "-z": True}
        self.args_array4 = {"-c": "mongo", "-d": "config", "-S": True,
                            "-j": True, "-f": True, "-z": True}
        self.args_array5 = {"-c": "mongo", "-d": "config", "-S": True, "-b": 1,
                            "-z": True}
        self.args_array6 = {"-c": "mongo", "-d": "config", "-S": True,
                            "-j": True}
        self.db_tbl = "database:table"
        self.class_cfg = "mongo_config"
        self.results = \
            "{1:{1: 11, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}, \
            2: {2: 22, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}}"
        self.setdate = "2020-04-29"

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    def test_insert_fail(self, mock_mongo, mock_cmds):

        """Function:  test_insert_fail

        Description:  Test with failed insert into Mongo.

        Arguments:

        """

        mock_mongo.return_value = (False, "Insert Failed")
        mock_cmds.return_value = self.results

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.mongo_stat(
                self.server, self.args_array2, db_tbl=self.db_tbl,
                class_cfg=self.class_cfg, req_arg=self.req_arg))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    def test_insert_success(self, mock_mongo, mock_cmds):

        """Function:  test_insert_success

        Description:  Test with successful insert into Mongo.

        Arguments:

        """

        mock_mongo.return_value = (True, None)
        mock_cmds.return_value = self.results

        self.assertFalse(mongo_perf.mongo_stat(
            self.server, self.args_array2, db_tbl=self.db_tbl,
            class_cfg=self.class_cfg, req_arg=self.req_arg))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    def test_no_suppress(self, mock_cmds, mock_date):

        """Function:  test_no_suppress

        Description:  Test option to standard JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_date.return_value = self.setdate

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.mongo_stat(
                self.server, self.args_array6, req_arg=self.req_arg))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    def test_suppress(self, mock_cmds, mock_date):

        """Function:  test_suppress

        Description:  Test option to standard JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_date.return_value = self.setdate

        self.assertFalse(mongo_perf.mongo_stat(
            self.server, self.args_array2, req_arg=self.req_arg))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    def test_json(self, mock_cmds, mock_date):

        """Function:  test_json

        Description:  Test option to standard JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_date.return_value = self.setdate

        mongo_perf.mongo_stat(
            self.server, self.args_array2, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    def test_flatten_json(self, mock_cmds, mock_date):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_date.return_value = self.setdate

        mongo_perf.mongo_stat(
            self.server, self.args_array4, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    def test_append_file(self, mock_cmds, mock_date):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_date.return_value = self.setdate

        mongo_perf.mongo_stat(
            self.server, self.args_array3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)
        mongo_perf.mongo_stat(
            self.server, self.args_array3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile2, self.ofile))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    def test_write_file(self, mock_cmds, mock_date):

        """Function:  test_write_file

        Description:  Test option to write to file.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_date.return_value = self.setdate

        mongo_perf.mongo_stat(
            self.server, self.args_array3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    def test_mongo(self, mock_mongo, mock_cmds):

        """Function:  test_mongo

        Description:  Test with sending data to mongo.

        Arguments:

        """

        mock_mongo.return_value = (True, None)
        mock_cmds.return_value = self.results

        self.assertFalse(mongo_perf.mongo_stat(
            self.server, self.args_array2, db_tbl=self.db_tbl,
            class_cfg=self.class_cfg, req_arg=self.req_arg))

    @mock.patch("mongo_perf.get_data")
    def test_dict_format(self, mock_cmds):

        """Function:  test_dict_format

        Description:  Test with converting output data to dictionary.

        Arguments:

        """

        mock_cmds.return_value = self.results

        self.assertFalse(mongo_perf.mongo_stat(
            self.server, self.args_array2, req_arg=self.req_arg))

    @mock.patch("mongo_perf.subprocess.Popen")
    def test_polling(self, mock_popen):

        """Function:  test_polling

        Description:  Test with polling option.

        Arguments:

        """

        mock_popen.return_value = self.subproc

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array5,
                                               req_arg=self.req_arg))

    @mock.patch("mongo_perf.subprocess.Popen")
    def test_std_out_file(self, mock_popen):

        """Function:  test_std_out_file

        Description:  Test with standard out to file.

        Arguments:

        """

        mock_popen.return_value = self.subproc

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args_array, req_arg=self.req_arg,
                ofile=self.ofile))

    @mock.patch("mongo_perf.subprocess.Popen")
    def test_default_args_array(self, mock_popen):

        """Function:  test_default_args_array

        Description:  Test with default options.

        Arguments:

        """

        mock_popen.return_value = self.subproc

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array,
                                               req_arg=self.req_arg))

    @mock.patch("mongo_perf.subprocess.Popen")
    def test_empty_args_array(self, mock_popen):

        """Function:  test_empty_args_array

        Description:  Test with empty args_array.

        Arguments:

        """

        mock_popen.return_value = self.subproc

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
