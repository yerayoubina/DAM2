package model;


import javax.persistence.*;

@Entity
@Table(name = "pokedex")
public class PokedexEntity {
    @Id
    @GeneratedValue(strategy =  GenerationType.IDENTITY)
    @Column(name = "id")
    private int id;

    @Column(name = "nome",  nullable = false, length = 50)
    private String nome;

    @Column(name = "peso",precision = 10, scale = 2)
    private double peso;

    @Column(name = "misc", columnDefinition = "TEXT")
    private String misc;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public String getMisc() {
        return misc;
    }

    public void setMisc(String misc) {
        this.misc = misc;
    }

    public PokedexEntity() {
    }

    public PokedexEntity(String nome, double peso, String misc) {
        this.nome = nome;
        this.peso = peso;
        this.misc = misc;
    }

    @Override
    public String toString() {
        return "PokedexEntity{" +
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", peso=" + peso +
                ", misc='" + misc + '\'' +
                '}';
    }
}
