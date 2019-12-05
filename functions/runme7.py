# runme7.py
# Demonstrate how to use __name__
def runtest():
    print("in runtest()")
    print("__name__:" + __name__)

def runtest2():
    print("in runtest2()")

# Self-test code
# Executed when run, but not executed when import
#print(__name__)
if __name__ == "__main__":
    runtest()
    runtest2()
