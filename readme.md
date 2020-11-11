### Authentication window for users

Call the login page with

`/login?user_id=1`

where user_id is the id of the project that has an account.

the user will attempt to login with his username and password.
if he has a valid account under the project with ID == user_id
will receive authentication token and redirectURL.

redirectURL is the url of the project that needs authentication.


### Running the server:

`python3 server.py` will run in development mode by default

`python3 server.py -env=prod` will run in production mode


### Connection with the GO auth service

live GO auth service at: https://verte-auth-server.herokuapp.com/
