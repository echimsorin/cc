# Let's get the back-end running!

## Prerequisites

### (You should already have most of this set up during training)

1. Install Python (we are using [Python 3.9](https://www.python.org/downloads/release/python-396/))

1. Install an Integrated Development Environment (IDE). I recommend [PyCharm](https://www.jetbrains.com/pycharm/)
   or [VSCode](https://code.visualstudio.com/).

1. Install [MySQL Workbench](https://www.mysql.com/products/workbench/) and have a local MySQL connection running. This
   is your local database which allows you to test your app locally.

## Fill up your Local Database

1. Open MySQL Workbench, create or select your local MySQL database connection.

1. Open a new query editor (Ctrl + T) in MySQL Workbench, then copy and paste the code from
   _python-api/resources/data_load.sql_ into the query editor and execute all the statements (Ctrl + Shift + Enter)

1. Verify that you have data in your database by running some select queries:

   ```
   use pets;
   select * from dogs;
   ```

1. To make sure your app can find the local database, set the connection details in the
   _/python-api/app/\_\_init\_\_.py_
   file under the part 'For local execution' to match your local database settings (check the port, username, and
   password match your local database).

## Run your back-end locally

1. Open a terminal \
   Pycharm: Alt + F12
   (or just click the 'Terminal' tab at the bottom of your IDE) \
   VSCode: Use Command Prompt (CMD). This can be found by searching for 'command prompt' in the Windows start menu.

1. Inside your terminal, enter the commands below. It's worth knowing what exactly each command here is doing. If you
   don't, google it or ask a trainer.

1. Go into the directory that stores the backend code using cd. \
   Pycharm Terminal:
   ```   cd python-api   ```
   CMD:
   Use the full path to the skeleton\python-api folder. You can right click and 'copy path' from the file explorer.
   Replace the path in the same command, like:
   ```
   cd C:\Users\You\...\python-api
   ```
   You should see that the path in the terminal updated to the python-api folder.

1. Create a Python virtual environment:
   ```
   python -m venv env
   env\Scripts\activate
   ```
   You should see "(env)" before the path in the terminal now. This signifies that you are using the virtual
   environment.

1. Install the libraries for this project in your virtual environment:
   ```
   pip install -r requirements.txt
   ```

1. Start the backend code:
   ```
   python run.py
   ```

## Explore the API you just created

1. Go to localhost:5000/dogs/. Hopefully, you will see the api response that has retrieved the dogs data from the
   database as a JSON.

1. You can also access localhost:5000/swagger-ui/ which displays swagger documentation about the API.

1. Now go set up your front-end to interact with this API.

## Deactivating and reactivating the Virtual Environment

1. To deactivate the virtual environment, just do:
   ```
   deactivate
   ```

1. Once the virtual environment has been created in the steps above, you don't need to create it again (hopefully!). You
   just have to reactivate it to be able to spin up your local back-end server again. To do this, just ``` cd``` into
   the python-api folder and run
   ```
   env\Scripts\activate
   ``` 
