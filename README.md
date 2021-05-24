# Provides

* Versioning through bump2version
* linting of code
* makefile 
* Documentaiton builds through sphinx
* Release to PyPi
* Run Tests

# Setup
Use 
```
cookiecutter gh:InstituteforDiseaseModeling/cookiecutter-python-library
```
to create a project from this template

## Github Actions
There are three types of github actions that are configured by default.

* Bump Version
  * For "release" branches automatically bumps the patch version for every checkin
  * Will automatically bump specified version part when a commit message containing \*\*\*BUMP \<version-part\>\*\*\* is pushed. For example: \*\*\*BUMP MINOR\*\*\* increments the minor version.
* Build/Test
  * Builds the package as a wheel file, determines that wheel file exists, installs the built wheel file, runs python tests (using pytest) in the ./tests sub-directory
  * Configured to run on ubuntu (python 3.6, 3.7, and 3.8), and windows (python 3.6)
* Build/Test/Publish
  * For "release" branches automatically publishes to staging a successfully built (and tested) package

## Setup

PYPI_STAGING_USERNAME: Username for your pypi staging user
PYPI_STAGING_PASSWORD: Password for your pypi staging user
DOCS_DEPLOY_KEY

### Docs
