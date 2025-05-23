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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_perf                               # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_help_true
        test_set_default_args
        test_default_args_array
        test_write_file
        test_append_file
        test_flatten_json
        test_suppress
        test_no_suppress
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        config = "test/integration/config"
        self.argv_list = ["mongo_perf.py", "-c", "mongo", "-d", config, "-S"]
        self.argv_list2 = list(self.argv_list)
        self.argv_list2.append("-f")
        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"

#        self.db_tbl = "dbname:tblname"
#        self.cmdline = CmdLine()
#        self.server = Server()
#        self.subproc = SubProcess()
#        self.config = "mongo"
#        self.config2 = "mongo2"
#        self.path = "./test/integration/mongo_perf/baseline"
#        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"
#        self.outfile = os.path.join(self.path, "mongo_stat_outfile.txt")
#        self.outfile2 = os.path.join(self.path, "mongo_stat_outfile2.txt")
#        self.outfile3 = os.path.join(self.path, "mongo_stat_outfile3.txt")
#        self.results = \
#            "{1:{1: 11, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}, \
#            2: {2: 22, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}}"
#        self.setdate = "2020-04-29"
#        self.argv = ["./mongo_perf.py", "-c", "mongo", "-d", self.path, "-S",
#                     "-z"]

    @unittest.skip("Skipping for now")
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

    @unittest.skip("Skipping for now")
    @mock.patch("mongo_perf.run_program")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_set_default_args(self, mock_cmdline, mock_run):

        """Function:  test_set_default_args

        Description:  Test setting default arguments.

        Arguments:

        """

        mock_cmdline.return_value = self.cmdline
        mock_run.return_value = True

        self.assertFalse(mongo_perf.main())

    @unittest.skip("Skipping for now")
    @mock.patch("mongo_perf.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_write_file(self, mock_cmdline, mock_inst, mock_cmds, mock_date):

        """Function:  test_write_file

        Description:  Test option to write to file.

        Arguments:

        """

        self.cmdline.argv.append("-o")
        self.cmdline.argv.append(self.ofile)
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline
        mock_date.return_value = self.setdate

        mongo_perf.main()

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile))

    @unittest.skip("Skipping for now")
    @mock.patch("mongo_perf.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_append_file(self, mock_cmdline, mock_inst, mock_cmds, mock_date):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        self.cmdline.argv.append("-a")
        self.cmdline.argv.append("-o")
        self.cmdline.argv.append(self.ofile)
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline
        mock_date.return_value = self.setdate

        mongo_perf.main()
        mongo_perf.main()

        self.assertTrue(filecmp.cmp(self.outfile2, self.ofile))

    @unittest.skip("Skipping for now")
    @mock.patch("mongo_perf.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    @mock.patch("mongo_perf.gen_libs.get_inst")
    def test_flatten_json(self, mock_cmdline, mock_inst, mock_cmds, mock_date):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        self.cmdline.argv.append("-f")
        self.cmdline.argv.append("-o")
        self.cmdline.argv.append(self.ofile)
        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_cmdline.return_value = self.cmdline
        mock_date.return_value = self.setdate

        mongo_perf.main()

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile))

    def test_suppress(self):

        """Function:  test_suppress

        Description:  Test with suppression.

        Arguments:

        """

        sys.argv = self.argv_list2

        self.assertFalse(mongo_perf.main())

    def test_no_suppress(self):

        """Function:  test_no_suppress

        Description:  Test with no suppression.

        Arguments:

        """

        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.main())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
