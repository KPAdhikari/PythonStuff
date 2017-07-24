#!/bin/bash

UserName=$1
RepoName=$2

#http://wiki.bash-hackers.org/commands/classictest The classing 'test' command
#    test <EXPRESSION>   [ <EXPRESSION> ]
#
#test -z $UserName && echo "Github User Name required as first param." 1>&2 && exit 1
#
#http://wiki.bash-hackers.org/commands/classictest The classing 'test' command
#
#check if minimum one parameter was given, and that one is "Hello"
#test $# -ge 1 -a "$1" = "Hello" || exit 1
#
#test $# -eq 2 && echo "Github User Name required as first param." || exit 1
#

#https://stackoverflow.com/questions/3945479/how-to-handle-missing-args-in-shell-script
if [ $# -lt 2 ]; then
    echo 1>&2 "$0: not enough arguments"
    echo "For first argument: Enter the Github User Name such as KPAdhikari or ShivaramKPA"
    echo "For seond argument: Enter repository name. If it doesn't match with the current"
    echo "                    directory name, it will fail"
    exit 2
elif [ $# -gt 2 ]; then
    echo 1>&2 "$0: too many arguments"
    exit 2
fi
# The three arguments are available as "$1", "$2", "$3"

#http://tldp.org/LDP/abs/html/comparison-ops.html
#if [ $2 -ne $someIntVar ]; then     # is to compare integers (doesn't work for string)
if [ "$2" != ${PWD##*/} ]; then
    echo "Repo name doesn't match with the current directory name."
    exit 2
elif [ "$2" == ${PWD##*/} ]; then
    echo "Congratulations! You typed the correct value of second argument for the repo. name. "
fi


#https://stackoverflow.com/questions/1371261/get-current-directory-name-without-full-path-in-a-bash-script
RepoName=${PWD##*/}          # to assign to a variable

printf '%s\n' "${PWD##*/}" # to print to stdout
# ...more robust than echo for unusual names
#    (consider a directory named -e or -n)

printf '%q\n' "${PWD##*/}" # to print to stdout, quoted for use as shell input
# ...useful to make hidden characters readable.


GithubRepo=https://github.com/${UserName}/${RepoName}.git

echo $GithubRepo


### Initialize the local repository
git init

git remote add origin https://github.com/${UserName}/${RepoName}.git

git remote -v
git remote set-url origin  https://github.com/${UserName}/${RepoName}.git

git add *



#kp: 3/4/17: Copied from https://coderwall.com/p/mnwcog/create-new-github-repo-from-command-line
#    With this, we can create a new repo in github from the command line as follows:
#       git create mynewrepo
#
#   Alternatively, we can go to github webpage itself and create the directory.
#
#    3/29/17: Actually, I need to run it as follows:
#
#     ./git-create mynewrepo
#

###  Now create the corresponding repository in github (for the given user account)
#curl -u 'KPAdhikari' https://api.github.com/user/repos -d "{\"name\":\"$repo_name\"}"
curl -u $UserName https://api.github.com/user/repos -d "{\"name\":\"$RepoName\"}"

git status

git commit -am "initial commit"

git status

git push -u origin master

git status
