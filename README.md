# LightFeather.io Coding Challenge 
Author: Joseph Ashley <br>
Date: 2021-09-16 

## Prerequisites
Verify python is installed
```
$ python3 -V
Python 3.8.10
```
Check if virtualenv is already installed
```
$ pip freeze | grep "virtualenv"
virtualenv==20.7.2
```
If not, install it
```
$ pip install virtualenv
```

## Installation
Start off by creating a new virtual enviroment 'test_env' (or whatever).
```
$ python3 -m venv test_env
$ cd test_env && source bin/activate
(test_env)$ 
```
Clone the repository and move the files into our working directory
```
(test_env)$ git clone https://github.com/joeashley/code_challenges.git
(test_env)$ mv code_challenges/* .
```
Install dependencies
```
(test_env)$ pip install -r requirements.txt
```
## Usage
Run the files as shown below. You will probably want to run them each in different windows in order to catch the output from both sides of the application.
```
(test_env)$ python3 api.py
(test_env)$ python3 form.py
```
![image](https://user-images.githubusercontent.com/31110789/133693792-d355d3ce-0b89-4fdf-aecd-ca4b6d7f53a6.png)
<br><br>
Then navigate to http://127.0.0.1:5000 to view the application
<br>
![image](https://user-images.githubusercontent.com/31110789/133693256-ed746763-b3a3-4e44-afcb-6abee70622e5.png)
<br><br>
On successful submission, the console will look like so:
<br>
![image](https://user-images.githubusercontent.com/31110789/133693674-63ab49b1-f08a-4217-abc5-84883d073dfc.png)
<br>
