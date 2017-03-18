# Update the code block below to only search directories that start with
# the letter "l" (lower case "L").

import os

start_here = '/usr'

for root, dirs, files in os.walk(start_here):
    if root.find('/l') != -1:
        print('Root is:  %s' %root)
