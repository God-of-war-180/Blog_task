# Blog_task

read me file

Steps to run the project
Clone the repository
Create a virtual environment using command python3 -m venv env
Activate virtual enviornment using command

# for Linux
source env/bin/activate

# for Windows
env/Source/activate

Install the dependencies using command : 
	
	pip install -r requirements.txt

Type source env/bin/activate

Run the server using command:

	python manage.py makemigrations

Then run the server using command: 

	python manage.py migrate

Finally run the server using command: 

	python manage.py runserver
	
kindly add "modheader" extention to authentication :
	https://chrome.google.com/webstore/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj

create a user from and get access token from 

    http://127.0.0.1:8000/auth/users/

example:

{
    "username": "user1",
    "email": "user1@gmail.com",
    "password": "password123"  #password should conatain minimum of 8 characters
}

create a jwt token by using:

    http://127.0.0.1:8000/auth/jwt/create

{
    "username": "user1",
    "password": "password123"
}


enter the credentials and get the 'access token'.


go to "mode header extention " > "requestheaders" and enter those access tokens with the prefix of JWT


Authorization   and JWT & value

and refresh you will get to the authenticated website.




