import sys
import antigravity

if __name__ == '__main__':
    if (len(sys.argv) < 4):
        print('Not enough arguments')
        exit(1)
    try:
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), bytes(sys.argv[3], 'UTF-8'))
    except Exception as e:
        print(e);
        