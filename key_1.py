#!/usr/bin/env python

import pynput.keyboard


def process_key_press(key):
    print(key)
    
keybord_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keybord_listener:
    keybord_listener.join()
