## Table of Contents 
* [Installation](#Installation)
* [Project-info](#Project-Info)

### Installation
To use the application make sure you have python3.x installed in your system.

##### Guide to install python3.x

https://realpython.com/installing-python/

Are you set with python environment?
Then lets create a virtual environment in oder to install the project dependencies  

##### Setting Virtual Environment
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
create a new directory 'Univention_GmbH_web_app'  
````
mkdir Deskstop/Univention GmbH_web_app
````
change currenct directory to 'Univention_GmbH_web_app'
````
cd Desktop/Univention_GmbH_web_app 
````
lets clone the project from github / you can also download it.
 
````
git clone https://github.com/dsouzajaison/web_app.git
````

#### activate virtualenv

If you have it installed,create another virtual environment for the project.Type these in your terminal:
````
cd Univention_GmbH_web_app
virtualenv venv
venv/bin/activate

````
In windows
````
venv\Scripts\activate
````
##### Install Requirements
Next, install the dependencies in the venv. From project folder run below command.
````
pip install -r requirements.txt
````
now that all the dependencies installed.Navigate to src folder.
#### Run application
````
cd Univention_GmbH_web_app/src/
````
Run the app with command line
````
python main.py
```` 
click the the localhost link to redirect to app webpage.

## project-Info

The framework I have used in Flask since it is one of the most used framework and quite direct. The database used here is filebased system.
TinyDb is a NOSQL database and simple for storing and retrieving data. This makes application light and no need to have a server always running.
ofcourse it could be implemented in sqlite3 or so.

PS: If any improvements are necessary or the task has not met the requirements , always open for suggestions.