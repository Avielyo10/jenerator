# Jenkins Plugin Generator
![](https://img.shields.io/badge/version-2.0-blue.svg)
![](https://img.shields.io/badge/license-Apache--2.0-brightgreen.svg)
![](https://img.shields.io/badge/requirements-python--3.6-red.svg)

# Installation

1. `pip install virtualenvwrapper`

2. `mkvirtualenv -p python3 venv`

3. `workon venv`

4. `pip install git+https://github.com/Avielyo10/jenerator`

# Usage
<pre>
Usage: jenerator [OPTIONS] COMMAND [ARGS]...

  Jenkins Plugin Generator - creates fast templates of jenkins plugins

Options:
  --help  Show this message and exit.

Commands:
  all        Creates it all
  builder    Creates build step
  installer  Creates tool-installation & installer
  publisher  Creates post-build action
  util       Creates utility class with helpful methods
  wrapper    Creates wrapper - build environment to install the tool if necessary
</pre>

# Jenerator 2.0 Release Notes
## March 10, 2019 

## New Features & Improvements
* **Using Python 3** - Since the End Of Life date (EOL, sunset date) for Python 2.7 is comming closer  (01/2020)  I decided to move to Python 3.  See also PEP 466.

* **New CLI** - Using Click to create a beautiful command line interface instead of the writing it on my own as in the previous version.
* **Packaged Version** - Now you can install this tool using pip! While this library is certainly able to be distributed via PyPI, I decided not to it for now.




