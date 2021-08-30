kp: 8/8/21, From: https://docs.beeware.org/en/latest/tutorial/tutorial-0.html

Before starting to work here, always activate the virtual
environment with "source beeware-venv/bin/activate"




===========
$ mkdir beeware-tutorial
$ cd beeware-tutorial
$ python3 -m venv beeware-venv
$ source beeware-venv/bin/activate

If this worked, your prompt should now be changed - it should have a (beeware-venv) prefix. This lets you know that you’re currently in your BeeWare virtual environment. Whenever you’re working on this tutorial, you should make sure your virtual environment is activated. If it isn’t, re-run the last command (the activate command) to re-activate your environment.

Alternative virtual environments

If you’re using Anaconda or miniconda, you may be more familiar with using conda environments. You might also have heard of virtualenv, a predecessor to Python’s built in venv module. As with Python installs - it doesn’t matter how you create your virtual environment, as long as you have one.

Even then - strictly speaking, using a virtual environment is optional. You can install BeeWare’s tools directly into your main Python environment. However, it’s really, really, really recommended that you use a virtual environment.
