from tkinter import Tk
from karttaruutu import KarttaRuutu


class Kayttoliittyma:
    def __init__(self, root):
        self._juuri = root
        self._nakyma = None

    def start(self):
        self._kartta_ruutu()

    def _kartta_ruutu(self):
        self._nakyma = KarttaRuutu(
            self._juuri
        )

        self._nakyma.pack()


window = Tk()
window.title("Reitinhaku")

ui = Kayttoliittyma(window)
ui.start()

window.mainloop()
