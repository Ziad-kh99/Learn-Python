import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''Setting up class before run tests.'''
        pass 

    @classmethod
    def tearDownClass(self):
        '''Deconstructiing class afetr run all test.'''
        pass

    def setUp(self):
        '''Setting up each test before exercising it.'''
        self.emp = Employee('Ziad', 'Khaled', 5000)


    def tearDown(self):
        '''Deconstructing each test after exercising it.''' 


    def test_email(self):
        self.assertEqual(self.emp.email, 'Ziad.Khaled@company.com')

        self.emp.first = 'Hossam'

        self.assertEqual(self.emp.email, 'Hossam.Khaled@company.com')


    def test_fullname(self):
        self.assertEqual(self.emp.fullname, 'Ziad Khaled')

        self.emp.last = 'Elsayed'

        self.assertEqual(self.emp.fullname, 'Ziad Elsayed')


    def test_apply_raise(self):
        self.assertEqual(self.emp.pay, 5000)

        self.emp.apply_raise()

        self.assertEqual(self.emp.pay, 5250)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Khaled/May')
            self.assertEqual(schedule, 'Success')

        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = False 

            schedule = self.emp.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Khaled/May')
            self.assertEqual(schedule, 'Bad Response!')



if __name__ == '__main__':
    unittest.main()