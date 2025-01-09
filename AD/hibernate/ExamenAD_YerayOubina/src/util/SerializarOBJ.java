package util;

import entities.Coche;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.List;

public class SerializarOBJ {

    public static <T> void serializarLista(List<T> lista, String fileName) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(lista);
            System.out.println("Lista serializada con éxito en: " + fileName);
        } catch (Exception e) {
            System.err.println("ERROR SERIALIZANDO " + e.getMessage());
        }
    }

    public static void serializarCoches(List<Coche> lista, String fileName) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(lista);
            System.out.println("Lista serializada con éxito en: " + fileName);
        } catch (Exception e) {
            System.err.println("ERROR SERIALIZANDO " + e.getMessage());
        }
    }

    public static <T> List<T> deserializarLista(String fileName) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            List<T> lista = (List<T>) ois.readObject();
            System.out.println("Lista deserializada con éxito desde: " + fileName);
            return lista;
        } catch (Exception e) {
            System.err.println("ERROR DESERIALIZANDO " + e.getMessage());
            return null;
        }
    }




}
