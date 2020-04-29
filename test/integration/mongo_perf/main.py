#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in mongo_perf.py.

    Usage:
        test/integration/mongo_perf/main.py

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

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_help_true -> Test help if returns true.
        test_help_false -> Test help if returns false.
        test_arg_req_true -> Test arg_require if returns true.
        test_arg_req_false -> Test arg_require if returns false.
        test_arg_cond_false -> Test arg_cond_req if returns false.
        test_arg_cond_true -> Test arg_cond_req if returns true.
        test_arg_dir_true -> Test arg_dir_chk_crt if returns true.
        test_arg_dir_false -> Test arg_dir_chk_crt if returns false.
        test_arg_file_true -> Test arg_file_chk if returns true.
        test_arg_file_false -> Test arg_file_chk if returns false.
        test_set_default_args -> Test setting default arguments.
        test_default_args_array -> Test with default options.
        test_json -> Test with JSON option.
        test_write_file -> Test option to write to file.
        test_append_file -> Test option to append to file.
        test_flatten_json -> Test option to flatten JSON data structure.
        test_mongo -> Test with mongo option.
        test_replica_set -> Test connecting to Mongo replica set.
        tearDown -> Clean up of testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CmdLine(object):

            """Class:  CmdLine

            Description:  Class which is a representation of a command line.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """
                self.cpath = "./test/integration/mongo_perf/baseline"
                self.argv = ["./mongo_perf.py", "-c", "mongo", "-d",
                             self.cpath, "-S"]

        self.cmdline = CmdLine()
        self.server = Server()
        self.config = "mongo"
        self.config2 = "mongo2"
        self.path = "./test/integration/mongo_perf/baseline"
        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"
        self.outfile = os.path.join(self.path, "mongo_stat_outfile.txt")
        self.outfile2 = os.path.join(self.path, "mongo_stat_outfile2.txt")
        self.outfile3 = os.path.join(self.path, "mongo_stat_outfile3.txt")
        self.results = \
            "{1:{1: 11, 'time': 'timestamp'}, 2: {2: 22, 'time': 'timestamp'}}"

    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_help_true(self, mock_cmdline):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        self.cmdline.argv.append("-h")
        mock_cmdline.return_value = self.cmdline

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_require")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_help_false(self, mock_cmdline, mock_req):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_req.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_require")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_arg_req_true(self, mock_cmdline, mock_req):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_req.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_cond_req")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_arg_req_false(self, mock_cmdline, mock_cond):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_cond.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_cond_req")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_arg_cond_false(self, mock_cmdline, mock_cond):

        """Function:  test_arg_cond_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_cond.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_dir_chk_crt")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_arg_cond_true(self, mock_cmdline, mock_dir):

        """Function:  test_arg_cond_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_dir.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_dir_chk_crt")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_arg_dir_true(self, mock_cmdline, mock_dir):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_dir.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_file_chk")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_arg_dir_false(self, mock_cmdline, mock_arg):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_arg.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_file_chk")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_arg_file_true(self, mock_cmdline, mock_arg):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_arg.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_arg_file_false(self, mock_cmdline, mock_run):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_run.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_set_default_args(self, mock_cmdline, mock_run):

        """Function:  test_set_default_args

        Description:  Test setting default arguments.

        Arguments:

        """

        self.cmdline.argv.append("-j")
        mock_cmdline.return_value = self.cmdline
        mock_run.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.cmds_gen.run_prog", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_default_args_array(self, mock_cmdline, mock_inst):

        """Function:  test_default_args_array

        Description:  Test with default options.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_json(self, mock_cmdline, mock_inst, mock_cmds):

        """Function:  test_json

        Description:  Test with JSON option.

        Arguments:

        """

        self.cmdline.argv.append("-j")
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_write_file(self, mock_cmdline, mock_inst, mock_cmds):

        """Function:  test_write_file

        Description:  Test option to write to file.

        Arguments:

        """

        self.cmdline.argv.append("-j")
        self.cmdline.argv.append("-o")
        self.cmdline.argv.append(self.ofile)
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline

        mongo_perf.main()

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_append_file(self, mock_cmdline, mock_inst, mock_cmds):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        self.cmdline.argv.append("-j")
        self.cmdline.argv.append("-a")
        self.cmdline.argv.append("-o")
        self.cmdline.argv.append(self.ofile)
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline

        mongo_perf.main()
        mongo_perf.main()

        self.assertTrue(filecmp.cmp(self.outfile2, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_flatten_json(self, mock_cmdline, mock_inst, mock_cmds):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        self.cmdline.argv.append("-j")
        self.cmdline.argv.append("-f")
        self.cmdline.argv.append("-o")
        self.cmdline.argv.append(self.ofile)
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline

        mongo_perf.main()

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_mongo(self, mock_cmdline, mock_inst, mock_cmds):

        """Function:  test_mongo

        Description:  Test with mongo option.

        Arguments:

        """

        self.cmdline.argv.append("-j")
        self.cmdline.argv.append("-f")
        self.cmdline.argv.append("-o")
        self.cmdline.argv.append(self.ofile)
        self.cmdline.argv.append("-m")
        self.cmdline.argv.append(self.config)
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline

        mongo_perf.main()

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile))

    @mock.patch("mongo_perf.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_replica_set(self, mock_cmdline, mock_inst, mock_cmds):

        """Function:  test_replica_set

        Description:  Test connecting to Mongo replica set.

        Arguments:

        """

        self.cmdline.argv.append("-j")
        self.cmdline.argv.append("-f")
        self.cmdline.argv.append("-o")
        self.cmdline.argv.append(self.ofile)
        self.cmdline.argv.append("-m")
        self.cmdline.argv.append(self.config2)
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline

        mongo_perf.main()

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
