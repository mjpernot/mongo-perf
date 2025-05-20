# Classification (U)

"""Program:  get_data.py

    Description:  Integration testing of get_data in mongo_perf.py.

    Usage:
        test/intergration/mysql_db_admin/get_data.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import filecmp
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_perf                               # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs              # pylint:disable=E0401,C0413,R0402
import mongo_lib.mongo_class as mongo_class  # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_return_data2
        test_return_data

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        config_dir = "test/integration/config"
        config_name = "mongo"
        cfg = gen_libs.load_module(config_name, config_dir)
        user = "--username=" + cfg.user
        japd = "--password=" + cfg.japd
        host = "--host=" + cfg.host + ":" + str(cfg.port)
        authdb = "--authenticationDatabase=" + cfg.auth_db
        self.cmd = [
            "mongostat", user, host, japd, "--json", authdb, "-n=1", "1"]

    def test_return_data2(self):

        """Function:  test_return_data2

        Description:  Test with returning datatype of bytes.

        Arguments:

        """

        self.assertTrue(isinstance(mongo_perf.get_data(self.cmd), bytes))

    def test_return_data(self):

        """Function:  test_return_data

        Description:  Test with returning data.

        Arguments:

        """

        self.assertIsNotNone(mongo_perf.get_data(self.cmd))


if __name__ == "__main__":
    unittest.main()
