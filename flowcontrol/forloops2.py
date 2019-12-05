# forloops2.py
"""
adfa;fja;
"""

for state in ["idle", 2, "running", "sleeping", "ready to run"]:
    # print("This process is " + state)
    print("This process is {}".format(state))

for i in range(0, 20, 5):
    print("i is {} ".format(i))
    #print("i is " + str(i))

for i in range(1,10):
    for j in range(1,10):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("================")
