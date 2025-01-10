package util;

import org.hibernate.SessionFactory;
import org.hibernate.boot.Metadata;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;

//ALTER SEQUENCE public.pokedex_id_seq RESTART WITH 1;
//ALTER SEQUENCE public.adestrador_id_seq RESTART WITH 1;

public class HibernateUtil {
    private static StandardServiceRegistry registry;
    private static SessionFactory sessionFactory;

    public static SessionFactory getSessionFactory() {
        try {
            //Crea registry
            registry = new StandardServiceRegistryBuilder().configure("resources/hibernate.cfg.xml").build();
            //Crea metadataSources
            MetadataSources sources = new MetadataSources(registry);
            //Crea Metadata
            Metadata metadata = sources.getMetadataBuilder().build();
            //Crea SessionFactory
            sessionFactory = metadata.getSessionFactoryBuilder().build();
            System.out.println("CONEXION EXITOSA");
        } catch (Exception e) {
            System.err.println("ERROR CONEXION" + e.getMessage());
            if (registry != null) StandardServiceRegistryBuilder.destroy(registry);
        }

        return sessionFactory;
    }

    public static void shutdown() {
        if (sessionFactory != null) {
            sessionFactory.close();
        }
        if (registry != null) {
            StandardServiceRegistryBuilder.destroy(registry);
        }
    }
}
