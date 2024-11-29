package com.dam.conexionHIbernate;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.util.List;


public class ConsultaClientes {
    public static void main(String[] args) {
        listarApellidoODireccion();
    }

    private static void listarApellidoODireccion() {
        try (SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Clientes.class).buildSessionFactory();
            Session ss = sf.openSession()) {
            String hql = "from Clientes c where c.apellidos='Delgado'" + " or c.direccion='gran via'";
            List<Clientes> clientes = ss.createQuery(hql).getResultList();

            for(Clientes c : clientes){
                System.out.println(c);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private static void listarPorApellido() {
        //CREAR SESSION
        try (SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Clientes.class).buildSessionFactory();
        Session ss = sf.openSession()){
            ss.beginTransaction();

            List<Clientes> clientes =  ss.createQuery("from Clientes c where c.apellidos='Rey'").getResultList(); //hql -> mostrar apellido Rey c.apellidos (model)

            for(Clientes c : clientes){
                System.out.println(c);
            }

            ss.getTransaction().commit();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private static void listarClientes() {
        //CREAR SESSION
        try (SessionFactory sf = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Clientes.class).buildSessionFactory();
             Session ss = sf.openSession()){

            ss.beginTransaction();

            //Consulta clientes
            List<Clientes> clientes = ss.createQuery("from Clientes").getResultList();

            for(Clientes c : clientes){
                System.out.println(c);
            }

            //Guarda el estado
            ss.getTransaction().commit();
        }catch (Exception e){
            System.err.println(e.getMessage());
        }
    }

    }





