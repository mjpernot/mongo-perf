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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_perf                               # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                                         # pylint:disable=R0903

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
        self.user = "mongo"
        self.japd = "japd"
        self.host = "hostname"
        self.port = 27017
        self.auth = False
        self.auth_db = "admin"
        self.repset = None
        self.repset_hosts = None
        self.status = True
        self.err_msg = None
        self.config = {"authMechanism": "SCRAM-SHA-1"}
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        return self.status, self.err_msg


class SubProcess():                                     # pylint:disable=R0903

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

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_insert_failed
        test_insert_success
        test_conn_fail_suppress
        test_connection_fail
        test_connection_success
        test_no_suppress
        test_suppress
        test_replica_set
        test_mongo
        test_flatten_json
        test_append_file
        test_write_file
        test_json
        test_default_args_array
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.subproc = SubProcess()
        self.config = "mongo"
        self.config2 = "mongo2"
        self.path = "./test/integration/mongo_perf/baseline"
        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"

        # Python 2 and 3 product different outputs
        if sys.version_info[0] == 3:
            self.outfile = os.path.join(self.path, "mongo_stat_outfile-p3.txt")
            self.outfile2 = os.path.join(
                self.path, "mongo_stat_outfile2-p3.txt")
            self.outfile3 = os.path.join(
                self.path, "mongo_stat_outfile3-p3.txt")
        else:
            self.outfile = os.path.join(self.path, "mongo_stat_outfile.txt")
            self.outfile2 = os.path.join(self.path, "mongo_stat_outfile2.txt")
            self.outfile3 = os.path.join(self.path, "mongo_stat_outfile3.txt")

        self.req_arg_list = ["--authenticationDatabase=admin", "--json"]
        self.opt_arg_list = {"-n": "-n="}
        self.func_names = {"-S": mongo_perf.mongo_stat}
        self.args = gen_class.ArgParser()
        self.args2 = gen_class.ArgParser()
        self.args2a = gen_class.ArgParser()
        self.args3 = gen_class.ArgParser()
        self.args4 = gen_class.ArgParser()
        self.args5 = gen_class.ArgParser()
        self.args6 = gen_class.ArgParser()
        self.args7 = gen_class.ArgParser()
        self.args8 = gen_class.ArgParser()
        self.args.args_array = {
            "-c": self.config, "-d": self.path, "-S": True, "-z": True}
        self.args2.args_array = {
            "-c": self.config, "-d": self.path, "-S": True, "-z": True}
        self.args2a.args_array = {
            "-c": self.config, "-d": self.path, "-S": True, "-z": True,
            "-w": True}
        self.args3.args_array = {
            "-c": self.config, "-d": self.path, "-S": True, "-o": self.ofile,
            "-z": True}
        self.args4.args_array = {
            "-c": self.config, "-d": self.path, "-S": True, "-o": self.ofile,
            "-a": True, "-z": True}
        self.args5.args_array = {
            "-c": self.config, "-d": self.path, "-S": True, "-o": self.ofile,
            "-f": True, "-z": True}
        self.args6.args_array = {
            "-c": self.config, "-d": self.path, "-S": True, "-m": self.config,
            "-z": True, "-i": "dbname:tblname"}
        self.args7.args_array = {
            "-c": self.config2, "-d": self.path, "-S": True, "-z": True}
        self.args8.args_array = {
            "-c": self.config, "-d": self.path, "-S": True}
        self.results = \
            "{1:{1: 11, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}, \
            2: {2: 22, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}}"
        self.setdate = "2020-04-29"

    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.subprocess.Popen")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_insert_fail(                               # pylint:disable=R0913
            self, mock_inst, mock_disconn, mock_popen, mock_cmd, mock_mongo):

        """Function:  test_insert_fail

        Description:  Test with failed insert into Mongo.

        Arguments:

        """

        mock_mongo.return_value = (False, "Connection error")
        mock_cmd.return_value = self.results
        mock_popen.return_value = self.subproc
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_perf.run_program(
                    self.args6, self.func_names, req_arg=self.req_arg_list,
                    opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.subprocess.Popen")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_insert_success(                            # pylint:disable=R0913
            self, mock_inst, mock_disconn, mock_popen, mock_cmd, mock_mongo):

        """Function:  test_insert_success

        Description:  Test with successful insert into Mongo.

        Arguments:

        """

        mock_mongo.return_value = (True, None)
        mock_cmd.return_value = self.results
        mock_popen.return_value = self.subproc
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mongo_perf.run_program(
                self.args6, self.func_names, req_arg=self.req_arg_list,
                opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_conn_fail_suppress(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_conn_fail_suppress

        Description:  Test with failed conn with suppression.

        Arguments:

        """

        self.server.status = False
        self.server.err_msg = "Error connection message"

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mongo_perf.run_program(
                self.args2a, self.func_names, req_arg=self.req_arg_list,
                opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_connection_fail(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_connection_fail

        Description:  Test with failed connection to mongo.

        Arguments:

        """

        self.server.status = False
        self.server.err_msg = "Error connection message"

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_perf.run_program(
                    self.args2, self.func_names, req_arg=self.req_arg_list,
                    opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_connection_success(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_connection_success

        Description:  Test with successful connection to mongo.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mongo_perf.run_program(
                self.args2, self.func_names, req_arg=self.req_arg_list,
                opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_no_suppress(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_no_suppress

        Description:  Test with no suppression.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_perf.run_program(
                    self.args8, self.func_names, req_arg=self.req_arg_list,
                    opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_suppress(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_suppress

        Description:  Test with suppression.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mongo_perf.run_program(
                self.args2, self.func_names, req_arg=self.req_arg_list,
                opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.subprocess.Popen")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_class.RepSet")
    def test_replica_set(self, mock_inst, mock_disconn, mock_popen):

        """Function:  test_replica_set

        Description:  Test connecting to Mongo replica set.

        Arguments:

        """

        mock_popen.return_value = self.subproc
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mongo_perf.run_program(
                self.args7, self.func_names, req_arg=self.req_arg_list,
                opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.mongo_libs.ins_doc")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.subprocess.Popen")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_mongo(                                     # pylint:disable=R0913
            self, mock_inst, mock_disconn, mock_popen, mock_cmd, mock_mongo):

        """Function:  test_mongo

        Description:  Test with mongo option.

        Arguments:

        """

        mock_mongo.return_value = (True, None)
        mock_cmd.return_value = self.results
        mock_popen.return_value = self.subproc
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mongo_perf.run_program(
                self.args6, self.func_names, req_arg=self.req_arg_list,
                opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_flatten_json(self, mock_inst, mock_disconn, mock_cmds, mock_date):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_date.return_value = self.setdate

        mongo_perf.run_program(
            self.args5, self.func_names, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list)

        self.assertTrue(filecmp.cmp(self.outfile3, self.ofile))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_append_file(self, mock_inst, mock_disconn, mock_cmds, mock_date):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_date.return_value = self.setdate

        mongo_perf.run_program(
            self.args4, self.func_names, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list)
        mongo_perf.run_program(
            self.args4, self.func_names, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list)

        self.assertTrue(filecmp.cmp(self.outfile2, self.ofile))

    @mock.patch("mongo_perf.gen_libs.get_date")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_write_file(self, mock_inst, mock_disconn, mock_cmds, mock_date):

        """Function:  test_write_file

        Description:  Test option to write to file.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_date.return_value = self.setdate

        mongo_perf.run_program(
            self.args3, self.func_names, req_arg=self.req_arg_list,
            opt_arg=self.opt_arg_list)

        self.assertTrue(filecmp.cmp(self.outfile, self.ofile))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_json(self, mock_inst, mock_disconn, mock_cmds):

        """Function:  test_json

        Description:  Test with JSON option.

        Arguments:

        """

        mock_cmds.return_value = self.results
        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(
            mongo_perf.run_program(
                self.args2, self.func_names, req_arg=self.req_arg_list,
                opt_arg=self.opt_arg_list))

    @mock.patch("mongo_perf.subprocess.Popen")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_default_args_array(self, mock_inst, mock_disconn, mock_popen):

        """Function:  test_default_args_array

        Description:  Test with default options.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_popen.return_value = self.subproc

        self.assertFalse(
            mongo_perf.run_program(
                self.args, self.func_names, req_arg=self.req_arg_list,
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
