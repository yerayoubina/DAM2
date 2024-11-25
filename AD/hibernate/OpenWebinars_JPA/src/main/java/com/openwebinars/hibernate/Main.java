package com.openwebinars.hibernate;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class Main {
    public static void main(String[] args) {
        // Crear un EntityManagerFactory
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("PrimerProyectoHibernateJPA");

        // Crear un EntityManager
        EntityManager em = emf.createEntityManager();

        // Usar el EntityManager (ejemplo, podrías empezar una transacción o consultar)
        em.getTransaction().begin();

        // Aquí irían tus operaciones de base de datos...

        em.getTransaction().commit(); // Confirmar la transacción
    }
}
