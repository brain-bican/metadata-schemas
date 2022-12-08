[![Tests](https://github.com/AllenInstitute/python_cicd_template/actions/workflows/tests.yaml/badge.svg)](https://github.com/AllenInstitute/python_cicd_template/actions/workflows/tests.yaml)
# How to use this repository as a template
Click the green "Use this template" button at the top of the page.  
This will create a new repository with the same contents as this one.  
You can then clone that repository and start working on your own project.

## Getting started

### Tweaks to readme.md
The Tests badge URL will need to be updated to match your template repository URL like this:
* https://github.com/<your_account_name>/<your_repo_name>/actions/workflows/tests.yaml/badge.svg
* https://github.com/<your_account_name>/<your_repo_name>/actions/workflows/tests.yaml

## Tweaks to pyproject.toml
The following attributes need updating in pyproject.toml:
```tmol
[project]
name = ...
descrption = ...
authors = ...
classifiers = ...

[project.urls]
repository = "https://github.com/<your_account_name>/<your_repo_name>"

[project.scripts]
<your_script_name> = "<your_package_name><your_module_name>:<your_function_name>"
```

## Tweaks to project folders
The following folders need to be renamed to match your project name:
* `src/<your_package_name>`

## Tweaks to tests
In your tests you need to import from your package name instead of `example_pkg`:
```python
from example_pkg import ExampleClass, example_function
# change to 
from your_package_name import ExampleClass, example_function
```

## Install a virtual environment
```bash
python -m pip install --upgrade pip
python -m pip install virtualenv
python -m virtualenv venv
```
## Activate your virtual environment
### Mac/Linux:
```bash
source ./venv/bin/activate
```
### Windows:
```bash
.\venv\Scripts\activate
```

## Install the package
```bash
# install the package in editable mode
pip install -e .
# install development dependencies
pip install -r requirements-dev.txt
```
## setup pre-commit
```bash
pre-commit install
````

## Run tests
```bash
pytest
```
