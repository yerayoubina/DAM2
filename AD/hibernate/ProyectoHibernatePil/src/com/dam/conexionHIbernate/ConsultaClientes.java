package com.dam.conexionHIbernate;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.util.List;


public class ConsultaClientes {
    public static void main(String[] args) {
        //CREAR SESSION
        try (SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Clientes.class).buildSessionFactory();
        Session ss = sf.openSession()){

            ss.beginTransaction();

            //Consulta clientes
            List<Clientes> clientes = ss.createQuery("from Clientes").getResultList();



        }
    }
}
