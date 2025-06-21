import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

calc_dir = os.path.abspath("calculator")
pkg_dir = os.path.join(calc_dir, "pkg")
main_dir = os.path.join(calc_dir, "main.py")
pkg_calculator_dir = os.path.join(calc_dir, "pkg/calculator.py")




#print(get_files_info(calc_dir, calc_dir))
#print(get_files_info(calc_dir, pkg_dir))
#print(get_files_info(calc_dir, "/bin"))
#print(get_files_info(calc_dir, os.path.abspath(os.path.join(calc_dir, "../"))))

print(get_file_content(calc_dir, main_dir))
print(get_file_content(calc_dir, pkg_calculator_dir))
print(get_file_content(calc_dir, "/bin/cat"))