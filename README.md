# LightFeather.io Coding Challenge 
Author: Joseph Ashley <br>
Date: 2021-09-16 

## Prerequisites
Before beginning, first check that python 3 is installed.
```
$ python3 -V
Python 3.8.10
```
Likewise we should check to see if the python package virtualenv is installed. If not, install it like so.
```
$ pip freeze | grep "virtualenv"
virtualenv==20.7.2
# Otherwise...
$ pip install virtualenv
```

## Installation
Start off by creating a new virtual environment, here I am calling it 'test_env'.
```
$ python3 -m venv test_env
$ cd test_env && source bin/activate
(test_env)$ 
```
Once in the virtual environment, clone this repository and move the source files into our working directory
```
(test_env)$ git clone https://github.com/joeashley/code_challenge.git
(test_env)$ mv code_challenge/* .
```
And lastly, install any unmet dependencies by running:
```
(test_env)$ pip install -r requirements.txt
```
## Usage
Run the files as shown below. You will probably want to run them each in different windows in order to catch the output from both sides of the application.
```
(test_env)$ python3 api.py
(test_env)$ python3 form.py
```
<br>

![image](https://user-images.githubusercontent.com/31110789/133693792-d355d3ce-0b89-4fdf-aecd-ca4b6d7f53a6.png)

<br>
Then navigate to http://127.0.0.1:5000 to view the application
<br><br>

![image](https://user-images.githubusercontent.com/31110789/133693256-ed746763-b3a3-4e44-afcb-6abee70622e5.png)

<br>
On successful submission, the console will look like so:
<br><br>

![image](https://user-images.githubusercontent.com/31110789/133693674-63ab49b1-f08a-4217-abc5-84883d073dfc.png)

<br>
