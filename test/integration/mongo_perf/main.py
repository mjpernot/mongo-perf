# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in mongo_perf.py.

    Usage:
        test/integration/mongo_perf/main.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
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
        test_write_file
        test_append_file
        test_expand_json
        test_flatten_json
        test_suppress
        test_no_suppress
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        config = "test/integration/config"
        self.argv_list = ["mongo_perf.py", "-c", "mongo", "-d", config, "-S"]
        self.ofile = "./test/integration/mongo_perf/tmp/outfile.txt"

    def test_write_file(self):

        """Function:  test_write_file

        Description:  Test option to write to file.

        Arguments:

        """

        self.argv_list.append("-z")
        self.argv_list.append("-f")
        self.argv_list.append("-o")
        self.argv_list.append(self.ofile)
        sys.argv = self.argv_list

        mongo_perf.main()

        self.assertTrue(os.path.exists(self.ofile))

    def test_append_file(self):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        self.argv_list.append("-z")
        self.argv_list.append("-f")
        self.argv_list.append("-o")
        self.argv_list.append(self.ofile)
        sys.argv = self.argv_list
        mongo_perf.main()
        self.argv_list.append("-a")
        sys.argv = self.argv_list
        mongo_perf.main()

        self.assertEqual(line_cnt(self.ofile), 2)

    def test_expand_json(self):

        """Function:  test_expand_json

        Description:  Test option to expand JSON data structure.

        Arguments:

        """

        self.argv_list.append("-z")
        self.argv_list.append("-o")
        self.argv_list.append(self.ofile)
        sys.argv = self.argv_list

        mongo_perf.main()

        self.assertGreater(line_cnt(self.ofile), 20)

    def test_flatten_json(self):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        self.argv_list.append("-z")
        self.argv_list.append("-f")
        self.argv_list.append("-o")
        self.argv_list.append(self.ofile)
        sys.argv = self.argv_list

        mongo_perf.main()

        self.assertEqual(line_cnt(self.ofile), 1)

    def test_suppress(self):

        """Function:  test_suppress

        Description:  Test with suppression.

        Arguments:

        """

        self.argv_list.append("-z")
        sys.argv = self.argv_list

        self.assertFalse(mongo_perf.main())

    def test_no_suppress(self):

        """Function:  test_no_suppress

        Description:  Test with no suppression.

        Arguments:

        """

        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf.main())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing.

        Arguments:

        """

        if os.path.isfile(self.ofile):
            os.remove(self.ofile)


if __name__ == "__main__":
    unittest.main()
