import os
import json
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
STATUS_CODE_SUCCESS = 200
STATUS_NOT_FOUND = 404
STATUS_UNPROCESSABLE = 422


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"*": {"origins": "*"}})

    '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

    '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origins', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
    @app.route('/categories')
    def get_categories():
        categories = Category.query.all()
        if len(categories):
            data = list(map(Category.format, categories))
            success = True
            result = {
                "data": data,
                "statusCode": STATUS_CODE_SUCCESS,
                "success": success
            }
            return jsonify(result)
        else:
            result = {
                "data": [],
                "statusCode": STATUS_CODE_SUCCESS,
                "success": False
            }
            return jsonify(result)
        abort(STATUS_UNPROCESSABLE)
    
    @app.route('/categories', methods=['POST'])
    def add_category():
        if request.data:
            category_data = json.loads(request.data.decode('utf-8'))
            category_object = Category(type=category_data['category_type'])
            Category.insert(category_object)
            res = Category.format(category_object)
            result = {
                "data": {
                    "id": res['id'],
                    "type": res['type']
                },
                "statusCode": STATUS_CODE_SUCCESS,
                "success": True
            }
            return jsonify(result)
        abort(STATUS_UNPROCESSABLE)

    '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

    '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

    '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

    '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

    '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
    @app.errorhandler(404)
    def not_found(error):
        error_data = {
            "success": False,
            "statusCode": STATUS_NOT_FOUND,
            "message": "Resource not found"
        }
        return jsonify(error_data), STATUS_NOT_FOUND
    
    @app.errorhandler(422)
    def not_unprocessable(error):
        error_data = {
            "success": False,
            "statusCode": STATUS_UNPROCESSABLE,
            "message": "Request unprocessable"
        }
        return jsonify(error_data), STATUS_UNPROCESSABLE

    with app.app_context():
        db = SQLAlchemy()
        db.init_app(app)
        db.create_all()

    return app
