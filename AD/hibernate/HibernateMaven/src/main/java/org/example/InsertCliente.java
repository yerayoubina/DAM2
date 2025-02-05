package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class InsertCliente {

    public static void main(String[] args) {
        // Crear SessionFactory y vincularlo a un mapeo
        SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Cliente.class).buildSessionFactory();

        // Session
        Session ss = sf.openSession();

        //CREATE
        try {
            Cliente cliente1 = new Cliente("Jimmy", "Chicote", "Sagasta");
            ss.beginTransaction();
            ss.persist(cliente1);
            ss.getTransaction().commit();
            System.out.println("Cliente insertado en la base de datos");

            ss.beginTransaction();

            System.out.println("Lectura del registro con ID"+ cliente1.getId());

            Cliente clienteInsertado = ss.get(Cliente.class, cliente1.getId());

            System.out.println("Registro: " + clienteInsertado);

            ss.getTransaction().commit();

            System.out.println("Terminado!");
            ss.close();

        } catch (Exception e) {
            ss.getTransaction().rollback();
            ss.close();
            System.out.println(e.getMessage());
        }




    }





}
