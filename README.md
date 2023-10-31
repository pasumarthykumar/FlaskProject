# Building a RESTful API with Flask - Error Handling, Authentication,and File Handling with Public and Admin Routes


Project Team Members :
Pavan Kumar Pasumarthy(CWID : 885153056),

# Project Description 

The primary objective of this project is the creation of a highly functional RESTful API using the Flask framework. Noteworthy attributes encompass a robust error-handling mechanism, dependable JWT (JSON Web Token) authentication to ensure secure user interactions, and a secure approach to handling files, which involves rigorous checks on file types and sizes. It serves as a foundational model in Python for building Flask APIs, integrating these critical components, and includes a comprehensive readme to facilitate the setup and deployment process. This renders it an invaluable asset for the development of web and mobile applications.

#Drive Link For the Project Demonstration and Screenshots
Prior to commencing, it's essential to ensure that you fulfill the following prerequisites:

Python (3.6 or a newer version) must be installed on your system.
Follow these steps to create a Python virtual environment for the purpose of isolating the application's dependencies:

Execute the following command to generate a Python virtual environment:

python -m venv venv
Activate the virtual environment by running:


source venv/bin/activate
Use the following pip command to install the mandatory packages:


pip install Flask flask_sqlalchemy pymysql
Configuration:

Open the Flask application file (app.py) and ensure proper configuration of the subsequent settings:

SECRET_KEY: This must be configured with a confidential key for your application.
SQLALCHEMY_DATABASE_URI: Configure this with the accurate URI for your MySQL database.
Running the Application:

In the command line interface, navigate to the project directory where the app.py file is situated. Initiate the Flask application using the ensuing command:

flask run

The application will be accessible by entering http://localhost:5000 in your web browser.

Accessing the Application:

Once the application is operational, you can reach it by launching your web browser and going to http://localhost:5000.


Error Handling:

The Flask application manages custom error handling for a range of HTTP error codes, including:
	404 (Not Found)
	401 (Unauthorized)
	400 (Bad Request)
	500 (Internal Server Error)
	403 (Forbidden)
	422  (Unprocessable Entity)
	429  (Too Many Requests)

Authentication:

The Flask application offers a user authentication system that relies on JSON Web Tokens (JWT).
Access to the following routes is provided:
	*/login (POST) - This route is utilized for logging in by providing a username and password. In the case of valid credentials, it will furnish a JWT access token.
	*/protected (GET) - This route is safeguarded and mandates the presence of a valid JWT token. To gain access, you must include the JWT token within the request header.
For testing the application, you can employ tools like Postman or cURL to transmit HTTP requests that include JWT tokens.
Application Configuration:
	*The secret key used for JWT tokens is configured within the app.config['JWT_SECRET_KEY'] variable. In a production setting, it is advisable to replace it with your secret key.
	*The user authentication process in this example is designed for simplicity, and in a real-world application, it should be replaced with a proper user database.
 
File Handling:

The Flask application offers a feature for uploading files and provides the following endpoints:
	*/upload-form (GET) - This route exhibits an HTML form designed for file uploads.
	*/upload (POST) - Utilize this route for the purpose of file uploads. To evaluate the file upload functionality, you can employ this route to submit files.

Application Configuration:

	*The application is structured to accept files with specific extensions as defined in the ALLOWED_EXTENSIONS set, such as png, jpg, and jpeg.
	*A maximum file size of 10MB (10 * 1024 * 1024 bytes) is established as the allowable limit, and this value can be adjusted via the MAX_CONTENT_LENGTH variable.
	*The default directory for file uploads is predetermined as 'C:/Project/myflaskapp/Uploads'. It is advisable to modify this to your preferred folder location.


Open Access Route:

The Flask application offers an uncomplicated route accessible at /public/items (GET) for obtaining a collection of publicly available items. The content of this list can be tailored within the PublicRoute.py file to meet specific requirements. 
Should the need arise, both the list of public items and the application's functionality can be adapted to accommodate more intricate data structures.


Services Overview:

The Flask application serves as a gateway to communicate with a MySQL database for restaurant management. It facilitates operations like restaurant creation, retrieval, updating, and deletion through dedicated routes. 
To test and engage with the application, you can employ tools such as Postman for making API requests.
Feel free to adapt and enhance the application to support additional intricate data and features according to your requirements.
