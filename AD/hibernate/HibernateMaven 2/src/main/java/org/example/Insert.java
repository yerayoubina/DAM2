package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class Insert {
    public static void main(String[] args) {

        SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").buildSessionFactory();

        Session ss = null;

        try{
            ss = sf.openSession();

            Cliente c1 = new Cliente("Manuel", "guimarey", "Barbon");
            Detalles_cliente cDetalles = new Detalles_cliente("www.pildoras.com", "777373","Es Profesor");

            //Asociar objetos
            c1.setDetalles_cliente(cDetalles);

            ss.beginTransaction();
            ss.persist(c1);

            ss.getTransaction().commit();
            System.out.println("<-- Cliente insertado -->");
            ss.close();
        }catch (Exception e){
            System.out.println(e.getMessage());
            assert ss != null;
            ss.close();
        }
    }
}
