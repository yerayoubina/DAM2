package dao;

import config.HibernateConfig;
import model.PokedexEntity;
import model.PokemonEntity;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.util.List;

public class PokedexDao {

    public void insertarPokemon(PokemonEntity pokemon){
        try (Session session = HibernateConfig.getSessionFactory().openSession()) {
            Transaction transaction = session.beginTransaction();
            session.save(pokemon);
            transaction.commit();
        } catch (Exception e) {
            System.out.println("Error al crear el pokemon: " + e.getMessage());
        }
    }

    public void listarPokemons() {
        try (Session session = HibernateConfig.getSessionFactory().openSession()) {
            String hql = "FROM PokemonEntity";
            List<PokemonEntity> pokemons = session.createQuery(hql, PokemonEntity.class).getResultList();

            for (PokemonEntity p : pokemons) {
                System.out.println(p.getNome());
            }
        } catch (Exception e) {
            System.err.println("Error al listar los pokemons: " + e.getMessage());
        }
    }
}
