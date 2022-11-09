from tkinter import ttk, constants, Canvas
from kartat.kartta1 import Kartat

class KarttaRuutu:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self.canvas = None
        self.cordinate_list = ["0", "0", "9", "9"]
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    """Alustetaan kartta käymällä rivejä läpi,
    jos kartalla on 'o', niin tulee valkoinen,
    jos kartalla on 'p', niin tulee musta.
    Lisäksi, jos valkoisella on valittu alku koordinaatti,
    niin tulee sininen. Punainen tulee loppukoordinaatille."""
    def set_cordinates_for_canvas(self):
        if self.canvas != None:
            self.canvas.after(1000, self.canvas.destroy())
        self.canvas = Canvas(self._root, width=500, height=500)
        show_map = Kartat().maps(1)
        color_number_1 = 0
        color_number_2 = 0

        for i in range(40, 401, 40):
            for j in range(40, 401, 40):
                if show_map[color_number_1][color_number_2] == "o":
                    self.canvas.create_rectangle(j, i, j+40, i+40, fill="white")
                    if self.cordinate_list != None:
                        if str(color_number_1) == self.cordinate_list[0] and str(color_number_2) == self.cordinate_list[1]:
                            self.canvas.create_rectangle(j, i, j+40, i+40, fill="blue")
                            print("mentiin")
                            print(color_number_1, self.cordinate_list[0])
                        if str(color_number_1) == self.cordinate_list[2] and str(color_number_2) == self.cordinate_list[3]:
                            self.canvas.create_rectangle(j, i, j+40, i+40, fill="red")
                else:
                    self.canvas.create_rectangle(j, i, j+40, i+40, fill="black")
                color_number_2 += 1
            color_number_1 += 1
            color_number_2 = 0
        self.canvas.pack(padx=0, pady=50)

    def _handle_finding_route(self, value1, value2, value3, value4):
        print("Reitti löytyi ajassa:")
        print(value1, value2)
        print(value3, value4)
        self.cordinate_list = [value1, value2, value3, value4]
        self.set_cordinates_for_canvas()

    """Alustetaan näkymä."""
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Reitin haku")
        label_for_start = ttk.Label(master=self._frame, text="Aloituskoordinaatti")
        label_for_finish = ttk.Label(master=self._frame, text="Lopetuskoordinaatti")

        cordinate_1 = ttk.Entry(master=self._frame)
        number_1 = ttk.Entry(master=self._frame)
        alphabet_2 = ttk.Entry(master=self._frame)
        number_2 = ttk.Entry(master=self._frame)
        
        label.grid(row=0, column=0)
        label_for_start.grid(row=2, column=0)
        cordinate_1.grid(row=2, column=1)
        number_1.grid(row=2, column=2)
        label_for_finish.grid(row=3, column=0)
        alphabet_2.grid(row=3, column=1)
        number_2.grid(row=3, column=2)

        button = ttk.Button(
            master=self._frame,
            text="Etsi reitti",
            command=lambda: self._handle_finding_route(cordinate_1.get(), number_1.get(), alphabet_2.get(), number_2.get())
        )

        button.grid(row=1, column=0)