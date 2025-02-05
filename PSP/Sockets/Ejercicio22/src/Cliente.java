import java.io.*;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Cliente implements Runnable{

    @Override
    public void run() {
        operacionCliente();
    }

    private static void operacionCliente() {
        try {
            System.out.print("Estableciendo la conexión al servidor ");

            // Simula tiempo
            temporizador(2500);

            //Realiza la conexión
            Socket clientSocket = new Socket();
            InetSocketAddress addr = new InetSocketAddress("localhost", 6666);
            clientSocket.connect(addr);

            // Streams enlazados al socket
            ObjectOutputStream oos = new ObjectOutputStream(clientSocket.getOutputStream());
            ObjectInputStream ois = new ObjectInputStream(clientSocket.getInputStream());

            //Usuario añade numeros a la lista
            List<Integer> lista = pedirNumeros(4);

            //Lista al servidor
            oos.writeObject(lista); // enviar
            oos.flush(); //liberar

            progresoOperacionServidor();

            //Leer lista del servidor y mostrar
            System.out.println("\nRESULTADO -> " + (Integer) ois.readObject());

            //Closes
            ois.close();
            oos.close();
            clientSocket.close();

            System.out.println("\nBye, bye");

        } catch (IOException | ClassNotFoundException | InterruptedException ex) {
            System.err.println(ex.getMessage());
        }
    }

    /**
     * Se ha hecho a modo experimental. Simula un progreso del cálculo
     */
    private static void progresoOperacionServidor() throws InterruptedException {
        System.out.println("Enviada operación al servidor");

        for(int i = 1; i <= 100; i++){
                Thread.sleep(25);
                System.out.print("\r Calculando suma " + i + "%");
        }
    }

    /**
     * Esta función simula un temporizador para dar la sensación de que la conexión al servidor es un proceso costoso. A su vez garatinza que la petición del cliente no se establezca antes de que el servidor esté disponible.
     * @param milisegundos tiempo de espera
     */
    private static void temporizador(long milisegundos) throws InterruptedException {
        long tiempoInicial = System.currentTimeMillis();
        while(System.currentTimeMillis() - tiempoInicial < milisegundos){
            Thread.sleep(200);
            System.out.print(".");
        }
    }

    /**
     * Pedir número por consola
     * @param nVeces Las veces que el usuario interactua
     * @return List<Integer>
     */
    private static List<Integer> pedirNumeros(int nVeces) throws InterruptedException {
        Scanner sc = new Scanner(System.in);
        List<Integer> lista = new ArrayList<>();

        while (lista.size() < nVeces) {
            System.out.print(lista.size() + 1 +  ") Añade número entero: ");
            if(sc.hasNextInt()){
                lista.add(sc.nextInt());
            }else {
                System.err.println("El dato introducido no es un número entero");
                sc.next();
                Thread.sleep(100); // Dar margen a la salida del error
            }
        }
        sc.close();
        return lista;
    }
}
