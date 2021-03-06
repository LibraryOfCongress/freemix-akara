"""
Setup for the Django Redmine app.
"""
package_name="freemix_akara"

VERSION = __import__(package_name).__version__

from distutils.core import setup
from distutils.command.sdist import sdist
from distutils.command.build import build
import os

def write_version_file():
    f = open("%s/version.py"%package_name, "w")
    f.write('__version__ = "%s"\n' % (VERSION,))
    f.close()

def remove_version_file():
    os.remove("%s/version.py"%package_name)

class sdist_version(sdist):

    def run(self):
        write_version_file()
        sdist.run(self)
        remove_version_file()

class build_version(build):

    def run(self):
        write_version_file()
        build.run(self)
        remove_version_file()


setup(
    name = "freemix-akara",
    version = VERSION,
    description = "Akara modules for Freemix",
    keywords = "freemix akara",
    license = "License :: OSI Approved :: Apache Software License",
    author = "Uche Ogbuji",
    author_email = "uche@zepheira.com",
    url = "https://github.com/zepheira/freemix-akara",
    #Itching to rename freemix_akara to lib, but resisting that itch for the moment ;)
    package_dir={'freemix_akara': 'freemix_akara'
                    },
    packages = ['freemix_akara'],
    #include_package_data=True,
    cmdclass = {'sdist': sdist_version, 'build': build_version}
)
