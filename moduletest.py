import unittest, os
from app import app, db
from app.models import user, conversations

class UserModelCase(unittest.TestCase):

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            u1 = user(userID='00000000', name='Tester', email='test@test.com', password_hash='testpass')
            u2 = user(userID='11111111', name='Tester2', email='test2@test.com', password_hash='testpass2')
            db.session.add(u1)
            db.session.add(u2)
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = user.query.get('0')
        u.set_password('cat')
        print("Running password hashing test...")
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

if __name__ == '__main__':
    unittest.main(verbosity=2)