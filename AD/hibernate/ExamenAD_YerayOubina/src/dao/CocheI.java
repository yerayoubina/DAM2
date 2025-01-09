package dao;


import entities.Coche;

import java.util.List;

/**
 * Interfaz para declarar las implementaciones que ha de seguri el dao
 **/
public interface CocheI {

    void insertarCoche(Coche coche);

    List<Coche> listaCoches();

    Coche findCocheById(Integer id);

    Coche findCocheByMatricula(String matricula);

    void deleteCoches();

    void updateCoche(Coche coche);


}
