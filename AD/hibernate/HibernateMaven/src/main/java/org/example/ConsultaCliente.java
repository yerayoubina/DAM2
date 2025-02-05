package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.util.List;

public class ConsultaCliente {
    public static void main(String[] args) {

        Session ss = null;
        try (SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Cliente.class).buildSessionFactory()) {
            // Sesion
            ss = sf.openSession();
            ss.getTransaction();

            //Lista = HQL
            List<Cliente> clientes = ss.createQuery("FROM Cliente", Cliente.class).getResultList();


            //mostrar los clientes
            mostrarClientes(clientes);

            //Lista Paco
            clientes = ss.createQuery("FROM Cliente c WHERE c.nombre = 'Paco'", Cliente.class).getResultList();
            System.out.println("PACOS_---");
            mostrarClientes(clientes);

            //lista los de la calle Gran Vía
            clientes = ss.createQuery("FROM Cliente c WHERE c.direccion = 'Gran via '", Cliente.class).getResultList();
            System.out.println("DE GRAN VIA---");

            mostrarClientes(clientes);

            ss.getTransaction().commit();
            ss.close();
            } catch (Exception e) {
            assert ss != null;
            ss.getTransaction().rollback();
            ss.close();
            System.out.println(e.getMessage());
        }


    }

    private static void mostrarClientes(List<Cliente> clientes) {
        for (Cliente c : clientes) {
            System.out.println(c);
        }
    }
}
