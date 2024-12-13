import gi
from gi.overrides.Gtk import Window

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title = "GRID")

        grid = Gtk.Grid()

        boton1 = Gtk.Button(label = "Boton 1")
        boton2 = Gtk.Button(label = "Boton 2")
        boton3 = Gtk.Button(label = "Boton 3")
        boton4 = Gtk.Button(label = "Boton 4")
        boton5 = Gtk.Button(label = "Boton 5")
        boton6 = Gtk.Button(label = "Boton 6")
        boton7 = Gtk.Button(label = "Boton 7")
        boton8 = Gtk.Button(label = "Boton 8")
        boton9 = Gtk.Button(label = "Boton 9")
        boton10 = Gtk.Button(label = "Boton 10")
        boton11 = Gtk.Button(label = "Boton 11")
        boton12 = Gtk.Button(label = "Boton 12")

        """
        grid.attach(boton1, 0, 0, 1, 1)
        grid.attach(boton2, 1, 0, 1, 1)
        grid.attach(boton3, 0, 1, 1, 1)
        grid.attach(boton4, 1, 1, 1, 1)
        grid.attach(boton5, 0, 2, 1, 1)
        grid.attach(boton6, 1, 2, 1, 1)
        grid.attach(boton7, 0, 3, 1, 1)
        grid.attach(boton8, 1, 3, 1, 1)
        grid.attach(boton9, 0, 4, 1, 1)
        grid.attach(boton10, 1, 4, 1, 1)
        grid.attach(boton11, 0, 5, 1, 1)
        grid.attach(boton12, 1, 5, 1, 1)
        """

        grid.add(boton1)
        grid.attach (boton2,1,0,2,1)
        grid.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(boton4, boton2, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(boton7, boton3, Gtk.PositionType.BOTTOM, 3, 1)
        grid.attach_next_to(boton8, boton7, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(boton9, boton8, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(boton10, boton9, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(boton11, boton9, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach_next_to(boton12, boton8, Gtk.PositionType.RIGHT, 1, 3)

        self.add(grid)


if __name__ =="__main__":
    ventana = MainWindow()
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()
    Gtk.main()

