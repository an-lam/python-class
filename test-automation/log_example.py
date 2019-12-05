# https://pymotw.com/3/logging/index.html#module-logging
# logging_file_example.py
"""
Setting debug level:
   Level      Value
   CRITICAL   50
   ERROR      40
   WARNING    30
   INFO       20
   DEBUG      10
   UNSET      0
The log message is only emitted if the handler and logger are configured to
emit messages of that level or higher. For example, if a message is CRITICAL,
and the logger is set to ERROR, the message is emitted (50 > 40). If a
message is a WARNING, and the logger is set to produce only messages set to
ERROR, the message is not emitted (30 < 40).
"""

import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
    # level=logging.INFO,
    #level=logging.ERROR,
)

logging.debug('Debug message')
logging.info('Info message')

# Open 'rt' = read-text mode
with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print("Log file: {}".format(LOG_FILENAME))
print(body)