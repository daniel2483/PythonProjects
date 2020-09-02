# pip install cx_Freeze.
# pip install idna.
# To create exe program run the command:
#   python setup.py build_exe

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Letter_Creator.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Letter_creator",
    options = options,
    version = "2.1",
    description = 'Application to create Letters for ORS and ONI',
    executables = executables,
    author='Jose Daniel Rodriguez S',
    author_email='jdrs2483@gmail.com'
)






