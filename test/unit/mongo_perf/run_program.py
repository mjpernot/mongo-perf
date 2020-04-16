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

    return True


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

        pass

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
        test_run_program -> Test run_program function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

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
                self.passwd = None
                self.host = "hostname"
                self.port = 27017
                self.auth = True
                self.repset = None

        self.cfg = CfgTest()
        self.server = Server()
        self.func_dict = {"-S": mongo_stat}
        self.args_array = {"-m": True, "-d": True, "-c": True, "-S": True}
        self.args_array2 = {"-m": True, "-d": True, "-c": True, "-S": True,
                            "-e": "ToEmail", "-s": "SubjectLine"}
        self.args_array3 = {"-d": True, "-c": True, "-S": True}

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

    @mock.patch("mongo_perf.cmds_gen.disconnect")
    @mock.patch("mongo_perf.gen_libs.load_module")
    @mock.patch("mongo_perf.mongo_class.RepSet")
    def test_replica_set(self, mock_inst, mock_cfg, mock_disconn):

        """Function:  test_replica_set

        Description:  Test connecting to Mongo replica set.

        Arguments:

        """

        self.cfg.repset = "replicasetname"
        mock_inst.return_value = self.server
        mock_cfg.side_effect = [self.cfg, True]
        mock_disconn.return_value = True

        self.assertFalse(mongo_perf.run_program(self.args_array,
                                                self.func_dict))

    @mock.patch("mongo_perf.cmds_gen.disconnect")
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
    @mock.patch("mongo_perf.cmds_gen.disconnect")
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
