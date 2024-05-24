import settings
import sys

def open_file(file) :
    try:
        return open(file, 'r');
    except:
        print("file opening failed");
        exit(1);
    pass

if (len(sys.argv) < 2):
    exit(0);
extension = ".template"
if (sys.argv[1].find(extension, len(sys.argv[1]) - len(extension)) == -1):
    print("FILE IS NOT .template");
    exit(1);

infile = open_file(sys.argv[1]);
    
# line = infile.read()
# print(line.format(**vars(settings)))

for line in infile:
    print(line)


    
# print(sys.argv[1][0:-len(extension)]);

