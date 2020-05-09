#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main
from unittest.mock import patch

from random_sum import sum_numbers_add_random_int


class TestApp(TestCase):
    @patch('random.randint')
    def test_random_sum(self, mocked_randint):
        nums = [10, 11, 12]
        mocked_randint.return_value = 1  # making randint builtin return integer 1
        self.assertEqual(sum_numbers_add_random_int(nums), 34)
        self.assertTrue(mocked_randint.called)
        mocked_randint.assert_called_with(1, 100)

        mocked_randint.return_value = 2  # making randint builtin return integer 2
        self.assertEqual(sum_numbers_add_random_int(nums), 35)
        self.assertTrue(mocked_randint.called)
        mocked_randint.assert_called_with(1, 100)

        mocked_randint.return_value = 3  # making randint builtin return integer 3
        self.assertEqual(sum_numbers_add_random_int(nums), 36)
        self.assertTrue(mocked_randint.called)
        mocked_randint.assert_called_with(1, 100)


if __name__ == '__main__':
    main()
