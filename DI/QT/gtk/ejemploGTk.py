import gi
from gi.overrides.Gtk import Window

gi.require_version("Gtk","3.0")
from gi.repository import Gtk


"""PRIMER BOTON CON GTK"""
class VentanaPrincipa (Window):
    def __init__(self):
        super().__init__(title ="BOTON SALUDAR")
        self.set_default_size(400,200)

        # Container vertical
        self.box = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        self.add(self.box)

        # Etiqueta
        self.labelSaludar = Gtk.Label(label = "Escribe tu nombre y presiona saludar")
        #self.box.add(self.labelSaludar)
        self.box.pack_start(self.labelSaludar, False, False, 0)

        # TXT input
        self.txtSaludo = Gtk.Entry()
        self.txtSaludo.set_placeholder_text("Introduce tu nombre")
        #self.box.add(self.txtSaludo)
        self.box.pack_start(self.txtSaludo, False, True, 0)

        # Crear boton
        self.btnSaludo = Gtk.Button(label = "Pulsa aquí")
        self.btnSaludo.connect("clicked", self.fun_saludar)
        #self.box.add(self.btnSaludo)
        self.box.pack_start(self.btnSaludo, False, False, 0)

        self.btnSalir = Gtk.Button(label = "CERRAR APP")
        self.btnSalir.connect("clicked", self.fun_cerrar)
        self.box.pack_start(self.btnSalir, False, False, 0)

    def fun_saludar(self, widget):
        # Obtener el texto del campo de texto y mostrar el saludo
        nombre = self.txtSaludo.get_text()
        saludo = self.labelSaludar.get_text()
        if nombre.strip():
            self.labelSaludar.set_text(f"¡Hola, {nombre}!")

        else:
            self.labelSaludar.set_text("Por favor, escribe tu nombre.")

        print(saludo)

    def fun_cerrar(self, widget):
        Gtk.main_quit()

if __name__ =="__main__":
    ventana = VentanaPrincipa()
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()
    Gtk.main()