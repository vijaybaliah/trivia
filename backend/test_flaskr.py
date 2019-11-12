import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'password', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.code_success = 200
        self.code_not_found = 404
        self.code_unprocessable = 422

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    def format_response(self, response):
        return json.loads(response.data)
    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['success'])


    def test_get_questions(self):
        res = self.client().get('/questions')
        data = self.format_response(res)
        self.assertDictEqual(data['data']['categories'][0], 
            {'id': 1, 'type': 'category1'}
        )
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['success'])

    def test_404_get_questions(self):
        res = self.client().get('/questions?page=100')
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_not_found)
        self.assertFalse(data['success'])

    def test_delete_question(self):
        res = self.client().delete('/questions/3')
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['success'])

    def test_404_delete_question(self):
        res = self.client().delete('/questions/24')
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_not_found)
        self.assertFalse(data['success'])
    
    def test_add_question(self):
        mock_data = {
            'question': 'test',
            'answer': 'test2',
            'difficulty': 1,
            'category_id': 1
        }
        res = self.client().post('/questions', json=mock_data)
        data = self.format_response(res)
        self.assertEqual(data['data']['question'], mock_data['question'])
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['success'])
    
    def test_404_add_question(self):
        mock_data = {
            'difficulty': 1,
            'category_id': 1
        }
        res = self.client().post('/questions', json=mock_data)
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_not_found)
        self.assertFalse(data['success'])
    
    def test_search_questions(self):
        mock_data = {
            'search_term': 'test'
        }
        res = self.client().post('/questions/search', json=mock_data)
        data = self.format_response(res)
        self.assertRegex(data['data'][0]['question'], mock_data['search_term'])
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['success'])

    def test_404_search_questions(self):
        mock_data = {
        }
        res = self.client().post('/questions/search', json=mock_data)
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_not_found)
        self.assertFalse(data['success'])

    def test_get_questions_by_category_id(self):
        res = self.client().get('/categories/1/questions')
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['data']))

    def test_404_get_questions_by_category_id(self):
        res = self.client().get('/categories/100/questions')
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_not_found)
        self.assertFalse(data['success'])
    
    def test_get_quiz_question(self):
        mock_data = {
            "quiz_category": {
                "id": "1"
            },
            "previous_questions": []
        }
        res = self.client().post('/quizzes', json=mock_data)
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['data']))
    
    def test_404_get_quiz_question(self):
        mock_data = {
            "quiz_category": {
                "id": "1"
            }
        }
        res = self.client().post('/quizzes', json=mock_data)
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_not_found)
        self.assertFalse(data['success'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()