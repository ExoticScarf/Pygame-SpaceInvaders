import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python36\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("A Bit Racey.py")]

cx_Freeze.setup(
    name = "A Bit Racey",
    options = {"build_exe": {"packages": ["pygame"], "include_files": ["CarSprite.png"]}},
    executables = executables,
    version = "1.0.0"
)
