package com.dam.conexionHIbernate;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;


public class GuardaCliente {
    public static void main(String[] args) {
        try (SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Clientes.class).buildSessionFactory()) {
            Session ss = sf.openSession();

            Clientes c1 = new Clientes("Juan", "Diaz", "Gran via");

            ss.beginTransaction();
            ss.save(c1);
            ss.getTransaction().commit();

            System.out.println("Nuevo registro en la base de datos:\n "+  c1.toString());
            ss.close();
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
