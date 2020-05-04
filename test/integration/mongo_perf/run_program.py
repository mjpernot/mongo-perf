#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Integration testing of run_program in mongo_perf.py.

    Usage:
        test/integration/mongo_perf/run_program.py

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
        self.user = "mongo"
        self.passwd = None
        self.host = "hostname"
        self.port = 27017
        self.auth = False
        self.repset = None

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_email -> Test with email option.
        test_replica_set -> Test connecting to Mongo replica set.
        test_mongo -> Test with mongo option.
        test_flatten_json -> Test option to flatten JSON data structure.
        test_append_file -> Test option to append to file.
        test_write_file -> Test option to write to file.
        test_json -> Test with JSON option.
        test_default_args_array -> Test with default options.
        tearDown -> Clean up of testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.config = "mongo"
        self.config2 = "mongo2"
        self.path = "./test/integration/mongo_perf/baseline"
        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"
        self.outfile = os.path.join(self.path, "mongo_stat_outfile.txt")
        self.outfile2 = os.path.join(self.path, "mongo_stat_outfile2.txt")
        self.outfile3 = os.path.join(self.path, "mongo_stat_outfile3.txt")
        self.req_arg_list = ["--authenticationDatabase=admin"]
        self.opt_arg_list = {"-j": "--json", "-n": "-n="}
        self.func_dict = {"-S": mongo_perf.mongo_stat}
        self.args_array = {"-c": self.config, "-d": self.path, "-S": True}
        self.args_array2 = {"-c": self.config, "-d": self.path, "-S": True,
                            "-j": True}
        self.args_array3 = {"-c": self.config, "-d": self.path, "-S": True,
                            "-j": True, "-o": self.ofile}
        self.args_array4 = {"-c": self.config, "-d": self.path, "-S": True,
                            "-j": True, "-o": self.ofile, "-a": True}
        self.args_array5 = {"-c": self.config, "-d": self.path, "-S": True,
                            "-j": True, "-o": self.ofile, "-f": True}
        self.args_array6 = {"-c": self.config, "-d": self.path, "-S": True,
                            "-m": self.config}
        self.args_array7 = {"-c": self.config2, "-d": self.path, "-S": True}
        self.results = \
            "{1:{1: 11, 'time': 'timestamp'}, 2: {2: 22, 'time': 'timestamp'}}"

    @unittest.skip("not yet implemented")
    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_email(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg, True]
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(self.args_array2,
                                                self.func_dict))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.mongo_class.RepSet")
    def test_replica_set(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_replica_set

        Description:  Test connecting to Mongo replica set.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(
            self.args_array7, self.func_dict, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_mongo(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_mongo

        Description:  Test with mongo option.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(
            self.args_array6, self.func_dict, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_flatten_json(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        mongo_perf.run_program(
            self.args_array5, self.func_dict, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list)

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_append_file(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        mongo_perf.run_program(
            self.args_array4, self.func_dict, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list)
        mongo_perf.run_program(
            self.args_array4, self.func_dict, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list)

        self.assertTrue(filecmp.cmp(self.outfile2, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_write_file(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_write_file

        Description:  Test option to write to file.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        mongo_perf.run_program(
            self.args_array3, self.func_dict, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list)

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_json(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_json

        Description:  Test with JSON option.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.run_program(
                self.args_array2, self.func_dict, req_arg=self.req_arg_list,
                opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.cmds_gen.run_prog", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_default_args_array(self, mock_inst, mock_disconn):

        """Function:  test_default_args_array

        Description:  Test with default options.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(
            self.args_array, self.func_dict, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
