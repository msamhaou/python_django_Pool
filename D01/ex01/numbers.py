def read_numbers(filename):
    file = open(filename, '+r');
    line = file.readline();
    file.close();
    return line;

if __name__ == '__main__':
    line = read_numbers('numbers.txt');
    print(line, end='');

