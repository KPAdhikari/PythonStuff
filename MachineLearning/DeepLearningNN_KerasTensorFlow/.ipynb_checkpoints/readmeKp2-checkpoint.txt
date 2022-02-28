For some reason, I couldn't get the virtual env 'kerasenv' (which I had created from the regular terminal outside of the jupyter lab) 
working on the jupyter notebook despite trying to use ideas from https://www.zainrizvi.io/blog/jupyter-notebooks-best-practices-use-virtual-environments/. Even using some ideas found in https://stackoverflow.com/questions/57422648/no-module-named-ipykernel-launcher didn't help.

So, I am trying again, this time with a rather clean slate - starting with the virtual env created from the terminal opened inside 
this 'jupyter lab' (actually, I am opening and editing this file itself using the jupyter lab - one tab has the 'terminal', another tab is this file; later on I will have at least the jupyter notebook where I will try to use keras and tensorflow etc using the virtual environment 'env4keras' which I created from this "in-house" (meaning the one opened inside the jupyter-lab) terminal with the following command (as suggested in the above mentioned site i.e. https://www.zainrizvi.io/blog/jupyter-notebooks-best-practices-use-virtual-environments/)


python3 -m venv env4keras --system-site-packages

Here is what I did and what I saw in the terminal
########################
kpadhikari@MyMacs-MacBook-Air:~/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow$ python3 -m venv env4keras --system-site-packages
kpadhikari@MyMacs-MacBook-Air:~/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow$ ll
total 16
drwxr-xr-x  6 kpadhikari  staff   192B Feb  5 00:08 env4keras
drwxr-xr-x  7 kpadhikari  staff   224B Jan 31 00:30 kerasenv
-rw-r--r--  1 kpadhikari  staff   1.3K Feb  4 01:35 my_first_Keras_Tensorflow_notebook.ipynb
-rw-r--r--  1 kpadhikari  staff   388B Jan 31 00:24 readmeKp.txt
kpadhikari@MyMacs-MacBook-Air:~/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow$ du -sh *
 15M    env4keras
471M    kerasenv
4.0K    my_first_Keras_Tensorflow_notebook.ipynb
4.0K    readmeKp.txt
kpadhikari@MyMacs-MacBook-Air:~/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow$ source myenv/bin/activate
bash: myenv/bin/activate: No such file or directory
kpadhikari@MyMacs-MacBook-Air:~/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow$ source env4keras/bin/activate
(env4keras) kpadhikari@MyMacs-MacBook-Air:~/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow$ which python
/Users/kpadhikari/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow/env4keras/bin/python
(env4keras) kpadhikari@MyMacs-MacBook-Air:~/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow$ python -m ipykernel install --user --name=env4keras
Installed kernelspec env4keras in /Users/kpadhikari/Library/Jupyter/kernels/env4keras
(env4keras) kpadhikari@MyMacs-MacBook-Air:~/GitStuff/KPAdhikari/PythonStuff/MachineLearning/DeepLearningNN_KerasTensorFlow$ 
########################