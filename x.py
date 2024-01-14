from ptoled import PTOLEDDisplay
from ptbuttons import PTUpButton, PTDownButton, PTSelectButton, PTCancelButton

up_button = PTUpButton()
down_button = PTDownButton()
select_button = PTSelectButton()
cancel_button = PTCancelButton()
def do_up_thing():
    oled_screen = PTOLEDDisplay()
    oled_screen.draw_multiline_text("up button")
def do_down_thing():
    oled_screen = PTOLEDDisplay()
    oled_screen.draw_multiline_text("down button")
def do_another_thing():
    oled_screen = PTOLEDDisplay()
    oled_screen.draw_multiline_text("X button")
def select_something():
    oled_screen = PTOLEDDisplay()
    oled_screen.draw_multiline_text("O button")

up_button.when_pressed = do_up_thing
down_button.when_pressed = do_down_thing
select_button.when_pressed = select_something
cancel_button.when_pressed = do_another_thing