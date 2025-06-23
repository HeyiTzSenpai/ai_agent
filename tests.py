import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

calc_dir = os.path.abspath("calculator")
pkg_dir = os.path.join(calc_dir, "pkg")
main_dir = os.path.join(calc_dir, "main.py")
pkg_calculator_dir = os.path.join(calc_dir, "pkg/calculator.py")
lorem_txt_dir = os.path.join(calc_dir, "lorem.txt")
morelorem_txt_dir = os.path.join(calc_dir, "pkg/morelorem.txt")



print(write_file(calc_dir, lorem_txt_dir, "wait, this isn't lorem ipsum"))
print(write_file(calc_dir, morelorem_txt_dir, "lorem ipsum dolor sit amet"))
print(write_file(calc_dir, "/tmp/temp.txt", "this should not be allowed"))




#print(get_files_info(calc_dir, calc_dir))
#print(get_files_info(calc_dir, pkg_dir))
#print(get_files_info(calc_dir, "/bin"))
#print(get_files_info(calc_dir, os.path.abspath(os.path.join(calc_dir, "../"))))

#print(get_file_content(calc_dir, main_dir))
#print(get_file_content(calc_dir, pkg_calculator_dir))
#print(get_file_content(calc_dir, "/bin/cat"))