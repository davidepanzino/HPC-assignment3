from distutils.core import setup
from Cython.Build import cythonize

#setup(ext_modules=cythonize("cythonfn1.pyx", compiler_directives = {"language_level": "3"})) #--List Case
setup(ext_modules=cythonize("cythonfn2.pyx", compiler_directives = {"language_level": "3"})) #--Array Case