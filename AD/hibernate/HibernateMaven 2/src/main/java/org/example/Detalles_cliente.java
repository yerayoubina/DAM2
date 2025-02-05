package org.example;


import jakarta.persistence.*;

@Entity
@Table(name ="detalles_cliente")
public class Detalles_cliente {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private int id;

    @Column(name = "web")
    private String web;

    @Column(name = "tfn")
    private String tfn;

    @Column(name = "comentarios")
    private String comentarios;

    @OneToOne(mappedBy = "detalles_cliente",cascade = CascadeType.ALL)
    @JoinColumn(name = "id")
    private Cliente cliente;

    public Detalles_cliente(){}

    public Detalles_cliente(String web, String tfn, String comentarios) {
        this.web = web;
        this.tfn = tfn;
        this.comentarios = comentarios;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getWeb() {
        return web;
    }

    public void setWeb(String web) {
        this.web = web;
    }

    public String getTfn() {
        return tfn;
    }

    public void setTfn(String tfn) {
        this.tfn = tfn;
    }

    public String getComentarios() {
        return comentarios;
    }

    public void setComentarios(String comentarios) {
        this.comentarios = comentarios;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    @Override
    public String toString() {
        return "Detalles_cliente{" +
                "web='" + web + '\'' +
                ", tfn='" + tfn + '\'' +
                ", comentarios='" + comentarios + '\'' +
                ", cliente=" + cliente.getNombre() +
                '}';
    }
}
