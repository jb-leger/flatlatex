"""Setup script for flatlatex

Based on `sampleproject`, see:
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the __init__.py file

###
# c'est toi qui extrait la doc comme ca ? sinon to peux exec' the module et
# garder le `__doc__`, tu peux en profiter pour attraper le `__version__` en
# meme temps.
###
with open(path.join(here, 'flatlatex', '__init__.py'), encoding='utf-8') as f:
    ast = compile(f.read(), '__init__.py', 'exec')
    fake_global = {'__name__': '__main__'}
    try:
        exec(ast, fake_global)
    except (SystemError, ImportError) as e:
        print('System error')

    long_description = fake_global['__doc__']
    version = fake_global['__version__']


setup(
    name='flatlatex',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='A LaTeX math converter to unicode text',
    long_description=long_description,

    # The project's main homepage.
    url='https://gitlab.crans.org/leger/flatlatex',

    # Author details
    author='Jean-Benoist Leger',
    author_email='jb@leger.tf',

    # Choose your license
    license='BSD-2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Markup :: LaTeX',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
    ],

    # What does your project relate to?
    keywords='latex math unicode',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['regex'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['pytest'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    python_requires='>=3',

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
    },
)
