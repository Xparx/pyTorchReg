from setuptools import setup

DISTNAME = 'pytorchreg'
VERSION = '0.01'
DESCRIPTION = "Regularizers for pytorch models."
# with open('README.rst') as f:
#     LONG_DESCRIPTION = f.read()
MAINTAINER = 'Andreas Tjarnberg'
MAINTAINER_EMAIL = 'andreas.tjarnberg@nyu.edu'
URL = 'https://github.com/Xparx/pyTorchReg'
DOWNLOAD_URL = ''
LICENSE = 'GPL'


setup(name=DISTNAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=MAINTAINER,
      author_email=MAINTAINER_EMAIL,
      license=LICENSE,
      packages=['pytorchreg'],
      python_requires='>=3.7',
      install_requires=[
          'torch',
          'sklearn',
      ],
      zip_safe=False)
