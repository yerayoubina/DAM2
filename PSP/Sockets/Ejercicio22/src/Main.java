public class Main {
    public static void main(String[] args) {

        /*
         *  Se representa un escenario de cliente servidor a través de dos hilos que interactúan dicha petición
         *
         */

        Thread serverHilo = new Thread(new Servidor());
        Thread clienteHilo = new Thread(new Cliente());

        serverHilo.start();
        clienteHilo.start();

    }
}