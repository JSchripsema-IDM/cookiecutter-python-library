import os
import shutil

docs = True if "{{cookiecutter.docs}}".lower()[0] == "y" else False
linting = True if "{{cookiecutter.linting}}".lower()[0] == "y" else False


if not linting:
    print('Removing linting')
    os.remove(os.path.join('.github', 'workflows', 'lint.yml'))

if not docs:
    print('Removing docs options, including github actions, read the docs, and the docs tree')
    os.remove(os.path.join('.github', 'workflows', 'build-docs.yml'))
    os.remove('.readthedocs.yml')
    shutil.rmtree('docs')

print("""
The next thing to do is 
1. Add current project to github
    git add .
    git commit -m "Initial version of library"
    git push 
2. In github, configure your secrets for PYPI_STAGING_USERNAME, PYPI_STAGING_PASSWORD, and DOCS_DEPLOY_KEY if you
    enabled docs.
3.  Now you are ready to begin using your repo. Github actions have been enabled for linting(optional), docs(build only),
    packaging and publishing. To publish to IDM's production pypi server, you need to provide a basic suite of tests
""")
