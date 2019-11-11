import os
import json
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

PER_PAGE = 10
MAX_PER_PAGE = 20
STATUS_CODE_SUCCESS = 200
STATUS_NOT_FOUND = 404
STATUS_UNPROCESSABLE = 422


def paginate_request(resource, page, per_page=PER_PAGE, max_per_page=MAX_PER_PAGE):
    return resource.query.paginate(page, per_page, False, max_per_page)

def get_request_data(request):
    return json.loads(request.data.decode('utf-8'))


def format_result(data, total_count=None, status_code=STATUS_CODE_SUCCESS, success=True):
    """
        formats the given data to a generalised format.

        Parameters:
            data (dict): response data
            [total_count](int): total count of the response data
    """
    result = {
        "data": data,
        "status_code": status_code,
        "success": success
    }
    if total_count and total_count >= 0:
        result['total_count'] = total_count
    return jsonify(result)

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
                "status_code": STATUS_CODE_SUCCESS,
                "success": success
            }
            return jsonify(result)
        else:
            result = {
                "data": [],
                "status_code": STATUS_CODE_SUCCESS,
                "success": False
            }
            return jsonify(result)
        abort(STATUS_UNPROCESSABLE)
    
    @app.route('/categories', methods=['POST'])
    def add_category():
        if request.data:
            category_data = get_request_data(request)
            category_object = Category(type=category_data['category_type'])
            Category.insert(category_object)
            res = Category.format(category_object)
            result = {
                "data": {
                    "id": res['id'],
                    "type": res['type']
                },
                "status_code": STATUS_CODE_SUCCESS,
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
    @app.route('/questions')
    def get_questions():
        page = request.args.get('page', 1, type=int)
        categories = list(map(Category.format, Category.query.all()))
        paginated_questions = paginate_request(Question, page)
        questions = list(map(Question.format, paginated_questions.items))
        total_count = paginated_questions.total
        if total_count > 0:
            data = {
                'categories': categories,
                'questions': questions,
            }
            return format_result(data, total_count)
        abort(STATUS_UNPROCESSABLE)
    '''
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question_object = Question.query.get(question_id)
            Question.delete(question_object)
            res = Question.format(question_object)
            result = {
                "data": {
                    "id": res['id'],
                    "question": res['question'],
                    "difficulty": res['difficulty'],
                    "category_id": res['category_id']
                },
                "status_code": STATUS_CODE_SUCCESS,
                "success": True
            }
            return jsonify(result)
        except Exception as e:
            print('delete_question: ', e)
            abort(STATUS_UNPROCESSABLE)
    '''
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''
    @app.route('/questions', methods=['POST'])
    def add_question():
        if (request.data):
            request_data = get_request_data(request)
            if ('question' in request_data\
                and 'answer' in request_data\
                and 'difficulty' in request_data\
                and 'category_id' in request_data):
                question_object = Question(
                    question=request_data['question'],
                    answer=request_data['answer'],
                    difficulty=request_data['difficulty'],
                    category_id=request_data['category_id']
                )
                Question.insert(question_object)
                res = Question.format(question_object)
                data = {
                    "id": res['id'],
                    "question": res['question'],
                    "difficulty": res['difficulty'],
                    "category_id": res['category_id']
                }
                total_count = 1
                return format_result(data, total_count)
            else:
                abort(STATUS_UNPROCESSABLE)
        abort(STATUS_UNPROCESSABLE)
    '''
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    '''
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        if (request.data):
            page = request.args.get('page', 1, type=int)
            request_data = get_request_data(request)
            if 'search_term' in request_data:
                paginated_query = Question.query.filter(Question\
                    .question.ilike('%' + request_data['search_term'] + '%'))\
                    .paginate(page, PER_PAGE, False, MAX_PER_PAGE)
                questions = list(map(Question.format, paginated_query.items))
                total_count = paginated_query.total
                return format_result(questions, total_count)
            else:
                abort(STATUS_UNPROCESSABLE)
        abort(STATUS_UNPROCESSABLE)


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
            "status_code": STATUS_NOT_FOUND,
            "message": "Resource not found"
        }
        return jsonify(error_data), STATUS_NOT_FOUND
    
    @app.errorhandler(422)
    def not_unprocessable(error):
        error_data = {
            "success": False,
            "status_code": STATUS_UNPROCESSABLE,
            "message": "Request unprocessable"
        }
        return jsonify(error_data), STATUS_UNPROCESSABLE

    with app.app_context():
        db = SQLAlchemy()
        db.init_app(app)
        db.create_all()

    return app
