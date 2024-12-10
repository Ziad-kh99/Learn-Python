# Managing Projects in Python:
* There are many approaches to manage project in python not only one, and here I'll practice what I see convienent for me.
* NOTE: all the commands shown below depend on linux(Ubuntu).


## Regular Approache (venv/pip):

### 1. Create Virtual Environment':
* We can create virtual environment using 'venv'.
    * Note that you may need to install 'venv' if it's not installed by default:
        - apt install python3.12-venv

* To create virtual environment:
    - python -m venv <project_name-venv>

* To activate virtual environment:
    - source <project_name-venv/bin/activate> 

* To deactivate virtual environment:
    - deactivate 

* Note that any packages installed inside virtual environment will be available only within it.


### 2. Install Packages:
#### Using pip:
* There are many packages manager available we could use.
* The most popular one and usually installed by with python in 'pip' (Package Installer for Python).
* Using 'pip' you can install, uninstall, upgrade, and fetch for packages.
* 'pip' install packages from 'pypi' (Python Package Index).

##### pip commands:
* To install pip:
    - python -m ensurepip --upgrade
* To check pip version:
    - pip --version
* To list installed packages:
    - pip list
* To get info about a specific package:
    - pip show <package-name>
* To install package:
    - pip install <package-name>


## ANACONDA:
* Anaconda is another approach we can use to manage our projects and virtual environments.
