import sys
from datetime import datetime

sys.path.insert(0, './local_lib')

from path import Path

folder = Path('dir_test')
folder.mkdir_p()

file_path = folder / 'test_file.txt'
file_path.touch()

content = "Hello from py3 " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file_path.write_text(content)

txt = file_path.read_text()

print(txt)
 