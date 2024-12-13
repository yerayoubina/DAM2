package model;

import net.bytebuddy.matcher.InheritedAnnotationMatcher;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "pokemon")
public class PokemonEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private int id;

    @Column(name = "nome", nullable = false, length = 50)
    private String nome;

    @Column(name = "nacemento")
    private java.sql.Date nacemento;

    @ManyToOne
    @JoinColumn(name = "PokedexEntry", referencedColumnName = "id")
    private PokedexEntity pokedextry;

    @ManyToOne
    @JoinColumn(name = "Adestrador", referencedColumnName = "id")
    private AdestradorEntity adestrador;

    public PokemonEntity(String nome) {
        this.nome = nome;
    }

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

    public Date getNacemento() {
        return nacemento;
    }

    public void setNacemento(java.sql.Date nacemento) {
        this.nacemento = nacemento;
    }

    public PokedexEntity getPokedextry() {
        return pokedextry;
    }

    public void setPokedextry(PokedexEntity pokedextry) {
        this.pokedextry = pokedextry;
    }

    public AdestradorEntity getAdestrador() {
        return adestrador;
    }

    public void setAdestrador(AdestradorEntity adestrador) {
        this.adestrador = adestrador;
    }

    public PokemonEntity() {
    }

    @Override
    public String toString() {
        return "PokemonEntity{" +
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", nacemento=" + nacemento +
                ", pokedextry=" + pokedextry +
                ", adestrador=" + adestrador +
                '}';
    }
}
