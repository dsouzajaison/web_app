#Table of Contents 
* Installation Guide for linux system.
* Other Info

###Installation Guide
To use the application make sure you have python3.x installed in your system.

##### Guide to install python3.x

https://realpython.com/installing-python/

Are you set with python environment?
Then lets create a virtual environment in oder to install the project dependencies  

#####Setting Virtual Environment
To set up a virtual environment, we first need to install the package virtualenv using pip.
To do so, open up your PowerShell/Terminal and execute the following commands.

Upgrade pip to its latest version  
````cmd
python -m pip install --upgrade pip
````
Install virtualenv  

````
pip install virtualenv 
````
If your requirement falls under any of the following categories,

* have only one Python version installed
* don't want to specify any Python version
* want to use default Python version (check your version by running "python --version" on the command line)

Then, you can simply create your virtual environment using the "virtualenv venv" command, where "venv" is the environment name. 
However, if none of the above categories satisfies your requirement, then follow along as it's time to create your virtual environment using with Python 3.6. 

navigate to Desktop  
```
cd Desktop/
```
create a new directory 'project_webapp'  
````
mkdir Deskstop/Univention GmbH_web_app
````
change currenct directory to project_webapp'  
````
cd Desktop/Univention GmbH_web_app 
````
lets clone the project from github / you can also download it.
 
````
#TODO
````

####activate virtualenv

If you have it installed,create another virtual environment for the project.Type these in your terminal:
````
cd project_webapp
virtualenv venv
venv/bin/activate

````
In windows
````
venv\Scripts\activate
````
#####Install Requirements
Next, install the dependencies in the venv. From project folder run below command.
````
pip install -r requirements.txt
````
now that all the dependencies installed.Navigate to src folder.
####Run application
````
cd Univention GmbH_web_app/src/
````
Run the app with command line
````
python main.py
```` 
click the the localhost link to redirect to app webpage.
