# test_app.py
import unittest
import datetime as dt
from unittest.mock import Mock, patch
from app import has_user_expired, find_expired_users


class TestApp(unittest.TestCase):
    def setUp(self):
        self.today = dt.datetime.now()
        self.yesterday = dt.datetime.now() - dt.timedelta(days=1)
        self.day_before = dt.datetime.now() - dt.timedelta(days=2)
        self.tomorrow = dt.datetime.now() + dt.timedelta(days=2)

    def test_has_user_expired(self):
        '''
        The function `has_user_expired()` takes a argument `user` which is a
        SQLAlchemy database object. The object contains attributes `id`,
        `firstname`, `lastname`, `join_date` and `expiration_date`.

        If the `expiration_date` is less than the date today it will
        return `True` or if the `expiration_date` is greater than today
        then return `False`

        For this test since we do not want to speak with the database we
        will create a `Mock` object and assign it the attributes that
        a user has. This `Mock` object is just another python class that when
        called for any fake attribute will return an answer.
        '''

        # create a mock `user` object
        user = Mock()

        # now set the attributes for the `user` object
        user.id = 1
        user.firstname = 'John'
        user.lastname = 'Smith'
        user.join_date = self.day_before
        user.expiration_date = self.yesterday

        # now we pass the `user` object check for expected result `True`
        result = has_user_expired(user)
        self.assertTrue(result)

        # for the same user we can update the `expiration_date` to sometime
        # in the future to see if the expected result is `False`
        user.expiration_date = self.tomorrow
        result = has_user_expired(user)
        self.assertFalse(result)

    def test_find_expired_users(self):
        """
        We patch the function `get_all_user()` with our own function
        `mocked_get_all_users` for which we set a `return_value`.
        The `return_value` will contain a list of `Mock` users.
        Some of these users are expired and some of them haven't expired.
        We compare the output of our mocked `get_all_user()` function with
        the `expected` output.
        """

        with patch('app.get_all_users') as mocked_get_all_users:
            mocked_get_all_users.return_value = [
                Mock(id=1,
                     firstname='John',
                     lastname='Smith1',
                     join_date=self.today,
                     expiration_date=self.tomorrow),
                Mock(id=2,
                     firstname='John',
                     lastname='Smith2',
                     join_date=self.yesterday,
                     expiration_date=self.tomorrow),
                Mock(id=3,
                     firstname='John',
                     lastname='Smith3',
                     join_date=self.day_before,
                     expiration_date=self.tomorrow),
                Mock(id=4,
                     firstname='John',
                     lastname='Smith3',
                     join_date=self.day_before,
                     expiration_date=self.yesterday),
                Mock(id=5,
                     firstname='John',
                     lastname='Smith3',
                     join_date=self.day_before,
                     expiration_date=self.today),
            ]
            results = find_expired_users()
            expected = [4, 5]  # we know only user `id` 4 and 5 have expired
            self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
