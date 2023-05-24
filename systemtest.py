import unittest, os, time
from app import app, db
from app.models import user, concersations
from selenium import webdriver

class SystemTest(unittest.TestCase):
  driver = None
  
  def setUp(self):
    self.driver = webdriver.Firefox(executable_path=r)

    if not self.driver:
      self.skipTest('Web browser not available')
    else:
      db.init_app(app)
      db.create_all()
      u1 = user(userID='0', name='Tester', email='test@test.com', password_hash='testpass')
      u2 = user(userID='1', name='Tester2', email='test2@test.com', password_hash='testpass2')
      db.session.add(u1)
      db.session.add(u2)
      db.session.commit()
      self.driver.maximize_window()
      self.driver.get('http://127.0.0.1:5000')

    def tearDown(self):
      if self.driver:
        self.driver.close()
        db.session.query(user).detete()
        db.session.query(conversations).delete()
        db.session.commit()
        db.session.remove()

  def test_register(self):
    u = user.query.get('22222222')
    self.assertEqual(u.name,'Test',msg='user exists in db')
    self.driver.get('http://127.0.0.1:5000/create')
    self.driver.implicitly_wait(5)
    name_field = self.driver.find_element_by_id('name')
    name_field.send_keys('Testy')
    mail_field = self.driver.find_element_by_id('email')
    mail_field.send_keys('Test3@test.com')
    password_field = self.driver.find_element_by_id('password')
    password_field.send_keys('password123')
    time.sleep(1)
    self.driver.implicitly_wait(5)
    submit = self.driver.find_element_by_id('submit')
    submit.click()

if __name__=='__main__':
  unittest.main(verbosity=2)