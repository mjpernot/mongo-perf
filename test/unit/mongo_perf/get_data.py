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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_perf                               # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class SubProcess():                                     # pylint:disable=R0903

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
