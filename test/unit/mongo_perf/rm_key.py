#!/usr/bin/python
# Classification (U)

"""Program:  rm_key.py

    Description:  Unit testing of rm_key in mongo_perf.py.

    Usage:
        test/unit/mongo_perf/rm_key.py

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

# Local
sys.path.append(os.getcwd())
import mongo_perf
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_empty_dict -> Test with empty dictionary.
        test_rm_miss_key -> Test with missing key to remove.
        test_rm_no_key -> Test with no key to remove.
        test_rm_key -> Test removing one key.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {}
        self.data2 = {"key1": "val1"}
        self.data3 = {"key1": "val1", "key2": "val2"}
        self.key = ""
        self.key2 = "key2"
        self.key3 = "key3"
        self.key4 = "key1"
        self.results = {}
        self.results2 = {"key1": "val1"}
        self.results3 = {"key1": "val1", "key2": "val2"}

    def test_one_entry(self):

        """Function:  test_one_entry

        Description:  Test with one entry in dictionary.

        Arguments:

        """

        self.assertEqual(mongo_perf.rm_key(self.data2, self.key4),
                         self.results)

    def test_empty_dict(self):

        """Function:  test_empty_dict

        Description:  Test with empty dictionary.

        Arguments:

        """

        self.assertEqual(mongo_perf.rm_key(self.data, self.key2),
                         self.results)

    def test_rm_miss_key(self):

        """Function:  test_rm_miss_key

        Description:  Test with missing key to remove.

        Arguments:

        """

        self.assertEqual(mongo_perf.rm_key(self.data3, self.key3),
                         self.results3)

    def test_rm_no_key(self):

        """Function:  test_rm_no_key

        Description:  Test with no key to remove.

        Arguments:

        """

        self.assertEqual(mongo_perf.rm_key(self.data3, self.key),
                         self.results3)

    def test_rm_key(self):

        """Function:  test_rm_key

        Description:  Test removing one key.

        Arguments:

        """

        self.assertEqual(mongo_perf.rm_key(self.data3, self.key2),
                         self.results2)


if __name__ == "__main__":
    unittest.main()
