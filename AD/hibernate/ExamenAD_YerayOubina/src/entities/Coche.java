package entities;


import javax.persistence.*;
import java.io.Serializable;

/**
 * Clase que representa la entidad Coche en la BBDD
 *
**/
@Entity
@Table(name = "coche")
public class Coche implements Serializable {

    /**
     * Registrar un Id para no tener problemas conla serialización
 **/
    private static final long serialVersionUID = 1L;

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "matricula", length = 255)
    private String matricula;

    @Column(name = "marca", length = 255)
    private String marca;



    /**
     * Constructor vacío para implementar funcionalidades con su respectivo DAO
     **/
    public Coche(){}

    /**
     * Getters, Setter y toString
     **/
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    @Override
    public String toString() {
        return "Coche{" +
                "id=" + id +
                ", matricula='" + matricula + '\'' +
                ", marca='" + marca + '\'' +
                '}';
    }
}
