import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib  # Importar GLib correctamente

class MiVentana(Gtk.Window):
    def __init__(self):
        super().__init__(title="Mi App GTK Mejorada")

        # Configuración de la ventana principal
        self.set_default_size(500, 400)
        self.set_border_width(10)

        # Caja principal para los widgets
        self.box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        # Etiqueta inicial
        self.label = Gtk.Label(label="Introduce tu nombre:")
        self.box.pack_start(self.label, True, True, 0)

        # Campo de texto (Entrada de usuario)
        self.entry = Gtk.Entry()
        self.box.pack_start(self.entry, True, True, 0)

        # Botón para mostrar saludo
        self.button_saludo = Gtk.Button(label="Mostrar Saludo")
        self.button_saludo.connect("clicked", self.on_button_saludo_clicked)
        self.box.pack_start(self.button_saludo, True, True, 0)

        # Etiqueta para el saludo
        self.greeting_label = Gtk.Label(label="")
        self.box.pack_start(self.greeting_label, True, True, 0)

        # ComboBox para seleccionar un color
        self.combo_box = Gtk.ComboBoxText()
        self.combo_box.append_text("Rojo")
        self.combo_box.append_text("Verde")
        self.combo_box.append_text("Azul")
        self.combo_box.set_active(0)  # Establecer el color por defecto
        self.combo_box.connect("changed", self.on_combo_box_changed)
        self.box.pack_start(self.combo_box, True, True, 0)

        # Barra de progreso
        self.progress_bar = Gtk.ProgressBar()
        self.box.pack_start(self.progress_bar, True, True, 0)

        # Botón para iniciar una tarea simulada
        self.button_tarea = Gtk.Button(label="Iniciar Tarea")
        self.button_tarea.connect("clicked", self.on_button_tarea_clicked)
        self.box.pack_start(self.button_tarea, True, True, 0)

        # Botón para mostrar un cuadro de diálogo
        self.button_dialog = Gtk.Button(label="Abrir Cuadro de Diálogo")
        self.button_dialog.connect("clicked", self.on_button_dialog_clicked)
        self.box.pack_start(self.button_dialog, True, True, 0)

        # Botón para salir
        self.button_exit = Gtk.Button(label="Salir")
        self.button_exit.connect("clicked", Gtk.main_quit)
        self.box.pack_start(self.button_exit, True, True, 0)

        # Caja de texto multilinea
        self.text_view = Gtk.TextView()
        self.text_view.set_wrap_mode(Gtk.WrapMode.WORD)
        self.text_buffer = self.text_view.get_buffer()
        self.box.pack_start(self.text_view, True, True, 0)

        # Estado para la simulación de la tarea
        self.progress_value = 0

    def on_button_saludo_clicked(self, widget):
        """Actualizar el saludo con el texto ingresado."""
        nombre = self.entry.get_text()
        if nombre:
            self.greeting_label.set_text(f"Hola, {nombre}!")
        else:
            self.greeting_label.set_text("¡Hola, extraño!")

    def on_combo_box_changed(self, widget):
        """Actualizar el color de fondo según la selección del ComboBox."""
        color = self.combo_box.get_active_text()
        if color == "Rojo":
            self.modify_bg(Gtk.StateFlags.NORMAL, Gdk.Color(65535, 0, 0))
        elif color == "Verde":
            self.modify_bg(Gtk.StateFlags.NORMAL, Gdk.Color(0, 65535, 0))
        elif color == "Azul":
            self.modify_bg(Gtk.StateFlags.NORMAL, Gdk.Color(0, 0, 65535))

    def on_button_tarea_clicked(self, widget):
        """Simular una tarea con la barra de progreso."""
        self.progress_value = 0
        self.progress_bar.set_fraction(0)
        # Llamar a la función para actualizar la barra de progreso cada 100 ms
        self.update_progress()

    def update_progress(self):
        """Actualizar la barra de progreso simulando el avance de una tarea."""
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar.set_fraction(self.progress_value / 100.0)
            # Reprogramar la actualización después de 100ms usando GLib
            GLib.timeout_add(100, self.update_progress)  # Ahora usamos GLib.timeout_add
        else:
            self.progress_bar.set_fraction(1.0)
            self.append_text_to_textview("Tarea completada.\n")

    def on_button_dialog_clicked(self, widget):
        """Mostrar un cuadro de diálogo con opciones."""
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.YES_NO, "¿Deseas continuar?")
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            self.append_text_to_textview("El usuario ha aceptado continuar.\n")
        else:
            self.append_text_to_textview("El usuario ha rechazado continuar.\n")
        dialog.destroy()

    def append_text_to_textview(self, text):
        """Añadir texto al TextView."""
        self.text_buffer.insert_at_cursor(text)

# Crear y mostrar la ventana
ventana = MiVentana()
ventana.connect("destroy", Gtk.main_quit)
ventana.show_all()

# Iniciar el bucle principal de GTK
Gtk.main()
