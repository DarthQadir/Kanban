import os
import unittest
from kanban import db, app

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):
 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        
    def tearDown(self):
        pass
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_add(self):
        response = self.app.post( '/add', data = dict(new_task="test",category='To do'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_move(self):
        self.test_add()
        response = self.app.post('/move', data=dict(move_task='test',move_column='Doing'),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_delete(self):
        self.test_add()
        response = self.app.post('/delete', data=dict(delete_task='test'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


        


if __name__ == "__main__":
    unittest.main()
    
