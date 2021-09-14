#!/usr/bin/python
# Classification (U)

"""Program:  _process_json.py

    Description:  Unit testing of _process_json in mongo_perf.py.

    Usage:
        test/unit/mongo_perf/_process_json.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_insert_fail
        test_insert_success
        test_std
        test_no_std
        test_indent_json
        test_flatten_json
        test_write_file
        test_append_file
        test_mongo

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.no_std = True
        self.no_std2 = False
        self.mode = "a"
        self.mode2 = "w"
        self.indent = None
        self.indent2 = 4
        self.outfile = "OutputFile"
        self.outfile2 = None
        self.db_tbl = "database:table"
        self.class_cfg = "mongo_config"
        self.data = {"Server": "ServerName",
                     "AsOf": "DataTime" + " " + "Time",
                     "RepSet": "RepSetName", "RepState": "SEC",
                     "PerfStats": {1: 11, 'time': 'timestamp'}}

    @mock.patch("mongo_perf.mongo_libs")
    def test_insert_fail(self, mock_mongo):

        """Function:  test_insert_fail

        Description:  Test with failed insert into Mongo.

        Arguments:

        """

        mock_mongo.ins_doc.return_value = (False, "Insert Failed")

        with gen_libs.no_std_out():
            self.assertFalse(mongo_perf._process_json(
                self.data, self.outfile2, self.indent, self.no_std, self.mode2,
                db_tbl=self.db_tbl, class_cfg=self.class_cfg))

    @mock.patch("mongo_perf.mongo_libs")
    def test_insert_success(self, mock_mongo):

        """Function:  test_insert_success

        Description:  Test with successful insert into Mongo.

        Arguments:

        """

        mock_mongo.ins_doc.return_value = (True, None)

        self.assertFalse(mongo_perf._process_json(
            self.data, self.outfile2, self.indent, self.no_std, self.mode2,
            db_tbl=self.db_tbl, class_cfg=self.class_cfg))

    @mock.patch("mongo_perf.gen_libs")
    def test_std(self, mock_libs):

        """Function:  test_std

        Description:  Test with standard out suppressed.

        Arguments:

        """

        mock_libs.print_data.return_value = True

        self.assertFalse(mongo_perf._process_json(
            self.data, self.outfile2, self.indent, self.no_std, self.mode2))

    @mock.patch("mongo_perf.gen_libs")
    def test_no_std(self, mock_libs):

        """Function:  test_no_std

        Description:  Test with no standard out suppressed.

        Arguments:

        """

        mock_libs.print_data.return_value = True

        self.assertFalse(mongo_perf._process_json(
            self.data, self.outfile2, self.indent, self.no_std2, self.mode2))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs")
    def test_indent_json(self, mock_libs):

        """Function:  test_indent_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        mock_libs.write_file.return_value = True

        self.assertFalse(mongo_perf._process_json(
            self.data, self.outfile, self.indent2, self.no_std, self.mode2))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs")
    def test_flatten_json(self, mock_libs):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        mock_libs.write_file.return_value = True

        self.assertFalse(mongo_perf._process_json(
            self.data, self.outfile, self.indent, self.no_std, self.mode2))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs")
    def test_write_file(self, mock_libs):

        """Function:  test_write_file

        Description:  Test write to file.

        Arguments:

        """

        mock_libs.write_file.return_value = True

        self.assertFalse(mongo_perf._process_json(
            self.data, self.outfile, self.indent, self.no_std, self.mode2))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs")
    def test_append_file(self, mock_libs):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        mock_libs.write_file.return_value = True

        self.assertFalse(mongo_perf._process_json(
            self.data, self.outfile, self.indent, self.no_std, self.mode))

    @mock.patch("mongo_perf.mongo_libs")
    def test_mongo(self, mock_mongo):

        """Function:  test_mongo

        Description:  Test with sending data to mongo.

        Arguments:

        """

        mock_mongo.ins_doc.return_value = (True, None)

        self.assertFalse(mongo_perf._process_json(
            self.data, self.outfile2, self.indent, self.no_std, self.mode2,
            db_tbl=self.db_tbl, class_cfg=self.class_cfg))


if __name__ == "__main__":
    unittest.main()
