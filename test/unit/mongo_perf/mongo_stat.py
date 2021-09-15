#!/usr/bin/python
# Classification (U)

"""Program:  mongo_stat.py

    Description:  Unit testing of mongo_stat in mongo_perf.py.

    Usage:
        test/unit/mongo_perf/mongo_stat.py

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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        self.data = data

        return True

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:
            (input) use_mailx

        """

        status = True

        if use_mailx:
            status = True

        return status


class Server(object):

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


class SubProcess(object):

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

        pass

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_insert_fail
        test_insert_success
        test_mail_subj_mailx
        test_mail_subj
        test_def_subj_mailx
        test_def_subj
        test_email_mailx
        test_email
        test_suppress
        test_no_suppress
        test_flatten_json
        test_write_file
        test_append_file
        test_mongo
        test_dict_format
        test_std_out_file
        test_polling
        test_default
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.mail = Mail()
        self.subproc = SubProcess()
        self.args_array = {"-b": 1}
        self.args_array2 = {"-j": True, "-z": True}
        self.args_array3 = {"-j": True, "-a": True, "-z": True}
        self.args_array4 = {"-j": True, "-f": True, "-z": True}
        self.args_array5 = {"-j": True, "-z": True}
        self.args_array6 = {"-j": True}
        self.args_array7 = {"-j": True, "-z": True, "-t": "email_addr"}
        self.args_array7a = {"-j": True, "-z": True, "-t": "email_addr",
                             "-u": True}
        self.args_array8 = {"-j": True, "-z": True, "-t": "email_addr",
                            "-s": "subject_line"}
        self.args_array8a = {"-j": True, "-z": True, "-t": "email_addr",
                             "-s": "subject_line", "-u": True}
        self.fname = "./test/unit/mongo_perf/tmp/outfile.txt"
        self.ofile = "OutputFile"
        self.db_tbl = "database:table"
        self.class_cfg = "mongo_config"
        self.results = \
            "{1:{1: 11, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}, \
            2: {2: 22, 'time': 'timestamp', 'set': 'spock', 'repl': 'PRI'}}"

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_insert_fail(self, mock_mongo, mock_cmds):

        """Function:  test_insert_fail

        Description:  Test with failed insert into Mongo.

        Arguments:

        """

        mock_mongo.ins_doc.return_value = (False, "Insert Failed")
        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_perf.mongo_stat(
                    self.server, self.args_array2, db_tbl=self.db_tbl,
                    class_cfg=self.class_cfg))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_insert_success(self, mock_mongo, mock_cmds):

        """Function:  test_insert_success

        Description:  Test with successful insert into Mongo.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_mongo.ins_doc.return_value = (True, None)
        mock_cmds.return_value = self.results

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args_array2, db_tbl=self.db_tbl,
                class_cfg=self.class_cfg))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.setup_mail")
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_mail_subj_mailx(self, mock_mongo, mock_cmds, mock_libs,
                             mock_mail):

        """Function:  test_mail_subj_mailx

        Description:  Test with passed with subject line using mailx.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array8a))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.setup_mail")
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_mail_subj(self, mock_mongo, mock_cmds, mock_libs, mock_mail):

        """Function:  test_mail_subj

        Description:  Test with passed with subject line.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array8))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.setup_mail")
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_def_subj_mailx(self, mock_mongo, mock_cmds, mock_libs, mock_mail):

        """Function:  test_def_subj_mailx

        Description:  Test with email default subject line using mailx.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array7a))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.setup_mail")
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_def_subj(self, mock_mongo, mock_cmds, mock_libs, mock_mail):

        """Function:  test_def_subj

        Description:  Test with email default subject line.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array7))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.setup_mail")
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_email_mailx(self, mock_mongo, mock_cmds, mock_libs, mock_mail):

        """Function:  test_email_mailx

        Description:  Test with email option using mailx.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array7a))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_class.setup_mail")
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_email(self, mock_mongo, mock_cmds, mock_libs, mock_mail):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True
        mock_mail.return_value = self.mail

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array7))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_suppress(self, mock_mongo, mock_cmds, mock_libs):

        """Function:  test_suppress

        Description:  Test with suppression.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array5))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_no_suppress(self, mock_mongo, mock_cmds, mock_libs):

        """Function:  test_no_suppress

        Description:  Test with no suppression.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array6))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_flatten_json(self, mock_mongo, mock_cmds):

        """Function:  test_flatten_json

        Description:  Test option to flatten JSON data structure.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_mongo.ins_doc.return_value = True
        mock_cmds.return_value = self.results

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array4,
                                               db_tbl=self.db_tbl))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_write_file(self, mock_mongo, mock_cmds, mock_libs):

        """Function:  test_write_file

        Description:  Test write to file.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.write_file.return_value = True

        self.assertFalse(mongo_perf.mongo_stat(
            self.server, self.args_array5, ofile=self.ofile))

    @mock.patch("mongo_perf.json.dumps", mock.Mock(return_value=True))
    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_append_file(self, mock_mongo, mock_cmds, mock_libs):

        """Function:  test_append_file

        Description:  Test option to append to file.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.write_file.return_value = True

        self.assertFalse(mongo_perf.mongo_stat(
            self.server, self.args_array3, class_cfg=self.class_cfg,
            ofile=self.ofile))

    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_mongo(self, mock_mongo, mock_cmds):

        """Function:  test_mongo

        Description:  Test with sending data to mongo.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_mongo.ins_doc.return_value = (True, None)
        mock_cmds.return_value = self.results

        self.assertFalse(
            mongo_perf.mongo_stat(
                self.server, self.args_array2, db_tbl=self.db_tbl,
                class_cfg=self.class_cfg))

    @mock.patch("mongo_perf.gen_libs")
    @mock.patch("mongo_perf.get_data")
    @mock.patch("mongo_perf.mongo_libs")
    def test_dict_format(self, mock_mongo, mock_cmds, mock_libs):

        """Function:  test_dict_format

        Description:  Test with converting output data to dictionary.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_cmds.return_value = self.results
        mock_libs.print_data.return_value = True
        mock_libs.get_date.return_value = "2020-04-09"

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array2))

    @mock.patch("mongo_perf.subprocess.Popen")
    @mock.patch("mongo_perf.mongo_libs")
    def test_std_out_file(self, mock_mongo, mock_popen):

        """Function:  test_std_out_file

        Description:  Test with standard out to file.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_popen.return_value = self.subproc

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array,
                                               ofile=self.fname))

    @mock.patch("mongo_perf.subprocess.Popen")
    @mock.patch("mongo_perf.mongo_libs")
    def test_polling(self, mock_mongo, mock_popen):

        """Function:  test_polling

        Description:  Test with polling option.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_popen.return_value = self.subproc

        self.assertFalse(mongo_perf.mongo_stat(self.server, self.args_array))

    @mock.patch("mongo_perf.subprocess.Popen")
    @mock.patch("mongo_perf.mongo_libs")
    def test_default(self, mock_mongo, mock_popen):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_mongo.create_cmd.return_value = ["command"]
        mock_popen.return_value = self.subproc

        self.assertFalse(mongo_perf.mongo_stat(self.server, {}))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.fname):
            os.remove(self.fname)


if __name__ == "__main__":
    unittest.main()
