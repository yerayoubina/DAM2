import gi
# Aseguramos la version de Gtk a usar

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Clase principal de la ventana
class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        # Inicializa la ventana principal
        super().__init__()
        self.set_title("Ejemplo con gtk Stack y StackSwitcher")

        # Contenedor principal en orientación vertical
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Creación del stack, un contenedor que alterna entre vistas
        stack = Gtk.Stack()
        # Configuración del tipo de transición entre vistas
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        # Duración de la transición en milisegundos
        stack.set_transition_duration(1500)

    # Primera vista: un CheckButton (botón de selección)
        chkPulsame = Gtk.CheckButton(label="Púlsame")
        # Se agrega al stack con un identificador y un título
        stack.add_titled(chkPulsame, "chk", "Check para pulsar")

    # Segunda vista: una etiqueta (Label) con formato
        lblEtiqueta = Gtk.Label()
        # Formato del texto usando Pango Markup
        lblEtiqueta.set_markup("<big> Una Etiqueta </big>")
        # Se agrega al stack con un identificador y un título
        stack.add_titled(lblEtiqueta, "lbl", "Etiqueta elegante")

    # Tercera vista: una etiqueta con formato
        lblEtiqueta2 = Gtk.Label("Otra etiqueta")
        # Agregar la etiqueta
        stack.add_titled(lblEtiqueta2, "lbl2", "Etiqueta secundaria")

        # Creación del StackSwitcher para cambiar entre vistas
        stack_switcher = Gtk.StackSwitcher()
        # Se asocia al stack creado anteriormente
        stack_switcher.set_stack(stack)

        # Agregar el StackSwitcher y el Stack al contenedor principal
        caixaV.pack_start(stack_switcher, True, True, 0)
        caixaV.pack_start(stack, True, True, 0)

        # Agregar el contenedor principal a la ventana
        self.add(caixaV)
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
