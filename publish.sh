#!/bin/bash

commitMessage="Update"

if [ $# -gt 0 ]; then
    commitMessage=$1
elif [ $# -lt 1 ]; then
    echo "Enter commit message in quotes"
    exit 2
fi


echo 'commit message is: ' $commitMessage
#exit 2

#jupyter-nbconvert --to slides slides.ipynb --reveal-prefix=reveal.js
#mv slides.slides.html  index.html
#mkdir -p /tmp/workspace
#cp -r * /tmp/workspace/
#
# For git 'commit' and 'add' options, look at the following pages:
# https://git-scm.com/docs/git-commit
# https://git-scm.com/docs/git-add
echo "running git status command.."
git status
git add -A .
#git commit -am "Update"
#git checkout -B gh-pages
#cp -r /tmp/workspace/* .
#git add -A .
echo "running git status command.."
git status
#git commit -am "Update"
git commit -am "${commitMessage}"
#git push origin master gh-pages
git push origin master
#git checkout master
#rm -rf /tmp/workspace
echo "running git status command.."
git status
