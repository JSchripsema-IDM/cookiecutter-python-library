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
     git add .bumpversion.cfg .dev_scripts/ .github .gitignore .readthedocs.yml *
     git commit -m "Initial version of library"
     git push 
    
   You will need to create a repository on Github, https://github.com/new
   Once you have created it, you need to add it as a remote
     git remote add origin <repo url>
    
2. In github, configure your secrets for PYPI_STAGING_USERNAME and PYPI_STAGING_PASSWORD. These credentials allow you to push packages to a
   pypi the configured staging pypi registry. For IDM repo's, it is recommended to work with test to setup a project account. Alternatively, you
   can use your own idm email and password. Just remember you will need to update the password here when you change it.
   
3.  Now you are ready to begin using your repo. Github actions have been enabled for linting(optional), docs(build only),
    packaging and publishing. To publish to IDM's production pypi server, you need to provide a basic suite of tests
    
4. Start development. See README.txt for setup instructions
""")
