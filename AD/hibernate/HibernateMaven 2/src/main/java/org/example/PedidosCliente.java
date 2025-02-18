package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.hibernate.collection.spi.PersistentIdentifierBag;

import java.util.Date;

public class PedidosCliente {
    public static void main(String[] args) {

        SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").buildSessionFactory();

        Session ss = null;

        try{
            ss = sf.openSession();
            ss.beginTransaction();

            Cliente c1 = ss.get(Cliente.class, 2); // obtener cliente base datos

            //Crear pedidos cliente
            Pedido p = new Pedido();
            p.setFecha(new Date(123,12,1));

            c1.addPedido(p);

            ss.persist(p);
            ss.getTransaction().commit();
            System.out.println("<-- PEDIDO insertado -->");
            ss.close();
        }catch (Exception e){
            System.out.println(e.getMessage());
            assert ss != null;
            ss.close();
        }
    }
}
