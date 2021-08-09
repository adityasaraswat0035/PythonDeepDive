import os
import sys
p='/path/to/datafile.dat'
def process_file(path):
    with open(path) as file_handle:
        pass

try:
    process_file(p)
except OSError as e:
    print("Could not process file beacuse {}".format(str(e)),file=sys.stderr)

# if os.path.exists(p):
#     process_file(p)
# else:
#     print('No such file as {}'.format(p))