# Question 3: fix the problem with this script
# Question 3 extra credit: How else might this fail?

# Name changed from time.py to times.py so as not to conflict with
# time module if being run in ipython, bpython, etc. 
# sys.argv[1] is a string, and needed to be made to a float.
 
import sys
import time

def main(t):
    """This should output something like 1473539489.174058"""
    
    time.sleep(t)
    print "seconds since the epoch is %f" % time.time()

if __name__ == "__main__":

    try:
        t = float(sys.argv[1])
    except:
        t = 1

    main(t)
