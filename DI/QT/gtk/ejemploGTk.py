import gi
from gi.overrides.Gtk import Window

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class VentanaPrincipa (Window):
    def __init__(self):
        super().__init__(title ="BOTON SALUDAR")
        self.set_default_size(400,200)

        # Container vertical
        box = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        self.add(box)

        # Etiqueta
        self.labelSaludar = Gtk.Label("Escribe tu nombre y presiona saludar")
        box.pack_start(self.labelSaludar, True, True, 0)

        # TXT input
        self.txtSaludo = Gtk.Entry()
        self.txtSaludo.set_placeholder_text("Introduce tu nombre")
        box.pack_start(self.txtSaludo, True, True, 0)

        # Crear boton

        self.btnSaludo = Gtk.Button(label = "Pulsa aquí")
        self.btnSaludo.connect("clicked", self.fun_saludar)
        box.pack_start(self.btnSaludo, True, True, 0)

    def fun_saludar(self, widget):
        # Obtener el texto del campo de texto y mostrar el saludo
        nombre = self.txtSaludo.get_text()
        if nombre.strip():
            self.labelSaludar.set_text(f"¡Hola, {nombre}!")
        else:
            self.labelSaludar.set_text("Por favor, escribe tu nombre.")

if __name__ =="__main__":
    ventana = VentanaPrincipa()
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()
    Gtk.main()