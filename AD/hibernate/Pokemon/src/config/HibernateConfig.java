package config;

import model.AdestradorEntity;
import model.PokedexEntity;
import model.PokemonEntity;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateConfig {
    private static SessionFactory sessionFactory;

    public static SessionFactory getSessionFactory() {
        if (sessionFactory == null) {
            try {
                // Cargar la configuración de Hibernate y construir la SessionFactory
                sessionFactory = new Configuration().configure("resources/properties.xml").buildSessionFactory();
            } catch (Exception e) {
                System.out.println("Error al crear la SessionFactory: " + e.getMessage());
                e.printStackTrace();
            }
        }
        return sessionFactory;
    }
}
