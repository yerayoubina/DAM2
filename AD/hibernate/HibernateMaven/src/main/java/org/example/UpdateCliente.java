package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class UpdateCliente {

    public static void main(String[] args) {
        // Crear SessionFactory y vincularlo a un mapeo
        SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Cliente.class).buildSessionFactory();

        // Session
        Session ss = sf.openSession();

        //CREATE
        try {
            //int clienteID = 1;

            ss.beginTransaction();

            //Cliente c = ss.get(Cliente.class, clienteID);

            //c.setApellidos("Gutierrez");

            ss.createMutationQuery("DELETE Cliente WHERE id = 3").executeUpdate();

            ss.getTransaction().commit();


            System.out.println("Terminado!");
            ss.close();

        } catch (Exception e) {

            ss.close();
            System.out.println(e.getMessage());
        }




    }





}
