package dao;

import entities.Coche;
import org.hibernate.PersistentObjectException;
import org.hibernate.Session;
import util.HibernateUtil;

import javax.persistence.PersistenceException;
import javax.persistence.criteria.*;
import java.util.List;


/**
 * Clase DAO donde se implementa la interfaz correspondiente para realizar la lógica CRUD
 **/

public class CocheImpl implements CocheI {
    @Override
    public void insertarCoche(Coche coche) {
        try (Session ss = HibernateUtil.getSessionFactory().openSession()) {
            ss.beginTransaction();
            ss.save(coche);
            ss.getTransaction().commit();

            //INFO
            System.out.println("------ SE HA INSERTADO EL COCHE-------------\n\t" + coche.toString());

        } catch (PersistentObjectException e) {
            System.err.println("ERROR CREANDO COCHE: " + e.getMessage());
        }

    }

    @Override
    public List<Coche> listaCoches() {

        //INFO
        System.out.println("------ METODO listaCoches() -------------");

        try (Session ss = HibernateUtil.getSessionFactory().openSession()) {
            // 1. CriteraBuilder y Query
            CriteriaBuilder cb = ss.getCriteriaBuilder();
            CriteriaQuery<Coche> query = cb.createQuery(Coche.class);
            Root<Coche> root = query.from(Coche.class);

            // 2. Devuelme una lista con la consulta
            return ss.createQuery(query).list();
        } catch (Exception e) {
            System.err.println("ERROR LISTANDO COCHES" + e.getMessage());
            return null;
        }
    }

    @Override
    public Coche findCocheById(Integer id) {
        //INFO
        System.out.println("------ METODO findCocheById() -------------");

        try (Session ss = HibernateUtil.getSessionFactory().openSession()) {

            try {
                // 1. criteria
                CriteriaBuilder cb = ss.getCriteriaBuilder();
                CriteriaQuery<Coche> query = cb.createQuery(Coche.class);
                Root<Coche> root = query.from(Coche.class);
                // 2. Query
                Predicate filter = cb.equal(root.get("id"), id);

                // Devuelve un único Coche
                return ss.createQuery(query.where(filter)).getSingleResult();
            } catch (PersistenceException e) {
                System.err.println("ERROR BUSCANDO COCHE POR ID: " + e.getMessage());
                return null;
            }
        }
    }


    @Override
    public Coche findCocheByMatricula(String matricula) {
        //INFO
        System.out.println("------ METODO findCocheByMatricula() -------------");

        try (Session ss = HibernateUtil.getSessionFactory().openSession()) {

            try {
                // 1. criteria
                CriteriaBuilder cb = ss.getCriteriaBuilder();
                CriteriaQuery<Coche> query = cb.createQuery(Coche.class);
                Root<Coche> root = query.from(Coche.class);
                // 2. Query
                Predicate filter = cb.equal(root.get("matricula"), matricula);

                // Devuelve un único Coche
                return ss.createQuery(query.where(filter)).getSingleResult();
            } catch (PersistenceException e) {
                System.err.println("ERROR BUSCANDO COCHE POR MATRICULA: " + e.getMessage());
                return null;
            }
        }
    }

    @Override
    public void deleteCoches() {
        //INFO
        System.out.println("------ METODO deleteCoches() -------------");

        try (Session ss = HibernateUtil.getSessionFactory().openSession()) {

            try {

                ss.beginTransaction();

                // 1. criteria
                CriteriaBuilder cb = ss.getCriteriaBuilder();

                CriteriaDelete<Coche> delete = cb.createCriteriaDelete(Coche.class);

                Root<Coche> root = delete.from(Coche.class);

                // 2. Ejecuta delete
                ss.createQuery(delete).executeUpdate();
                ss.getTransaction().commit();

                System.out.println("SE HA ELIMINADO TODOS LOS REGISTROS");
            } catch (PersistenceException e) {
                System.err.println("ERROR ELIMINANDO TODOS LOS VEHICULOS: " + e.getMessage());
            }
        }
    }


    @Override
    public void updateCoche(Coche coche) {
        /*
            Session ss = HibernateUtil.getSessionFactory().openSession();

        try{
            ss.beginTransaction();

            //1.Criteria
            CriteriaBuilder cb = ss.getCriteriaBuilder();
            CriteriaUpdate<Coche> query= cb.createCriteriaUpdate(Coche.class);
            Root<Coche> root = query.from(Coche.class);

            //2. valores y condicion
            Predicate filter = cb.equal(root.get("id"), coche.getId());

            query.set("", coche.getNome())
                    .set("nacemento", adestrador.getNacemento())
                    .where(filter);
            //Ejecuta
            ss.createQuery(query).executeUpdate();
            ss.getTransaction().commit();
            return adestrador;
        }catch (PersistenceException e){
            System.err.println("ERROR UPDATE: " + e.getMessage());
            ss.getTransaction().rollback();
            return null;
        }finally {
            ss.close();
        }
    }
    */

        }


}
