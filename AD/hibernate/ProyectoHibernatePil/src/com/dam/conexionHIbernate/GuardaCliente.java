package com.dam.conexionHIbernate;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;


public class GuardaCliente {
    public static void main(String[] args) {
        try (SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Clientes.class).buildSessionFactory()) {
            Session ss = sf.openSession();

            Clientes c1 = new Clientes("Pondal", "Delgado", "Julian");

            ss.beginTransaction();
            ss.save(c1);
            ss.getTransaction().commit();

            //System.out.println("Nuevo registro en la base de datos:\n "+  c1.toString());

            //LECTURA REGISTRO
            Clientes clienteInsertado = ss.get(Clientes.class, c1.getId());
            System.out.println("Registro: " + clienteInsertado);
            ss.getTransaction().commit();
            System.out.println("TERMINADO");

            ss.close();
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
