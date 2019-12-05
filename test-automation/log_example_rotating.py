# https://pymotw.com/3/logging/index.html#module-logging
# log_example_rotating.py
import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level
# Create a logger with name "MyLogger")
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=2000,
    backupCount=10,
)
my_logger.addHandler(handler)

# Log some messages
for i in range(20):
    my_logger.debug("loop variable i = " + str(i))

# See what files are created
# Look for files matching with LOG_FILENAME
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in sorted(logfiles):
    print(filename)