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
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_perf                               # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs              # pylint:disable=E0401,C0413,R0402
import lib.gen_class as gen_class            # pylint:disable=E0401,C0413,R0402
import mongo_lib.mongo_libs as mongo_libs    # pylint:disable=E0401,C0413,R0402
import mongo_lib.mongo_class as mongo_class  # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def line_cnt(ofile):

    """Function:  line_cnt

    Description:  Return the number of lines in a file.

    Arguments:
        (input) ofile -> Filename to run count on
        (output) cnt -> Line count from file

    """

    with open(ofile, "r", encoding="UTF-8") as fhdr:
        cnt = sum(1 for _ in fhdr)

    return cnt


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_expand_json
        test_flatten_json
        test_append_file
        test_polling
        test_out_file
        test_no_std_out
        test_default_args_array
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        config = "test/integration/config"
        test_argv = ["mongo_perf.py", "-c", "mongo", "-d", config, "-S"]
        opt_val_list = [
            "-c", "-d", "-b", "-i", "-m", "-n", "-o", "-p", "-s", "-t"]
        opt_def_dict = {"-i": "sysmon:mongo_perf", "-n": "1", "-b": "1"}
        opt_def_dict2 = {"-n": "1", "-b": "1"}
        opt_multi_list = ["-s", "-t"]
        self.opt_arg_list = {"-n": "-n=", "-r": "--tlsInsecure"}
        self.req_arg = ["--authenticationDatabase=admin", "--json"]
        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"

        self.args = gen_class.ArgParser(
            test_argv, opt_val=opt_val_list, opt_def=opt_def_dict,
            multi_val=opt_multi_list, do_parse=True)
        self.args.arg_add_def(defaults=opt_def_dict2)
        self.args.insert_arg("-z", True)
        self.args.insert_arg("-f", True)

        self.args2 = gen_class.ArgParser(
            test_argv, opt_val=opt_val_list, opt_def=opt_def_dict,
            multi_val=opt_multi_list, do_parse=True)
        self.args2.arg_add_def(defaults=opt_def_dict2)
        self.args2.insert_arg("-z", True)

        self.args3 = gen_class.ArgParser(
            test_argv, opt_val=opt_val_list, opt_def=opt_def_dict,
            multi_val=opt_multi_list, do_parse=True)
        self.args3.arg_add_def(defaults=opt_def_dict2)

        self.mongo = mongo_libs.create_instance(
            self.args.get_val("-c"), self.args.get_val("-d"),
            mongo_class.Server)
        self.mongo.connect()

    def test_expand_json(self):

        """Function:  test_expand_json

        Description:  Test option to expand JSON data structure.

        Arguments:

        """

        mongo_perf.mongo_stat(
            self.mongo, self.args2, req_arg=self.req_arg,
            opt_arg=self.opt_arg_list, ofile=self.ofile)
        self.mongo.disconnect()

        self.assertGreater(line_cnt(self.ofile), 20)

    def test_flatten_json(self):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        mongo_perf.mongo_stat(
            self.mongo, self.args, req_arg=self.req_arg,
            opt_arg=self.opt_arg_list, ofile=self.ofile)
        self.mongo.disconnect()

        self.assertEqual(line_cnt(self.ofile), 1)

    def test_append_file(self):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        mongo_perf.mongo_stat(
            self.mongo, self.args, req_arg=self.req_arg,
            opt_arg=self.opt_arg_list, ofile=self.ofile)
        self.args.insert_arg("-a", True)
        mongo_perf.mongo_stat(
            self.mongo, self.args, req_arg=self.req_arg,
            opt_arg=self.opt_arg_list, ofile=self.ofile)
        self.mongo.disconnect()

        self.assertEqual(line_cnt(self.ofile), 2)

    def test_polling(self):

        """Function:  test_polling

        Description:  Test with polling option.

        Arguments:

        """

        self.args.insert_arg("-b", 1)

        mongo_perf.mongo_stat(
            self.mongo, self.args, req_arg=self.req_arg,
            opt_arg=self.opt_arg_list, ofile=self.ofile)
        self.mongo.disconnect()

        self.assertEqual(line_cnt(self.ofile), 1)

    def test_out_file(self):

        """Function:  test_out_file

        Description:  Test with data to file.

        Arguments:

        """

        mongo_perf.mongo_stat(
            self.mongo, self.args2, req_arg=self.req_arg,
            opt_arg=self.opt_arg_list, ofile=self.ofile)
        self.mongo.disconnect()

        self.assertTrue(os.path.exists(self.ofile))

    def test_no_std_out(self):

        """Function:  test_no_std_out

        Description:  Test with no standard out passed.

        Arguments:

        """

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.mongo, self.args2, req_arg=self.req_arg,
                opt_arg=self.opt_arg_list))
        self.mongo.disconnect()

    def test_default_args_array(self):

        """Function:  test_default_args_array

        Description:  Test with default options.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_perf.mongo_stat(
                    self.mongo, self.args3, req_arg=self.req_arg,
                    opt_arg=self.opt_arg_list))
        self.mongo.disconnect()

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
