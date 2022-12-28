<h1 align='center'>Python Package Structure</h1>

<h6 align='center'>This contains a template for structuring python packages. <a target='_blank' href='https://docs.python-guide.org/writing/structure/'>Learn more.</a></h6>

![Tests](https://github.com/prashantrahul141/Python-Package-Structure/actions/workflows/tests.yaml/badge.svg)

## This covers:

- Structuring python packages
- Using sub modules to separate code
- Importing submodules
- Importing resources like images
- Testing (pytest, mypy)
- Linting (flake8)
- Github actions with tox

<br>

## Some useful commands:

Building package

```sh
# first make sure build is installed and updated
pip install --upgrade build

# then run the build command
python -m build
```

Install user dependencies

```sh
pip install -r requirements.txt
```

Install dev dependencies

```sh
pip install -r requirements_dev.txt
```

Install the package locally in editable mode

```sh
pip install -e .
```

run pytest to run your tests

```sh
pytest
```

run flake8 to test linting

```sh
flake8
```

get a cool `test:status` badge on your readme :D

```
![Tests](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/<WORKFLOW_FILE>/badge.svg)
```
