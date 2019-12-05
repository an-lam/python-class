import os

# global variable
tab_stop = 0

def list_directories(s):
    tab_stop = 0

    def dir_list(d):
        #global tab_stop   # wrong
        # Look for variable in the enclosing scope, not global
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1    # Increase tab before next call
                dir_list(current_dir)  # Call recursive
                tab_stop -= 1    # Move tab back after listing dir.
            else:
                print("\t" * tab_stop + f)

    #tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")

#list_directories('.idea')
list_directories(".Idea")