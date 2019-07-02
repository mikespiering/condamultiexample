import sys
import numpy as np

def numpty_dumpty():
    sys.stdout.write("Hello world\n")
    a = np.array([1,5])
    np.savetxt(sys.stdout, a, fmt='%.i')


if __name__ == '__main__':
    numpty_dumpty()
