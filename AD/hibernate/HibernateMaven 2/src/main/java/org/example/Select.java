package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.hibernate.id.Configurable;

public class Select {
    public static void main(String[] args) {

        try (SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").buildSessionFactory()) {
            Session ss = sf.openSession();

            // Obtener detalles_cliente
            Detalles_cliente dc = ss.get(Detalles_cliente.class, 1);

            System.out.println(dc);

            System.out.println(dc.getCliente() );


            // Close the session
            ss.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}


