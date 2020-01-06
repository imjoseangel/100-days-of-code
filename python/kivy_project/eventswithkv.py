#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button


class ButtonApp(App):
    def build(self):
        return Button()

    @staticmethod
    def on_press_button():
        print('You pressed the button!')


if __name__ == '__main__':
    app = ButtonApp()
    app.run()
