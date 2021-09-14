#!/usr/bin/python
# Classification (U)

"""Program:  get_data.py

    Description:  Unit testing of get_data in mongo_perf.py.

    Usage:
        test/unit/mongo_perf/get_data.py

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


class SubProcess(object):

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        communicate

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

        pass

    def communicate(self):

        """Method:  communicate

        Description:  Mock representation of subprocess.communicate method.

        Arguments:

        """

        return "Data", True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_get_data

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cmd = "testme"
        self.return_data = "Data"

    @mock.patch("mongo_perf.subprocess.PIPE")
    @mock.patch("mongo_perf.subprocess.Popen")
    def test_get_data(self, mock_open, mock_pipe):

        """Function:  test_get_data

        Description:  Test get_data function.

        Arguments:

        """

        mock_open.return_value = SubProcess()
        mock_pipe.return_value = "Pipe_to_process"

        self.assertEqual(mongo_perf.get_data(self.cmd), self.return_data)


if __name__ == "__main__":
    unittest.main()
