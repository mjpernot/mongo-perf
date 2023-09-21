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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_perf
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        arg_add_def
        arg_cond_req
        arg_dir_chk
        arg_file_chk
        arg_require
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()
        self.opt_val = None
        self.multi_val = None
        self.do_parse = None
        self.defaults = None
        self.add_def_opt_req = None
        self.file_perm_chk = None
        self.file_crt = None
        self.arg_file_chk2 = True
        self.opt_req = None
        self.opt_req2 = True
        self.opt_con_req = None
        self.opt_con_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False

    def arg_add_def(self, defaults, opt_req=None):

        """Method:  arg_add_def

        Description:  Method stub holder for gen_class.ArgParser.arg_add_def.

        Arguments:

        """

        if not opt_req:
            opt_req = list()

        self.defaults = defaults
        self.add_def_opt_req = opt_req

    def arg_cond_req(self, opt_con_req):

        """Method:  arg_cond_req

        Description:  Method stub holder for gen_class.ArgParser.arg_cond_req.

        Arguments:

        """

        self.opt_con_req = opt_con_req

        return self.opt_con_req2

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_file_chk(self, file_perm_chk, file_crt):

        """Method:  arg_file_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_file_chk.

        Arguments:

        """

        self.file_perm_chk = file_perm_chk
        self.file_crt = file_crt

        return self.arg_file_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            (input) cmdline
            (input) flavor

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_help_true
        test_help_false
        test_arg_req_false
        test_arg_req_true
        test_arg_cond_false
        test_arg_cond_true
        test_arg_dir_false
        test_arg_dir_true
        test_arg_file_false
        test_arg_file_true
        test_run_program
        test_programlock_true
        test_programlock_false
        test_programlock_id
        test_set_j_option
        test_set_default_args

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args4 = ArgParser()
        self.args6 = ArgParser()
        self.args.args_array = {"-c": "CfgFile", "-d": "CfgDir"}
        self.args2.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-S": True, "-j": True}
        self.args4.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-S": True, "-i": True}
        self.args6.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-y": "Flavor"}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_arg_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_arg_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_arg_cond_false(self, mock_arg, mock_help):

        """Function:  test_arg_cond_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_arg_cond_true(self, mock_arg, mock_help):

        """Function:  test_arg_cond_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_arg_dir_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_arg_dir_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_arg_file_false(self, mock_arg, mock_help):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.ProgramLock")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_arg_file_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.ProgramLock")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_run_program(self, mock_arg, mock_help, mock_lock):

        """Function:  test_run_program

        Description:  Test with run_program.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.ProgramLock")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_programlock_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.gen_class.ProgramLock")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_programlock_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.side_effect = \
            mongo_perf.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.ProgramLock")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_programlock_id(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_id

        Description:  Test ProgramLock with flavor ID.

        Arguments:

        """

        mock_arg.return_value = self.args6
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.ProgramLock")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_set_j_option(self, mock_arg, mock_help, mock_lock):

        """Function:  test_set_j_option

        Description:  Test with setting default arg for -i option.

        Arguments:

        """

        mock_arg.return_value = self.args4
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_perf.main())

    @mock.patch("mongo_perf.run_program", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.ProgramLock")
    @mock.patch("mongo_perf.gen_libs.help_func")
    @mock.patch("mongo_perf.gen_class.ArgParser")
    def test_set_default_args(self, mock_arg, mock_help, mock_lock):

        """Function:  test_set_default_args

        Description:  Test setting default arguments.

        Arguments:

        """

        mock_arg.return_value = self.args2
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_perf.main())


if __name__ == "__main__":
    unittest.main()
