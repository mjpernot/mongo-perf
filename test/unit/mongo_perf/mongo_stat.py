#!/usr/bin/python
# Classification (U)

"""Program:  mongo_stat.py

    Description:  Unit testing of mongo_stat in mongo_perf.py.

    Usage:
        test/unit/mysql_db_admin/mongo_stat.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_dict_format -> Test with converting output data to dictionary.
        test_polling -> Test with polling option.
        test_default -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-b": 1}
        self.args_array2 = {"-j": True}

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs")
    def test_dict_format(self, mock_mongo, mock_cmds):

        """Function:  test_dict_format

        Description:  Test with converting output data to dictionary.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_mongo.json_2_out.return_value = True
        mock_cmds.return_value = "{1:{1: 11}, 2: {2: 22}, 3: {3: 33}}"

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array2))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs")
    def test_polling(self, mock_mongo, mock_cmds):

        """Function:  test_polling

        Description:  Test with polling option.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = True

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array))

    @mock.patch("mongo_perf.cmds_gen.run_prog")
    @mock.patch("mongo_perf.mongo_libs")
    def test_default(self, mock_mongo, mock_cmds):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = True

        self.assertFalse(mongo_perf.mongo_stat(self.server, {}))


if __name__ == "__main__":
    unittest.main()
