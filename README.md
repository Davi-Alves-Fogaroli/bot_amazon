# A bot to scrape the amazon site

## Steps to run the project: " https://github.com/Davi-Alves-Fogaroli/bot_amazon/blob/main/README.md "

### 1º step: 
-After unzipping the zip and opening the project in your code versioner, you will need to download the "pipenv" virtual environment
-Reference : " https://pipenv.pypa.io/en/latest/ "
- $ pip install pipenv
- $ pipenv shell
- $ pipenv install
- $ pipenv lock

### 2º step:
-After starting and configuring the virtual environment, you will need to download the crhomedriver in your browser's version
-Reference : " https://chromedriver.chromium.org/downloads "
-To find the version of your browser follow the step by step of the images below

![image](https://user-images.githubusercontent.com/61630258/170256891-c7cdcf28-6f35-4765-891c-64ef388c2182.png)

![image](https://user-images.githubusercontent.com/61630258/170257075-632d6097-9768-41e3-a35e-cc29492da081.png)

![image](https://user-images.githubusercontent.com/61630258/170257175-f8e02982-8de8-4e00-9294-6e04b4496000.png)

![image](https://user-images.githubusercontent.com/61630258/170257210-bcd4bfd1-5c0b-4378-9704-77dd3b7d6fb3.png)

-After downloading and unzipping, put your driver in the "driver" folder

### 3º step:
-Set webdriver environment variable
-In the root of the project create a file called ".env" use the file "example.env" as reference
-in ".env", create the variable "DRIVER_PATCH" and pass the relative or absolute path of your web driver (OBS: only one of the ways is enough)

### 4º step:
-With the previous steps done, open the terminal and run the following command:
- $ python main.py
