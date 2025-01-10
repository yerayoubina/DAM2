package entities;

import javax.persistence.*;
import java.io.Serializable;

/**
 * Clase que representa la entidad Multas en la BBDD
 *
 **/
@Entity
@Table(name = "Multas")
public class Multas implements Serializable {

    /**
     * Registrar un Id para no tener problemas conla serialización
     **/
    private static final long serialVersionUID = 1L;

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "idCoche")
    private Integer idCoche;

    @Column(name = "importe", precision = 10, scale = 2)
    private Double importe;

    @Column(name = "porcentaxeReduccion")
    private Integer porcentaxeReduccion;

    /*
    @ManyToOne
    @MapsId("idCoche")
    @JoinColumn(name = "idCoche")
    private Coche coche;
    */


    /**
     * Getters, Setter y toString
     **/

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getIdCoche() {
        return idCoche;
    }

    public void setIdCoche(Integer idCoche) {
        this.idCoche = idCoche;
    }

    public Double getImporte() {
        return importe;
    }

    public void setImporte(Double importe) {
        this.importe = importe;
    }

    public Integer getPorcentaxeReduccion() {
        return porcentaxeReduccion;
    }

    public void setPorcentaxeReduccion(Integer porcentaxeReduccion) {
        this.porcentaxeReduccion = porcentaxeReduccion;
    }



    @Override
    public String toString() {
        return "Multas{" +
                "id=" + id +
                ", idCoche=" + idCoche +
                ", importe=" + importe +
                ", porcentaxeReduccion=" + porcentaxeReduccion +
                '}';
    }
}
