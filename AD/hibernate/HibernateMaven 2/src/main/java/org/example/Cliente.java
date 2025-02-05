package org.example;


import jakarta.persistence.*;

@Entity
@Table(name ="clientes")
public class Cliente {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private int id;

    @Column(name = "nombre")
    private String nombre;

    @Column(name = "apellidos")
    private String apellidos;

    @Column(name = "direccion")
    private String direccion;

    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "id")
    private Detalles_cliente detalles_cliente;

    public Cliente(){}

    public Cliente(String nombre, String apellidos, String direccion) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.direccion = direccion;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public String getDicreccion() {
        return direccion;
    }

    public void setDicreccion(String dicreccion) {
        this.direccion = dicreccion;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public Detalles_cliente getDetalles_cliente() {
        return detalles_cliente;
    }

    public void setDetalles_cliente(Detalles_cliente detalles_cliente) {
        this.detalles_cliente = detalles_cliente;
    }

    @Override
    public String toString() {
        return "Cliente{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", apellidos='" + apellidos + '\'' +
                ", dicreccion='" + direccion + '\'' +
                '}';
    }
}
