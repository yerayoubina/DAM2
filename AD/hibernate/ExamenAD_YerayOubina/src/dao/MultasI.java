package dao;

import entities.Coche;
import entities.Multas;

import java.util.List;

/**
 * Interfaz para declarar las implementaciones que ha de seguri el dao
 **/
public interface MultasI {

    void insertarMulta(Multas multa);

    List<Multas> listaMultas();

    List<Multas> findMultasByCoche(Coche coche);



    void deleteMultas();


}
