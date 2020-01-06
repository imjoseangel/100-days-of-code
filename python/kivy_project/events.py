#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={
                            'center_x': .5,
                            'center_y': .5
                        })
        button.bind(on_press=self.on_press_button)

        return button

    @staticmethod
    def on_press_button(instance):
        print('You pressed the button!')


if __name__ == '__main__':
    app = MainApp()
    app.run()
