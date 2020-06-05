import sys
import os

dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(dir_path)

def main():
    from simulation.simulation import test
    test()

if __name__ == '__main__':
    main()
