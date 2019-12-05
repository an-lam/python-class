# test_commands_log.py
import logging
import logging.handlers

from ssh_connection import SSHconnection

"""
Setting message level:
   Level      Value
   CRITICAL   50
   ERROR      40
   WARNING    30
   INFO       20
   DEBUG      10
   UNSET      0
The log message is only emitted if the handler and logger are configured to 
emit messages of that level or higher. For example, if a message is CRITICAL,
and the logger is set to ERROR, the message is emitted (50 > 40).
If a message is a WARNING, and the logger is set to produce only messages set to 
ERROR, the message is not emitted (30 < 40).
"""
LOG_FILENAME = 'logging_example5.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    #level=logging.INFO,
    level=logging.DEBUG,
    #level=logging.ERROR,
)

#hostname = '10.203.35.153'
hostname = '10.0.0.21'
port = 22
username = 'pi'
password = 'anlam2018'

def setup_log(logger):
    # Getting a logger instance
    logger = logging.getLogger(__name__)
    # logger = logging.getLogger()  # get default logger "ROOT"
    logger.info("Calling setup_log")

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(
                       LOG_FILENAME,
                       maxBytes=5000,  # max size of log file
                       backupCount=3,  # how many log files to keep
              )
    logger.addHandler(handler)

def test_dmesg(logger):
    ssh_con = SSHconnection(hostname, username, password, port)
    out, err = ssh_con.execute_command_buffer("dmesg")
    print("output from Raspberry Pi: " + out)
    logger.info("output from Raspberry Pi: " + out)
    # assert out == ""
    #assert out != ""
    ssh_con.close()


if __name__ == "__main__":
    setup_log(logging)
    print("Calling test_dmesg:\n")
    test_dmesg(logging)


