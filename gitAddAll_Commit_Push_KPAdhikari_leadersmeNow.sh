#!/bin/bash

commitMessage="Update"

if [ $# -gt 0 ]; then
    commitMessage=$1
elif [ $# -lt 1 ]; then
    echo "Enter commit message in quotes"
    exit 2
fi

echo 'commit message is: ' $commitMessage
echo ''
echo ''
echo ''
echo "========= Next I am executing 'git status' for adding all.======'"
echo ''
echo ''
echo ''

#exit 2

#jupyter-nbconvert --to slides slides.ipynb --reveal-prefix=reveal.js
#mv slides.slides.html  index.html
#mkdir -p /tmp/workspace
#cp -r * /tmp/workspace/
#
# For git 'commit' and 'add' options, look at the following pages:
# https://git-scm.com/docs/git-commit
# https://git-scm.com/docs/git-add
#echo "running git status command.."
git status
echo ''
echo ''
echo ''
echo "========= Next I am executing 'git add -A' for adding all.======'"
echo ''
echo ''
echo ''
git add -A .
#git commit -am "Update"
#git checkout -B gh-pages
#cp -r /tmp/workspace/* .
#git add -A .
echo ''
echo ''
echo ''
echo "========= Next I am executing 'git status' again.======'"
echo ''
echo ''
echo ''
#echo "running git status command.."
git status

echo ''
echo ''
echo ''
echo "========= Next running 'git commit -am commitMessage' for adding all.======'"
echo ''
echo ''
echo ''
#git commit -am "Update"
git commit -am "${commitMessage}"

echo ''
echo ''
echo ''
echo "========= Finally running 'git push origin master' for adding all.======'"
echo ''
echo ''
echo ''
#git push origin master gh-pages
git push origin master
#git checkout master
#rm -rf /tmp/workspace

sleep 1s #units: s, m, h, d for sec (default), min, hour, day, so 4 = 4s
#printf "\n\n\n\"
echo -e "\n\n\n\n running 'git status' command.. \n\n"

git status
