from tkinter import Tk
from karttaruutu import KarttaRuutu


class UserInterface:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._map_screen()

    def _map_screen(self):
        self._current_view = KarttaRuutu(
            self._root,
        )

        self._current_view.pack()


window = Tk()
window.title("Reitinhaku")

ui = UserInterface(window)
ui.start()

window.mainloop()
