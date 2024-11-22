import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class TodoApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Todo")
        self.set_border_width(10)
        self.set_default_size(300, 200)

        # Contenedor principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # ListStore para almacenar las tareas
        self.todo_liststore = Gtk.ListStore(str)
        self.todo_treeview = Gtk.TreeView(model=self.todo_liststore)

        # Columna para mostrar las tareas
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Tasks", renderer, text=0)
        self.todo_treeview.append_column(column)
        self.todo_treeview.set_headers_visible(False)

        # Añadir TreeView al contenedor
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_min_content_height(150)
        scrolled_window.add(self.todo_treeview)
        vbox.pack_start(scrolled_window, True, True, 0)

        # Botones
        button_box = Gtk.Box(spacing=6)
        vbox.pack_start(button_box, False, False, 0)

        self.add_button = Gtk.Button(label="Add Todo")
        self.add_button.connect("clicked", self.on_add_todo)
        button_box.pack_start(self.add_button, True, True, 0)

        self.delete_button = Gtk.Button(label="Delete")
        self.delete_button.connect("clicked", self.on_delete_todo)
        button_box.pack_start(self.delete_button, True, True, 0)

        self.complete_button = Gtk.Button(label="Complete")
        self.complete_button.connect("clicked", self.on_complete_todo)
        button_box.pack_start(self.complete_button, True, True, 0)

        # Input para añadir tareas
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Escribe aquí...")
        vbox.pack_start(self.entry, False, False, 0)

    def on_add_todo(self, button):
        text = self.entry.get_text()
        if text.strip():
            self.todo_liststore.append([text])
            self.entry.set_text("")

    def on_delete_todo(self, button):
        selection = self.todo_treeview.get_selection()
        model, treeiter = selection.get_selected()
        if treeiter:
            model.remove(treeiter)

    def on_complete_todo(self, button):
        selection = self.todo_treeview.get_selection()
        model, treeiter = selection.get_selected()
        if treeiter:
            completed_task = model[treeiter][0] + " (completed)"
            model[treeiter][0] = completed_task


# Ejecutar la aplicación
if __name__ == "__main__":
    app = TodoApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
