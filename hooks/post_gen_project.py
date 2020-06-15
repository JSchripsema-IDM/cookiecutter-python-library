import os
import shutil

docs = True if "{{cookiecutter.docs}}".lower()[0] == "y" else False
linting = True if "{{cookiecutter.linting}}".lower()[0] == "y" else False


if not linting:
    print('Removing linting')
    os.remove(os.path.join('.github', 'workflows', 'lint.yml'))

if not docs:
    print('Removing docs')
    os.remove(os.path.join('.github', 'workflows', 'publish-documentation.yml'))
    os.remove(os.path.join('.github', 'workflows', 'build-docs.yml'))
    shutil.rmtree('docs')

print("""
The next thing to do is 
1. Add current project to github
    git add .
    git commit -m "Initial version of library"
    git push 
2. In github, configure your secrets for PYPI_STAGING_USERNAME, PYPI_STAGING_PASSWORD, and DOCS_DEPLOY_KEY if you
    enabled docs.
3. If you enabled docs, you need to then
    git checkout --orphan gh-pages
    create an empty file called .nojekyll
    git add .nojekyll
    git commit -m "First commit of docs"
    git push
    git checkout master
4.  Now you are ready to begin using your repo. Github actions have been enabled for linting(optional), docs(optional),
    packaging and publishing. To publish to IDM's production pypi server, you need to provide a basic suite of tests
""")
