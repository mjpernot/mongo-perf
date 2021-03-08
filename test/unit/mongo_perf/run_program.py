#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mongo_perf.py.

    Usage:
        test/unit/mongo_perf/run_program.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def mongo_stat(server, args_array, **kwargs):

    """Method:  mongo_stat

    Description:  Function stub holder for mongo_perf.mongo_stat.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Stub holder for dictionary of args.
        (input) **kwargs
            class_cfg -> Stub holder for Mongo configuration.

    """

    status = True

    if server and args_array and kwargs.get("class_cfg", True):
        status = True

    return status


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

        self.status = True
        self.err_msg = None

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        return self.status, self.err_msg


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.name = "Mongo"
        self.user = "mongo"
        self.japd = None
        self.host = "hostname"
        self.port = 27017
        self.auth = True
        self.auth_db = "admin"
        self.use_arg = True
        self.use_uri = False
        self.repset = None
        self.repset_hosts = None


class CfgTest2(object):

    """Class:  CfgTest2

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.name = "Mongo"
        self.user = "mongo"
        self.japd = None
        self.host = "hostname"
        self.port = 27017
        self.auth = True
        self.auth_db = "admin"
        self.use_arg = True
        self.use_uri = False
        self.repset = None
        self.repset_hosts = None
        self.auth_mech = "SCRAM-SHA-1"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_conn_fail_suppress -> Test with failed conn with suppression.
        test_connection_fail -> Test with failed connection.
        test_connection_success -> Test with successful connection.
        test_auth_mech -> Test with authorization mechanism setting.
        test_no_auth_mech -> Test with no authorization mechanism setting.
        test_replica_set -> Test connecting to Mongo replica set.
        test_mongo -> Test with mongo option.
        test_run_program -> Test run_program function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.cfg2 = CfgTest2()
        self.server = Server()
        self.func_dict = {"-S": mongo_stat}
        self.args_array = {"-m": True, "-d": True, "-c": True, "-S": True}
        self.args_array2 = {"-m": True, "-d": True, "-c": True, "-S": True,
                            "-e": "ToEmail", "-s": "SubjectLine"}
        self.args_array3 = {"-d": True, "-c": True, "-S": True}
        self.args_array4 = {"-w": True, "-d": True, "-c": True, "-S": True}

    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_conn_fail_suppress(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_conn_fail_suppress

        Description:  Test with failed connection with suppression.

        Arguments:

        """

        self.server.status = False
        self.server.err_msg = "Error Connection Message"

        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg, True]
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(self.args_array4,
                                                self.func_dict))

    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_connection_fail(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_connection_fail

        Description:  Test with failed connection.

        Arguments:

        """

        self.server.status = False
        self.server.err_msg = "Error Connection Message"

        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg, True]
        mock_disconn.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.run_program(self.args_array,
                                                    self.func_dict))

    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_connection_success(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_connection_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg, True]
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(self.args_array,
                                                self.func_dict))

    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_class.RepSet")
    def test_auth_mech(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_auth_mech

        Description:  Test with authorization mechanism setting.

        Arguments:

        """

        self.cfg2.repset = "replicasetname"
        self.cfg2.repset_hosts = ["host1:27017", "host2:27017"]

        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg2, self.cfg2]
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(self.args_array,
                                                self.func_dict))

    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_class.RepSet")
    def test_no_auth_mech(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_no_auth_mech

        Description:  Test with no authorization mechanism setting.

        Arguments:

        """

        self.cfg.repset = "replicasetname"
        self.cfg.repset_hosts = ["host1:27017", "host2:27017"]

        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg, True]
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(self.args_array,
                                                self.func_dict))

    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_class.RepSet")
    def test_replica_set(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_replica_set

        Description:  Test connecting to Mongo replica set.

        Arguments:

        """

        self.cfg.repset = "replicasetname"
        self.cfg.repset_hosts = ["host1:27017", "host2:27017"]

        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg, True]
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(self.args_array,
                                                self.func_dict))

    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_mongo(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_mongo

        Description:  Test with mongo option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg, True]
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(self.args_array,
                                                self.func_dict))

    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_libs.disconnect")
    @mock.patch("mongo_perf.mongo_libs.create_instance")
    def test_run_program(self, mock_inst, mock_disconn, mock_cfg):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True
        mock_cfg.return_value = self.cfg

        self.assertFalse(mongo_perf.run_program(self.args_array3,
                                                self.func_dict))


if __name__ == "__main__":
    unittest.main()
