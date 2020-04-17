# Node-Mongo-Nginx-Docker-Project
-----
This entire project was seperated into 3 distinct sections. The first section focused on learning and creating bash and python scripts. Firstly, we created a simple game using a bash script which would take a given number, and list all numbers from 0 up until the chosen number. Next, the task was to edit the game so that if a prime number appeared in the list it would output 'Dog', a number divisible by 3 and 5 would return 'Cat & Mouse', a number divisible by 3 would return 'Cat', a number divisible by 5 would return 'Mouse', and all other numbers would just be outputted as themselves. After that, the code also had to output the total numbers of dogs, cats, mice and cat&mouse that were present in the list. Once all those tasks were completed, I was required to rewrite the bash script using python.
 #
The second section of this project involved me creating a webform application using the code from the game. As the code was relatively small and written in python, I chose to use the python module flask to develop the webform. The user was prompted to enter a number between 50 - 200 into the form and submit. Upon submitting, the python code was run in the background, and the output displayed on a results webpage in a fun and interesting way.

The third section of this project was to take the webform I had created, and change it so that instead of running using flask, it was contained and running in a node.js application, using express and pug for the webapp. The final outcome being of similar design to the webform using flask.    


## Getting Started
-----

Although this project was 3 sections, below will be the steps for running the webapp section of this project, which containes the node.js application.
 #
To get started, simply clone this git repository to a new folder on your local machine, in a location that suits you best. Please see the prerequisites section for the softwares required for this project and the deployment section for how to run the project. 

## Prerequisites
-----
Before you can run the project, the below softwares are required:

  - Python3

See below for installation instructions.

### Installing
-----
##### Python3
  
  #  
To install python3 on your local machine, simply head to your terminal and enter the below command depending on which system you are using (Mac, Linux, Windows, Ubuntu etc).
  #
For Mac systems, the homebrew module can be used to install python3 by entering the below command:
 ```
 brew install python3
```
-----
 For Windows systems, head to the python [Download Page for Windows](https://www.python.org/downloads/windows/), and select the 'latest download for windows' button followed by the 32-bit or 64-bit exe file for your system. Once the download is complete, follow the instructions to complete the installation. To check the installation was successful, head to your terminal and run the below command:
 ```
 python3 --version
```

The output should display something similar to the below:
```
Python 3.6.8
```
-----
For Ubuntu systems, you first need to run a system update before installing python3. To do this enter the below commands to complete the installation:
```
sudo apt-get update
sudo apt-get install python3
```
For Centos systems, use the yum module to install python3 in the terminal with the below command:
```
sudo yum install python3
```

Linux systems should already have python installed and this can be checked with the below command:
```
python3 --version
```

 ## Deployment
 ---
 Now that all the prerequisites are install on your machine, you can run the project. To do this, ensure you are in the folder you cloned the repository, then enter into the 'webapp' folder. Once there, run the below command in your terminal:
   ```
 sudo npm install
``` 
 This command will run the package.json file which will install all the necessary dependancies for the application to work.
 #
 Once that has completed, simply tun the below command in the terminal to start the application:
 ```
 npm run watch
```
The terminal will display "Express in running on port 5000" and if you head to your web browser and type the below, you shall see the webform page: 
To view all entries into the database, navigate to 
 ```
 https://localhost:5000
```
Here you can enter your desired number for the game, and once you hit the submit button, your results will appear!

 ## Authors
 ---
 - ##### Elizabeth Nicholl



