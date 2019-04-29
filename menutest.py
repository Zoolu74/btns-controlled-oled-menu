import sys
from time import sleep

from Menus.Menu import Menu
from Input.Buttons import Buttons

m = Menu([
    "First line",
    "A second menu option",
    "Now to the third",
    "On to the forth",
    "Follow the fifth",
    "Support the sixth"
])

b = Buttons(**{'menu': m, 'btn_left': 17, 'btn_ok': 27, 'btn_right': 22})

if len(sys.argv) > 1:
    if sys.argv[1] == 'clear':
        m.blank(True)
    else:
        m.set_highlight(int(sys.argv[1]))
        m.render()
else:
    m.render()

while True:
    sleep(1)
