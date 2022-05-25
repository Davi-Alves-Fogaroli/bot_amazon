# A bot to scrape the amazon site

## Steps to run the project:

### 1º step: 
-After unzipping the zip and opening the project in your code versioner, you will need to download the "pipenv" virtual environment
-Reference : " https://pipenv.pypa.io/en/latest/ "
- $ pip install pipenv
- $ pipenv shell
- $ pipenv install

### 2º step:
-After starting and configuring the virtual environment, you will need to download the crhomedriver in your browser's version
-Reference : " https://chromedriver.chromium.org/downloads "
-To find the version of your browser follow the step by step of the images below
-1- imagem 
-2-
-3-
-4-
-After downloading and unzipping, put your driver in the "driver" folder

### 3º step:
-Set webdriver environment variable
-In the root of the project create a file called ".env" use the file "example.env" as reference
-in ".env", create the variable "DRIVER_PATCH" and pass the relative or absolute path of your web driver (OBS: only one of the ways is enough)

### 4º step:
-With the previous steps done, open the terminal and run the following command:
$ python main.py
