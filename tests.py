import os
from functions.get_files_info import get_files_info

calc_dir = os.path.abspath("calculator")
pkg_dir = os.path.join(calc_dir, "pkg")



print(get_files_info(calc_dir, calc_dir))
print(get_files_info(calc_dir, pkg_dir))
print(get_files_info(calc_dir, "/bin"))
print(get_files_info(calc_dir, os.path.abspath(os.path.join(calc_dir, "../"))))