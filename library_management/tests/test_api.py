
import frappe.defaults
import unittest
import requests
import ast
import os

host= "http://0.0.0.0:8000"
userName= ""
correctPswrd=""

class TestLogin(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_login_admin(self):
        user ='Administrator'
        # todo: hide password secret 
        # correct_password = os.environ['HOME']
        pload = {'usr':user,'pwd':'frappe'}
        r =requests.post(host+'/api/method/login' , data=pload)
        content = ast.literal_eval(r.text)
        message= str(content["message"])
        name= str(content["full_name"])
        self.assertEqual(message,'Logged In')
        self.assertEqual(name,user)

    def test_login_wrong_password(self):
        user ='Administrator'
        wrong_password = 'AZERTYU'
        pload = {'usr':user,'pwd':wrong_password}
        r =requests.post(host+'/api/method/login' , data=pload)
        status = r.status_code
        self.assertEqual(status,401)
      

    def test_login_user_not_exists(self):
        wrong_user ='azertyu'
        wrong_password = 'AZERTYU'
        pload = {'usr':wrong_user,'pwd':wrong_password}
        r =requests.post(host+'/api/method/login' , data=pload)
        status = r.status_code
        self.assertEqual(status,401)
