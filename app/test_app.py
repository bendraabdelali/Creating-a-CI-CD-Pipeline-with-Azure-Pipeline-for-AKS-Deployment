"""
Account API Service Test Suite
Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""

import unittest
# from  ..app import status # HTTP Status Codes

from flask_pymongo import PyMongo
from faker import Faker
from flask import Flask
from bson.objectid import ObjectId

from app import app, db


######################################################################
#  T E S T   C A S E S
######################################################################
class TestAccountService(unittest.TestCase):
    """Account Service Tests"""
    global mongodb_client
    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False



    @classmethod
    def tearDownClass(cls):
        """Runs once before test suite"""
        pass
    def setUp(self):
        """Runs before each test"""
        db.users.delete_many({})  # clean up the last tests
        self.client = app.test_client()
    def tearDown(self):
        """Runs once after each test case"""
        db.users.delete_many({})

    ######################################################################
    #  H E L P E R   M E T H O D S
    ######################################################################
    def create_account(self):
        data={}
        fake = Faker()
        data["name"] = fake.name()
        data["role"] = fake.job()
        return data
        

        
    def _create_accounts(self, count):
        """Factory method to create accounts in bulk"""
        global create_account
        accounts = []
        for i in range(count):
            account = self.create_account()

            response = db.users.insert_one(account)
            db_nbr_users = len([x for x in db.users.find() ])
            self.assertEqual(
               db_nbr_users,
               i+1
            )


            account["_id"] = ObjectId(response.inserted_id )
            accounts.append(account)
        return accounts

    ######################################################################
    #  A C C O U N T   T E S T   C A S E S
    ######################################################################

    def test_index(self):
        """It should get 200_OK from the Home Page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
   
    def test_health(self):
        """It should be healthy"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["status"], "OK")

    def test_create_account(self):
        """It should Create a new Account"""
        account = self.create_account()
        response = self.client.post(
            "/add-user",
            data=account,
           
        )
        
        db_nbr_users = len([x for x in db.users.find() ])
        self.assertEqual(
            db_nbr_users,
         1   
        )

        
# #  test route 

    def test_get_account(self):
        """It should Read a single Account"""
        account = self._create_accounts(1)[0]
        resp = self.client.get(
            f"/edit-user/{account['_id']}", content_type="application/json"
        )
        # get the note details from the db
        data = dict(db.users.find_one({'_id': ObjectId(account['_id'])}))

        # self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], account["name"])
    
    def test_account_not_found(self):
        """It should Read a single Account"""
        account = self._create_accounts(1)[0]
        resp = self.client.get(
            f"edit-user/0"
        )
        self.assertEqual(resp.status_code, 404)
    

    def test_get_account_list(self):
        """It should Get a list of Accounts"""
        accounts = self._create_accounts(5)
        # send a self.client.get() request to the BASE_URL
        resp = self.client.post("/")
        # assert that the resp.status_code is status.HTTP_200_OK
        self.assertEqual(resp.status_code,200)
        # get the data from resp.get_json()
        data =  resp.get_json()
        # assert that the len() of the data is 5 (the number of accounts you created)
        self.assertEqual(data["nbr_users"],5)

   



    def test_delete_account(self):
        """It should Delete an Account"""
        account = self._create_accounts(1)[0]
        nbr_users = len([i for i in db.users.find({'_id': account["_id"]})])
        self.assertEqual(nbr_users,1)
        
        resp =  self.client.post(
             f"/delete-user",
             data = {"_id":account['_id']}
        )
        data =  resp.get_json()
        # self.assertEqual(data['status'],1)
        nbr_users = len([i for i in db.users.find({'_id': account["_id"]})])
        self.assertEqual(nbr_users,0)

       
    def test_update_account(self):
            """It should Update an existing Account"""
            # create an Account to update    
            account = self._create_accounts(1)[0]
            nbr_users = len([i for i in db.users.find({'_id': account["_id"]})])
            self.assertEqual(nbr_users,1)
      
            # update the account
            # get the data from resp.get_json() as new_account
            new_account  = account

            # change new_account["name"] to something known
            new_account["name"]="walid"

            # send a self.client.post() request to the BASE_URL with a json payload of new_account
            resp =  self.client.post(
             f"/edit-user",
             data = new_account
            )
            
            # get the note details from the db
            data = dict(db.users.find_one({'_id': ObjectId(new_account["_id"])}))

            # assert that the updated_account["name"] is whatever you changed it to    
            self.assertEqual(data["name"], "walid")


if __name__ == '__main__':
    unittest.main()