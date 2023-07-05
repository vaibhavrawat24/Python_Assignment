This project demonstrates the implementation of a RESTful API using Django and SQLite, along with a user search feature. The API allows searching for users based on their first name. If the users are found in the local database, they are returned in a JSON response. Otherwise, the API calls a dummy API to fetch users with the given first name, saves them to the user table, and returns them in the response.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/your-repo.git
```
2. Navigate to the project directory:
```
cd your-repo
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Run database migrations:
```
python manage.py migrate
```
5. Start the development server:
```
python manage.py runserver
```


The server will start running at http://127.0.0.1:8000/.

## Usage

To search for users based on their first name, make a GET request to the API endpoint:

```
http://127.0.0.1:8000/?first_name=<search_query>
```


Replace `<search_query>` with the first name you want to search for. The API will respond with a JSON object containing the matching users' information.

If the users are found in the local database, the JSON response will include the user details retrieved from the database. If no users are found, the API will call a dummy API to fetch users with the given first name, save them to the user table, and return them in the response.

## Example

Let's assume we want to search for users with the first name "Jane". We can make a GET request to the following URL:

```
http://127.0.0.1:8000/?first_name=Jane
```

The API will respond with a JSON object similar to the following:

<img width="960" alt="django_project" src="https://github.com/vaibhavrawat24/Python_Assignment/assets/100408695/7050ead3-6945-42bf-a626-ca2a7645edfc">

If the search query matches users in the local database, the response will contain the details of the matching users. Otherwise, the response will include the user details fetched from the dummy API and saved to the local database.

Additional Notes
The project uses Django and SQLite as the database backend. You can modify the database settings in the settings.py file if needed.

The code for the user search feature can be found in the users/views.py file. It includes searching the local database for users and calling the dummy API if no users are found.

The project includes appropriate error handling and returns informative responses when users are not found or when there is an error during API calls.

The project uses the requests library to make HTTP requests to the dummy API. Make sure you have it installed (pip install requests).

The URL patterns for the API endpoints are defined in the user_api/urls.py file.

The user model is defined in the users/models.py file. You can modify the model fields according to your requirements.

The project includes migrations for the user model, allowing you to easily manage the database schema.
