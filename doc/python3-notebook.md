# ipython notebook with python3 on Ubuntu14.04

- Install prerequisities as root:
```
# install curl virtualenvwrapper
apt-get install -y curl virtualenvwrapper

# install as workaround for https://github.com/matplotlib/matplotlib/issues/3029/
apt-get install -y pkg-config

# install python development packages and g++
apt-get install -y python3-dev g++

# install dependencies for scipy
apt-get install -y libblas-dev liblapack-dev gfortran

# install some dependencies for matplotlib
apt-get install -y libfreetype6-dev libpng-dev libjpeg8-dev
```
- create and activate virtualenv
```
# create and activate virtual environment  (env name is jupnb)
# logout & relogin
mkvirtualenv --no-setuptools --python /usr/bin/python3 jupnb 

# install fresh pip
curl https://bootstrap.pypa.io/get-pip.py | python

# install fresh setuptools
pip install setuptools distribute

# install numpy as it is dependecy for many others
pip install numpy

# install scientific packages (seaborn instead of matplotlib for pretty plots)
pip install sympy scipy seaborn pandas jupyter

# install scikit-learn separately, it depends on numpy and scipy
pip install scikit-learn

# deactivate env
deactivate

# activate virtual env
workon jupnb
```

- Configure notebook profile
```
mkdir -p ~/.jupyter
cd ~/.jupyter
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout jupnb.key -out jupnb.pem
echo "c.NotebookApp.ip = '*'" >> jupyter_notebook_config.py
echo "c.NotebookApp.port = 8888" >> jupyter_notebook_config.py
echo "c.NotebookApp.open_browser = False" >> jupyter_notebook_config.py
echo "c.NotebookApp.password = u'$(ipython -c 'from notebook.auth import passwd; print(passwd())')'" >> jupyter_notebook_config.py
echo "c.NotebookApp.certfile = u'$HOME/.jupyter/jupnb.pem'" >> jupyter_notebook_config.py
echo "c.NotebookApp.keyfile = u'$HOME/.jupyter/jupnb.key'" >> jupyter_notebook_config.py
echo "c.NotebookApp.cookie_secret_file = '$HOME/.jupyter/secret_cookie'" >> jupyter_notebook_config.py
cp ~/.jupyter/jupnb.pem .
cd -
```
- run server and open https://127.0.0.1:8888/ in your browser:
```
jupyter notebook
```

- Reference
  - http://bikulov.org/blog/2015/11/07/install-jupyter-notebook-and-scientific-environment-in-ubuntu-14-dot-04-with-python-3/
