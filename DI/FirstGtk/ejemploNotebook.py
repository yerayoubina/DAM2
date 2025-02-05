import gi
# Aseguramos la version de Gtk a usar

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Clase principal de la ventana
class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        # Inicializa la ventana principal
        super().__init__()
        self.set_title("Ejemplo con gtk Notebook")

        cartafol = Gtk.Notebook()

        paxina1 = Gtk.Box()
        paxina1.set_border_width(10)
        paxina1.add(Gtk.Label(label = "Páxina 1"))
        cartafol.append_page(paxina1, Gtk.Label("Título páxina 1"))

        paxina2 = Gtk.Box()
        paxina2.set_border_width(10)
        paxina2.add(Gtk.Label("Páxina con imagen de título"))
        cartafol.append_page(paxina2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))


        # Agregar el contenedor principal a la ventana
        self.add(cartafol)
        # Conectar el evento de cierre de ventana con la finalización del programa
        self.connect("delete-event", Gtk.main_quit)
        # Mostrar todos los widgets de la ventana
        self.show_all()


# Bloque principal de ejecución
if __name__ == "__main__":
    # Crear una instancia de la ventana principal
    app = FiestraPrincipal()
    # Conectar el evento de destrucción de ventana
    app.connect("destroy", Gtk.main_quit)
    # Mostrar la ventana
    app.show_all()
    # Iniciar el bucle de eventos de Gtk
    Gtk.main()
