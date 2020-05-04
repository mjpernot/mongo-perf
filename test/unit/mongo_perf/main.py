#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in mongo_perf.py.

    Usage:
        test/unit/mongo_perf/main.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_perf
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_set_default_args -> Test setting default arguments.
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

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-c": "CfgFile", "-d": "CfgDir"}
        self.args_array2 = {"-c": "CfgFile", "-d": "CfgDir", "-S": True,
                            "-j": True}
        self.args_array3 = {"-c": "CfgFile", "-d": "CfgDir", "-S": True,
                            "-j": True, "-n": 1, "-b": 1}

    @mock.patch("mongo_perf.run_program")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser")
    def test_set_default_args(self, mock_arg, mock_help, mock_run):

        """Function:  test_set_default_args

        Description:  Test setting default arguments.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array2
        mock_arg.arg_add_def.return_value = self.args_array3
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_run.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_require")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser.arg_parse2")
    def test_help_false(self, mock_arg, mock_help, mock_req):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_require")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser.arg_parse2")
    def test_arg_req_true(self, mock_arg, mock_help, mock_req):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_cond_req")
    @mock.patch("mongo_perf.arg_parser.arg_require")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser.arg_parse2")
    def test_arg_req_false(self, mock_arg, mock_help, mock_req, mock_cond):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_cond_req")
    @mock.patch("mongo_perf.arg_parser.arg_require")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser.arg_parse2")
    def test_arg_cond_false(self, mock_arg, mock_help, mock_req, mock_cond):

        """Function:  test_arg_cond_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_dir_chk_crt")
    @mock.patch("mongo_perf.arg_parser.arg_cond_req")
    @mock.patch("mongo_perf.arg_parser.arg_require")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser.arg_parse2")
    def test_arg_cond_true(self, mock_arg, mock_help, mock_req, mock_cond,
                           mock_dir):

        """Function:  test_arg_cond_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = True
        mock_dir.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.arg_parser.arg_dir_chk_crt")
    @mock.patch("mongo_perf.arg_parser.arg_cond_req")
    @mock.patch("mongo_perf.arg_parser.arg_require")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser.arg_parse2")
    def test_arg_dir_true(self, mock_arg, mock_help, mock_req, mock_cond,
                          mock_dir):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_cond.return_value = True
        mock_dir.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser")
    def test_arg_dir_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser")
    def test_arg_file_true(self, mock_arg, mock_help):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.arg_parser")
    def test_arg_file_false(self, mock_arg, mock_help, mock_run):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_run.return_value = True

        self.assertFalse(mongo_perf.main())


if __name__ == "__main__":
    unittest.main()
