from tkinter import ttk, constants, Canvas
from kartat.kartta1 import Kartat
from algoritmit.dijkstra import Dijkstra
from algoritmit.ida_star import IDA_Star
import datetime


class KarttaRuutu:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self.canvas = None
        self.x_y_list = ["0", "0", "9", "9"]
        self.save_dijkstra = None
        self.ida_star = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def set_dijkstra(self):
        self.save_dijkstra = 1
        self.ida_star = None

    def set_ida_star(self):
        self.ida_star = 1
        self.save_dijkstra = None

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
        elif self.save_dijkstra == 1:
            print("Lyhyin reitti löydetty:")
            time_starts = datetime.datetime.now()
            make_map = Dijkstra(map_number).make_nodes(self.x_y_list)
            show_map = Dijkstra(
                map_number).algorithim(make_map[0], make_map[1], self.x_y_list)
            time_ends = datetime.datetime.now()
            final_time = time_ends-time_starts
            sekuntit = str(final_time).split(":")
            print(f"Reitti löytyi ajassa {sekuntit[-1]}s")
        elif self.ida_star == 1:
            print("lyhin reitti löydetty:")
            time_starts = datetime.datetime.now()
            tee_kartta = IDA_Star(map_number).tee_ruudut(self.x_y_list)
            show_map = IDA_Star(map_number).ida_funktio(tee_kartta[0], tee_kartta[1], self.x_y_list)
            time_ends = datetime.datetime.now()
            final_time = time_ends-time_starts
            sekuntit = str(final_time).split(":")
            print(f"Reitti löytyi ajassa {sekuntit[-1]}s")
        color1 = 0
        color2 = 0

        to = 40
        until = 401

        if map_number == 2:
            to = 30
            until = 461
        elif map_number == 3:
            to = 23
            until = 461

        for i in range(to, until, to):
            for j in range(to, until, to):
                if show_map[color1][color2] == "o":
                    self.canvas.create_rectangle(
                        j, i, j+to, i+to, fill="white")
                    if str(color1
                           ) == self.x_y_list[0] and str(color2) == self.x_y_list[1]:
                        self.canvas.create_rectangle(
                            j, i, j+to, i+to, fill="blue")
                    if str(color1
                           ) == self.x_y_list[2] and str(color2) == self.x_y_list[3]:
                        self.canvas.create_rectangle(
                            j, i, j+to, i+to, fill="red")
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

    def _handle_finding_route(self, value_list, map_number):
        if map_number == 1:
            if str(value_list[1]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Huolitutu arvot 0-9, alku x väärin. Asetettu 0")
                value_list[1] = str(0)
            if str(value_list[0]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Huolitutu arvot 0-9, alku y väärin. Asetetu 0")
                value_list[0] = str(0)
            if str(value_list[3]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Huolitutu arvot 0-9, loppu x väärin. Asetettu 9")
                value_list[3] = str(9)
            if str(value_list[2]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Huolitutu arvot 0-9, loppu y väärin. Asetettu 9")
                value_list[2] = str(9)
        elif map_number == 2:
            if str(value_list[1]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]:
                print("Huolitutu arvot 0-14, alku x väärin. Asetettu 0")
                value_list[1] = str(0)
            if str(value_list[0]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]:
                print("Huolitutu arvot 0-14, alku y väärin. Asetetu 0")
                value_list[0] = str(0)
            if str(value_list[3]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]:
                print("Huolitutu arvot 0-14, loppu x väärin. Asetettu 14")
                value_list[3] = str(14)
            if str(value_list[2]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]:
                print("Huolitutu arvot 0-14, loppu y väärin. Asetettu 14")
                value_list[2] = str(14)
        else:
            if str(value_list[1]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Huolitutu arvot 0-19, alku x väärin. Asetettu 0")
                value_list[1] = str(0)
            if str(value_list[0]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Huolitutu arvot 0-19, alku y väärin. Asetetu 0")
                value_list[0] = str(0)
            if str(value_list[3]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Huolitutu arvot 0-19, loppu x väärin. Asetettu 19")
                value_list[3] = str(19)
            if str(value_list[2]) not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
                print("Huolitutu arvot 0-19, loppu y väärin. Asetettu 19")
                value_list[2] = str(19)
        print(value_list[1], value_list[0])
        print(value_list[3], value_list[2])
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

        x_1 = ttk.Entry(master=self._frame)
        y_1 = ttk.Entry(master=self._frame)
        x_2 = ttk.Entry(master=self._frame)
        y_2 = ttk.Entry(master=self._frame)

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

        button_ida = ttk.Button(master=self._frame,
                                     text="IDA-*",
                                     command=self.set_ida_star)

        button_ida.grid(row=2, column=1)
