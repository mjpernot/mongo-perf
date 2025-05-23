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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_perf                               # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs              # pylint:disable=E0401,C0413,R0402
import lib.gen_class as gen_class            # pylint:disable=E0401,C0413,R0402
import mongo_lib.mongo_libs as mongo_libs    # pylint:disable=E0401,C0413,R0402
import mongo_lib.mongo_class as mongo_class  # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


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

        self.args = gen_class.ArgParser(
            test_argv, opt_val=opt_val_list, opt_def=opt_def_dict,
            multi_val=opt_multi_list, do_parse=True)
        self.args.arg_add_def(defaults=opt_def_dict2)
        mongo = mongo_libs.create_instance(
            self.args.get_val("-c"), self.args.get_val("-d"),
            mongo_class.Server)
        mongo.connect()

#        path = "/dir/path"
        self.req_arg = ["--authenticationDatabase=admin", "--json"]
        self.basepath = "./test/integration/mongo_perf/baseline"
        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"
#        self.outfile = os.path.join(self.basepath, "mongo_stat_outfile.txt")
#        self.outfile2 = os.path.join(self.basepath, "mongo_stat_outfile2.txt")
#        self.outfile3 = os.path.join(self.basepath, "mongo_stat_outfile3.txt")
#        self.outfile_p3 = os.path.join(
#            self.basepath, "mongo_stat_outfile-p3.txt")
#        self.outfile2_p3 = os.path.join(
#            self.basepath, "mongo_stat_outfile2-p3.txt")
#        self.outfile3_p3 = os.path.join(
#            self.basepath, "mongo_stat_outfile3-p3.txt")
#        self.server = Server()
#        self.subproc = SubProcess()
#        self.args = ArgParser()
#        self.args2 = ArgParser()
#        self.args3 = ArgParser()
#        self.args4 = ArgParser()
#        self.args5 = ArgParser()
#        self.args6 = ArgParser()
#        self.args7 = ArgParser()
#        self.args.args_array = {
#            "-c": "mongo", "-d": "config", "-S": True, "-z": True, "-p": path}
#        self.args2.args_array = {
#            "-c": "mongo", "-d": "config", "-S": True, "-z": True, "-p": path}
#        self.args3.args_array = {
#            "-c": "mongo", "-d": "config", "-S": True, "-a": True, "-z": True,
#            "-p": path}
#        self.args4.args_array = {
#            "-c": "mongo", "-d": "config", "-S": True, "-f": True, "-z": True,
#            "-p": path}
#        self.args5.args_array = {
#            "-c": "mongo", "-d": "config", "-S": True, "-b": 1, "-z": True,
#            "-p": path}
#        self.args6.args_array = {
#            "-c": "mongo", "-d": "config", "-S": True, "-p": path}
#        self.db_tbl = "database:table"
#        self.class_cfg = "mongo_config"
#        self.results = \
#            "{1:{1: 11, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}, \
#            2: {2: 22, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}}"
#        self.setdate = "2020-04-29"

    @unittest.skip("Skipping test for now")
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
            self.assertFalse(
                mongo_perf.mongo_stat(
                    self.server, self.args2, db_tbl=self.db_tbl,
                    class_cfg=self.class_cfg, req_arg=self.req_arg))

    @unittest.skip("Skipping test for now")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    def test_insert_success(self, mock_mongo, mock_cmds):

        """Function:  test_insert_success

        Description:  Test with successful insert into Mongo.

        Arguments:

        """

        mock_mongo.return_value = (True, None)
        mock_cmds.return_value = self.results

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args2, db_tbl=self.db_tbl,
                class_cfg=self.class_cfg, req_arg=self.req_arg))

    @unittest.skip("Skipping test for now")
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
            self.assertFalse(
                mongo_perf.mongo_stat(
                    self.server, self.args6, req_arg=self.req_arg))

    @unittest.skip("Skipping test for now")
    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    def test_suppress(self, mock_cmds, mock_date):

        """Function:  test_suppress

        Description:  Test option to standard JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_date.return_value = self.setdate

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args2, req_arg=self.req_arg))

    @unittest.skip("Skipping test for now")
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
            self.server, self.args2, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile) or
                        filecmp.cmp(self.outfile_p3, self.ofile))

    @unittest.skip("Skipping test for now")
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
            self.server, self.args4, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile) or
                        filecmp.cmp(self.outfile3_p3, self.ofile))

    @unittest.skip("Skipping test for now")
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
            self.server, self.args3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)
        mongo_perf.mongo_stat(
            self.server, self.args3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile2, self.ofile) or
                        filecmp.cmp(self.outfile2_p3, self.ofile))

    @unittest.skip("Skipping test for now")
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
            self.server, self.args3, class_cfg=self.class_cfg,
            req_arg=self.req_arg, ofile=self.ofile)

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile) or
                        filecmp.cmp(self.outfile_p3, self.ofile))

    @unittest.skip("Skipping test for now")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    def test_mongo(self, mock_mongo, mock_cmds):

        """Function:  test_mongo

        Description:  Test with sending data to mongo.

        Arguments:

        """

        mock_mongo.return_value = (True, None)
        mock_cmds.return_value = self.results

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args2, db_tbl=self.db_tbl,
                class_cfg=self.class_cfg, req_arg=self.req_arg))

    @unittest.skip("Skipping test for now")
    @mock.patch("mongo_perf.get_data")
    def test_dict_format(self, mock_cmds):

        """Function:  test_dict_format

        Description:  Test with converting output data to dictionary.

        Arguments:

        """

        mock_cmds.return_value = self.results

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args2, req_arg=self.req_arg))

    @unittest.skip("Skipping test for now")
    @mock.patch("mongo_perf.subprocess.Popen")
    def test_polling(self, mock_popen):

        """Function:  test_polling

        Description:  Test with polling option.

        Arguments:

        """

        mock_popen.return_value = self.subproc

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args5, req_arg=self.req_arg))

    @unittest.skip("Skipping test for now")
    @mock.patch("mongo_perf.subprocess.Popen")
    def test_std_out_file(self, mock_popen):

        """Function:  test_std_out_file

        Description:  Test with standard out to file.

        Arguments:

        """

        mock_popen.return_value = self.subproc

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args, req_arg=self.req_arg,
                ofile=self.ofile))

    def test_default_args_array(self):

        """Function:  test_default_args_array

        Description:  Test with default options.

        Arguments:

        """

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args, req_arg=self.req_arg))

    @unittest.skip("Skipping test for now")
    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
