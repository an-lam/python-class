# Python code to demonstrate
# conversion of nested dictionary
# into flattened dictionary

# code to convert ini_dict to flattened dictionary
# default seperater '_'
def flatten_dict(dd, separator='_', prefix=''):
    return {prefix + separator + k if prefix else k: v
            for kk, vv in dd.items()
            for k, v in flatten_dict(vv, separator, kk).items()
            } if isinstance(dd, dict) else {prefix: dd}


# initialising_dictionary
ini_dict = {'geeks': {'Geeks': {'for': 7}},
            'for': {'geeks': {'Geeks': 3}},
            'Geeks': {'for': {'for': 1, 'geeks': 4}}}

# priniting initial dictionary
print("initial_dictionary", str(ini_dict))

# printing final dictionary
print("final_dictionary", str(flatten_dict(ini_dict)))
