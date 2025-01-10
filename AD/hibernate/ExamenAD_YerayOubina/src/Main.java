import dao.CocheI;
import dao.CocheImpl;
import dao.MultasI;
import dao.MultasImp;
import entities.Coche;
import entities.Multas;
import util.SerializarOBJ;

import java.sql.SQLSyntaxErrorException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    /**
     * Atributos del main de apoyo para las operacioensw
     **/
    // DAOs
    static CocheI cocheDao = new CocheImpl();
    static MultasI multasDao = new MultasImp();


    // Ficheros
    static String fileSerializar = "SerializaCoches.ser";
    static String fileCochesXML = "Coches.xml";
    static String fileMultasXML = "Multas.xml";

    public static void main(String[] args) {

    /*
    Insertar na táboa Coche os seguintes coches: (recorda que os valores da PK son
        autoxerados)
        ('1234ABC', 'Toyota')
        ('5678XYZ', 'Ford')
     */

        // Crear coches e Insertar coches
        Coche c = new Coche();
        c.setMarca("toyota");
        c.setMarca("ford");
        cocheDao.insertarCoche(c);

        c.setMatricula("1234ABC");
        c.setMatricula("5678XY");
        cocheDao.insertarCoche(c);


        /*
        Consulta os IDs que teñen agora os coches e lístaos
         */
        List<Coche> coches = cocheDao.listaCoches();
        System.out.println("------ CONSULTA ID'S -------------");

        mostrarIdCoches(coches);

        /**
         * Inserta na táboa Multas as seguintes entradas:
         * (recorda que os valores da PK serán autoxerados, e os Ids dos coches foron autoxerados
         * tamén).
         */
        // Crear multas e insertar multas
        Multas m = new Multas();
        m.setIdCoche(coches.get(0).getId());
        m.setImporte(100.50);
        m.setPorcentaxeReduccion(10);
        multasDao.insertarMulta(m);

        m.setIdCoche(coches.get(1).getId());
        m.setImporte(100.50);
        m.setPorcentaxeReduccion(10);
        multasDao.insertarMulta(m);

        System.out.println("------ CONSULTA MULTAS -------------");

        mostrarMultas(multasDao.listaMultas());

        MultasImp multasXml = new MultasImp();
        System.out.println("------ EXPORTA XML -------------");


        multasXml.exportarAdestradoresToXML(fileMultasXML);


        // Serializar COCHES
        System.out.println("------SERIALIZA COCHES-------------");

        SerializarOBJ.serializarCoches(cocheDao.listaCoches(), fileSerializar);

        System.out.println("------REBAIZA POLICIAL------------");







    }


    private static void mostrarIdCoches(List<Coche> coches) {
        for (Coche c : coches) {
            System.out.println("Id: " + c.getId());
        }
    }

    private static void mostrarMultas(List<Multas> multas) {
        for (Multas m : multas) {
            System.out.println("Id: " + m.getId());
        }
    }


    /*
    ----------------------------------
    SERIALIZA
            SerializarOBJ.serializarCoches(dao.listaCoches(), "SerializaCoches.ser");

        List<Coche> lista = SerializarOBJ.deserializarLista("SerializaCoches.ser");
        for(Coche c : lista){
            System.out.println(c);
        }
-------------------------------------------------------

     */
}