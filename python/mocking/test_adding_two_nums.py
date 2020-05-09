#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main
from unittest.mock import patch
from adding_two_nums import add_two_numbers


class TestFunctions(TestCase):
    @patch('adding_two_nums.print_text')
    def test_add_two_numbers(self, mocked_print_text):
        self.assertEqual(add_two_numbers(1, 2), 3)

        # making sure mocked print_text function is called properly
        self.assertTrue(mocked_print_text.called)
        mocked_print_text.assert_called_with(3)


if __name__ == '__main__':
    main()
