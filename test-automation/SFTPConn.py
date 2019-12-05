import paramiko
import logging

#log = logging.getLogger(__name__)


class SFTPConn(object):

    def __init__(self, hostname, username, password):
        self.sftp = None
        self.sftp_open = False
        self._hostname = hostname
        self._username = username
        self._password = password
        self._port = 22

    def open(self):
        # open SSH Transport stream
        self.transport = paramiko.Transport((self._hostname, self._port))
        self.transport.connect(username=self._username, password=self._password)
        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.sftp_open = True

    def get(self, remote_path, local_path=None):
        """
        Copies a file from the remote host to the local host.
        """
        try:
            self.open()
            self.sftp.get(remote_path, local_path)
            # log.info("get file from %s :%s to %s" % (self._hostname, remote_path, local_path))
        finally:
            self.close()

    def put(self, local_path, remote_path=None):
        """
        Copies a file from the local host to the remote host
        """
        try:
            self.open()
            self.sftp.put(local_path, remote_path)
            # log.info("put file %s to %s:%s" % (local_path, self._hostname, remote_path))
        finally:
            self.close()

    def close(self):
        if self.sftp_open:
            self.sftp.close()
            self.sftp_open = False
        self.transport.close()
