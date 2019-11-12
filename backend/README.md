# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT

### Categories

```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a list of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An list with a single entity, categories, that contains a object of id: category_string type:value pairs. 
[
    {
        "id": 1,
        "type": "Science"
    },
    {
        "id": 2,
        "type": "Art"
    },
    {
        "id": 3,
        "type": "Geography"
    },
    {
        "id": 4,
        "type": "History"
    },
    {
        "id": 5,
        "type": "Entertainment"
    },
    {
        "id": 6,
        "type": "Sports"
    }
]

```

#### Add a new category

```
POST '/categories'
```
- Adds a new category into the category list.
- Request Body: 
 ```
{
    "category_type": "category3"
}
```
- Returns the newly added category and its ID
```
{
    "data": {
        "id": 4,
        "type": "category3"
    },
    "statusCode": 200,
    "success": true
}
```
### Questions

#### Adding a new question

```
POST '/questions'
```
- Takes in request body arguments and adds a new question to the existing list.
- Request Body:
```
{
	"question": "Which dung beetle was worshipped by the ancient Egyptians?",
	"answer": "Scarab",
	"difficulty": "4",
	"category_id": "4"
}
```
- Returns the data object of the newly inserted question
```
{
    "data": {
        "answer": "Scarab",
        "category_id": 4,
        "difficulty": 4,
        "id": 19,
        "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    "status_code": 200,
    "success": true,
    "total_count": 1
}
```

#### Get the list of question

```
GET /questions?page=<page_number>
```
- It gives the list of questions. Each entry object has a question, answer, difficulty and its
 corresponding category id
- Request Arguments:
```
?page=1
```
- returns the questions list and category list as well
```
{
    "data": {
        "categories": [
            {
                "id": 1,
                "type": "category1"
            },
            {
                "id": 2,
                "type": "category2"
            },
            {
                "id": 3,
                "type": "category3"
            },
            {
                "id": 4,
                "type": "category3"
            }
        ],
        "questions": [
            {
                "answer": "run",
                "category_id": 1,
                "difficulty": 1,
                "id": 1,
                "question": "question 1"
            }
        ]
    },
    "status_code": 200,
    "success": true,
    "total_count": 1
}
```

#### Delete a question

```
DELETE /questions/<int:question_id>
```
- It deletes the question from the given list based on qquestion id
- Request Params:
```
/questions/1
```
- It returns the data object of the question deleted
```
{
    "data": {
        "category_id": 4,
        "difficulty": 4,
        "id": 19,
        "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    "status_code": 200,
    "success": true
}
```

#### Search question 

```
POST /questions/search?page=<page_number>
```
- It performs partial text match and returns the list of questions matching.
- Request Argument:
```
/questions/search?page=1
```
- Request Body:
```
{
	"search_term": "ques"
}
```
- Returns the list of questions matching each entry has the same format as the get questions list request
except for the category list.
```
{
    "data": [
        {
            "answer": "run",
            "category_id": 1,
            "difficulty": 1,
            "id": 1,
            "question": "question 1"
        }
    ],
    "status_code": 200,
    "success": true,
    "total_count": 1
}
```

#### Get questions by category Id

```
GET /categories/<int:category_id>/questions?page=<page_number>
```
- It gives the list of questions that belongs to the particular category id
- Request Argument:
```
?page=1
```
- Request Params:
```
/categories/1/questions
```
- Returns the list of questions, each entity has an answer, question, difficulty and a category id
```
{
    "data": [
        {
            "answer": "The Liver",
            "category_id": 1,
            "difficulty": 4,
            "id": 16,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category_id": 1,
            "difficulty": 3,
            "id": 17,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category_id": 1,
            "difficulty": 4,
            "id": 18,
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "status_code": 200,
    "success": true,
    "total_count": 3
}
```

### Quiz

#### Get the quiz list

```
/quizzes
```

- Gives the data object which has the current question, the corresponding answer to it based on the 
category we have chosen

- Request Body:
```
{
    "quiz_category": {
        "id": "1"
    },
    "previous_questions": [1]
}
```
- quiz_category: the category which we want questions from
- previous_questions: contains the list of questions which we already played
- Result:
```
{
    "data": {
        "answer": "The Liver",
        "category_id": 1,
        "difficulty": 4,
        "id": 16,
        "question": "What is the heaviest organ in the human body?"
    },
    "status_code": 200,
    "success": true
}
```

## Error Codes

Currently it supports 404 and 422 error codes

## Testing
To run the tests, run
```
dropdb trivia_test -U postgres
createdb trivia_test -U postgres
psql trivia_test < trivia.psql
python test_flaskr.py
```