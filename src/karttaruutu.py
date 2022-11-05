from tkinter import ttk, constants

class KarttaRuutu:
    def __init__(self, root, handle_finding_route):
        self._root = root
        self._handle_finding_route = handle_finding_route
        self._frame = None
        self.alphabet_1 = None
        self.value1 = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        #self.value1 = self.alphabet_1.get()

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Reitin haku")
        label_for_start = ttk.Label(master=self._frame, text="Aloituskoordinaatti")
        label_for_finish = ttk.Label(master=self._frame, text="Lopetuskoordinaatti")

        self.alphabet_1 = ttk.Entry(master=self._frame)
        number_1 = ttk.Entry(master=self._frame)
        alphabet_2 = ttk.Entry(master=self._frame)
        number_2 = ttk.Entry(master=self._frame)
        
        label.grid(row=0, column=0)
        label_for_start.grid(row=2, column=0)
        self.alphabet_1.grid(row=2, column=1)
        number_1.grid(row=2, column=2)
        label_for_finish.grid(row=3, column=0)
        alphabet_2.grid(row=3, column=1)
        number_2.grid(row=3, column=2)

        button = ttk.Button(
            master=self._frame,
            text="Etsi reitti",
            command=lambda: self._handle_finding_route(self.alphabet_1.get())
        )

        button.grid(row=1, column=0)

    def get_values(self):
        return self.value1