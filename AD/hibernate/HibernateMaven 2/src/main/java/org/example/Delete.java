package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class Delete {
    public static void main(String[] args) {

        SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").buildSessionFactory();

        Session ss = null;

        try{
            /*

             */
            ss = sf.openSession();
            ss.beginTransaction();

            Cliente c = ss.get(Cliente.class, 31);
            Detalles_cliente cd = ss.get(Detalles_cliente.class, 1);

            if(c!=null){
                ss.remove(c);
                System.out.println("<-- Cliente ELIMINADO -->");
            }else {
                System.out.println("<-- NO SE HA PODIDO ACCEDER AL CLIENTE -->");

            }

            if(cd!=null){
                ss.remove(cd);
                System.out.println("<-- DETALLE-CLIENTE ELIMINADO -->");
            }else {
                System.out.println("<-- NO SE HA PODIDO ACCEDER AL DETALLE CLIENTE -->");

            }


            ss.getTransaction().commit();
            ss.close();
        }catch (Exception e){
            System.out.println(e.getMessage());
            assert ss != null;
            ss.close();
        }
    }
}
