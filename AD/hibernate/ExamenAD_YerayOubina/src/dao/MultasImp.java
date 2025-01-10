package dao;

import entities.Coche;
import entities.Multas;
import org.hibernate.PersistentObjectException;
import org.hibernate.Session;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import util.HibernateUtil;

import javax.persistence.PersistenceException;
import javax.persistence.criteria.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;
import java.util.List;


/**
 * Clase DAO donde se implementa la interfaz correspondiente para realizar la lógica CRUD
 **/

public class MultasImp implements MultasI {



    @Override
    public void insertarMulta(Multas multa) {
        try (Session ss = HibernateUtil.getSessionFactory().openSession()) {
            ss.beginTransaction();
            ss.save(multa);
            ss.getTransaction().commit();

            //INFO
            System.out.println("------ SE HA INSERTADO MULTA-------------\n\t" + multa.toString());

        } catch (PersistentObjectException e) {
            System.err.println("ERROR CREANDO MULTA: " + e.getMessage());
        }

    }

    @Override
    public List<Multas> listaMultas() {

            //INFO
            System.out.println("------ METODO listaMultas() -------------");

            try (Session ss = HibernateUtil.getSessionFactory().openSession()) {
                // 1. CriteraBuilder y Query
                CriteriaBuilder cb = ss.getCriteriaBuilder();
                CriteriaQuery<Multas> query = cb.createQuery(Multas.class);
                Root<Multas> root = query.from(Multas.class);

                // 2. Devuelme una lista con la consulta
                return ss.createQuery(query).list();
            } catch (Exception e) {
                System.err.println("ERROR LISTANDO Multas" + e.getMessage());
                return null;
            }
    }

    @Override
    public List<Multas> findMultasByCoche(Coche coche) {
        return null;
    }

    @Override
    public void deleteMultas() {
        //INFO
        System.out.println("------ METODO deleteMultas() -------------");

        try (Session ss = HibernateUtil.getSessionFactory().openSession()) {

            try {

                ss.beginTransaction();

                // 1. criteria
                CriteriaBuilder cb = ss.getCriteriaBuilder();

                CriteriaDelete<Multas> delete = cb.createCriteriaDelete(Multas.class);

                Root<Multas> root = delete.from(Multas.class);

                // 2. Ejecuta delete
                ss.createQuery(delete).executeUpdate();
                ss.getTransaction().commit();

                System.out.println("SE HA ELIMINADO TODOS LOS REGISTROS");
            } catch (PersistenceException e) {
                System.err.println("ERROR ELIMINANDO TODOS LAS MULTAS: " + e.getMessage());
            }
        }
    }

    public void exportarAdestradoresToXML(String filePath) {
        try {
            //Genera list
            MultasI dao = new MultasImp();
            List<Multas> multas = dao.listaMultas();

            // Crear el documento XML
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.newDocument();

            // Nodo raíz
            Element rootElement = doc.createElement("Multas");
            doc.appendChild(rootElement);

            // Añadir los registros como nodos XML
            for (Multas a : multas) {
                Element multaElement = doc.createElement("Multa");

                Element id = doc.createElement("Id");
                id.appendChild(doc.createTextNode(String.valueOf(a.getId())));
                multaElement.appendChild(id);

                Element idCoche = doc.createElement("idCoche");
                idCoche.appendChild(doc.createTextNode(String.valueOf(a.getIdCoche())));
                multaElement.appendChild(idCoche);

                Element importe = doc.createElement("importe");
                importe.appendChild(doc.createTextNode(String.valueOf(a.getImporte())));
                multaElement.appendChild(importe);

                Element porcentaxeReduccion = doc.createElement("porcentaxeReduccion");
                importe.appendChild(doc.createTextNode(String.valueOf(a.getImporte())));
                multaElement.appendChild(porcentaxeReduccion);

                rootElement.appendChild(multaElement);
            }

            // Escribir el contenido del XML en un archivo
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File(filePath));

            transformer.transform(source, result);

            System.out.println("Archivo XML generado en: " + filePath);
        } catch (Exception e) {
            System.err.println("Error al exportar a XML: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
