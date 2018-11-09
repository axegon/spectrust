import sys
import os
import shutil
from codecs import open
from subprocess import Popen
from setuptools import setup


try:
    Popen(["cargo", "--version"])
    print("Running Rust installation found.")
except FileNotFoundError:
    sys.exit("""
    It appears you don't have a running Rust nightly instalation.
    please visit https://www.rust-lang.org/en-US/install.html""")

cwd = os.path.abspath(os.path.dirname(__file__))

# A bit less of a hassle than using pyo3-pack, considering both projects are young...
Popen(["cargo", "build", "--manifest-path", "{}/spectrust/_spectro/Cargo.toml".format(cwd), "--release"]).communicate(
    "")

shutil.copy("{}/spectrust/_spectro/target/release/lib_spectro.so".format(cwd), "{}/spectrust/_spectro.so".format(cwd))

about = {}
with open(os.path.join(cwd, 'spectrust', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=['spectrust'],
    package_data={'': ['NOTICE'], "spectrust": ["*.so"]},
    package_dir={'spectrust': 'spectrust'},
    include_package_data=True,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Rust"
    ],
)
