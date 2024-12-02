import dao.PokedexDao;
import model.PokedexEntity;
import model.PokemonEntity;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        PokemonEntity pikachu = new PokemonEntity("Pikachu");
        PokedexDao pokedex = new PokedexDao();
        pokedex.listarPokemons();
    }


    public static void menu() {
        int opt;
        do {
            System.out.println("SELECCIONE UNA OPCION");
            System.out.println("1- INTRODUCIR POKEMON");
            System.out.println("2- LISTAR POKEMONS");
            System.out.println("3- SALIR");

            opt = new Scanner(System.in).nextInt();

            switch (opt) {
                case 1 -> {  //todo;
                }
            }
        } while (opt != 3);


    }
}