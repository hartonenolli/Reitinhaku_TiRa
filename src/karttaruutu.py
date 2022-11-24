from tkinter import ttk, constants, Canvas
from kartat.kartta1 import Kartat
from algoritmit.dijkstra import Dijkstra
import datetime


class KarttaRuutu:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self.canvas = None
        self.x_y_list = ["0", "0", "9", "9"]
        self.save_dijkstra = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def set_dijkstra(self):
        self.save_dijkstra = 1

    """Alustetaan kartta käymällä rivejä läpi,
    jos kartalla on 'o', niin tulee valkoinen,
    jos kartalla on 'p', niin tulee musta.
    Lisäksi, jos valkoisella on valittu alku koordinaatti,
    niin tulee sininen. Punainen tulee loppukoordinaatille."""

    def set_cordinates_for_canvas(self, map_number):
        show_map = Kartat().maps(map_number)
        if self.canvas is not None:
            self.canvas.after(0, self.canvas.destroy())
        self.canvas = Canvas(self._root, width=500, height=500)
        if show_map[int(self.x_y_list[0])][int(self.x_y_list[1])] == "p":
            print("Start is not correct!")
            self._initialize()
        elif show_map[int(self.x_y_list[2])][int(self.x_y_list[3])] == "p":
            print("End is not correct!")
            self._initialize()
        #show_map = Kartat().maps(map_number)
        elif self.save_dijkstra == 1:
            time_starts = datetime.datetime.now()
            make_map = Dijkstra(map_number).make_nodes(self.x_y_list)
            show_map = Dijkstra(
                map_number, make_map[0], make_map[1], self.x_y_list).algorithim()
            time_ends = datetime.datetime.now()
            print(time_ends-time_starts)
        color1 = 0
        color2 = 0

        start1 = ""
        start2 = ""
        finish1 = ""
        finish2 = ""

        to = 40
        until = 401

        if map_number == 3:
            to = 30
            until = 461


        for i in range(to, until, to):
            for j in range(to, until, to):
                if show_map[color1][color2] == "o":
                    self.canvas.create_rectangle(
                        j, i, j+to, i+to, fill="white")
                    # if self.x_y_list is not None:
                    if str(color1
                           ) == self.x_y_list[0] and str(color2) == self.x_y_list[1]:
                        self.canvas.create_rectangle(
                            j, i, j+to, i+to, fill="blue")
                        start1 += str(color2)
                        start2 += str(color1)
                    if str(color1
                           ) == self.x_y_list[2] and str(color2) == self.x_y_list[3]:
                        self.canvas.create_rectangle(
                            j, i, j+to, i+to, fill="red")
                        finish1 += str(color2)
                        finish2 += str(color1)
                elif show_map[color1][color2] == "d":
                    self.canvas.create_rectangle(
                        j, i, j+to, i+to, fill="green")
                elif show_map[color1][color2] == "r":
                    self.canvas.create_rectangle(
                        j, i, j+to, i+to, fill="yellow")
                else:
                    self.canvas.create_rectangle(
                        j, i, j+to, i+to, fill="black")
                color2 += 1
            color1 += 1
            color2 = 0
        self.canvas.pack(padx=0, pady=50)
        # if algorithm_number == 1:
        # if self.save_dijkstra == 1:
        #    Dijkstra(map_number).make_nodes([start1, start2, finish1, finish2])
        return True

    def _handle_finding_route(self, value_list, map_number):
        print("Reitti löytyi ajassa:")
        print(value_list[0], value_list[1])
        print(value_list[2], value_list[3])
        self.x_y_list = value_list
        self.set_cordinates_for_canvas(map_number)

    """Alustetaan näkymä.
        Tässä asetetaan kaikki elementit paikoilleen.
        Painamalla Kartta painikkeita saa kartat näkyviin.
        Painamalla Dijkstra painiketta ennen kartta painiketta
        aloitetaan reitinhaku algoritmilla."""

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Reitin haku")
        label_for_start = ttk.Label(
            master=self._frame, text="Aloituskoordinaatti")
        label_for_finish = ttk.Label(
            master=self._frame, text="Lopetuskoordinaatti")

        y_1 = ttk.Entry(master=self._frame)
        x_1 = ttk.Entry(master=self._frame)
        y_2 = ttk.Entry(master=self._frame)
        x_2 = ttk.Entry(master=self._frame)

        label.grid(row=0, column=0)
        label_for_start.grid(row=3, column=0)
        x_1.grid(row=3, column=1)
        y_1.grid(row=3, column=2)
        label_for_finish.grid(row=4, column=0)
        x_2.grid(row=4, column=1)
        y_2.grid(row=4, column=2)

        button = ttk.Button(
            master=self._frame,
            text="Kartta1",
            command=lambda: self._handle_finding_route(
                [y_1.get(), x_1.get(), y_2.get(), x_2.get()], 1)
        )

        button.grid(row=1, column=0)

        button_map = ttk.Button(master=self._frame,
                                text="Kartta2",
                                command=lambda:
                                self._handle_finding_route(
                                    [y_1.get(), x_1.get(), y_2.get(), x_2.get()],
                                    2))

        button_map.grid(row=1, column=1)

        button_3 = ttk.Button(master=self._frame,
                                text="Kartta3",
                                command=lambda:
                                self._handle_finding_route(
                                    [y_1.get(), x_1.get(), y_2.get(), x_2.get()],
                                    3))

        button_3.grid(row=1, column=2)

        button_dijkstra = ttk.Button(master=self._frame,
                                     text="Dijkstra",
                                     command=self.set_dijkstra)

        button_dijkstra.grid(row=2, column=0)
