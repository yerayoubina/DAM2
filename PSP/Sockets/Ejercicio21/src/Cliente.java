import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.Scanner;

public class Cliente {
    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);

            System.out.println("Creando socket cliente");
            Socket clientSocket = new Socket();

            System.out.println("Estableciendo la conexión");
            InetSocketAddress addr = new InetSocketAddress("localhost", 6666);

            clientSocket.connect(addr);
            InputStream is = clientSocket.getInputStream();
            OutputStream os = clientSocket.getOutputStream();

            for (int i = 1; i <= 3; i++) {
                String mensaje = sc.nextLine(); // mensaje a mandar
                os.write(mensaje.getBytes());   // mandar mensaje a través del outputStream
                System.out.println("- Mensaje enviado: " +"Mensaje " + i + " desde cliente ->  " +  mensaje);

                byte[] respuesta = new byte[100]; // almacenamiento para la respuesta del servidor
                is.read(respuesta); // leer respuesta del servidor
                System.out.println("- Respuesta recibida: " + new String(respuesta).trim() + "\n");
            }

            System.out.println("\nCerrando el socket cliente");
            clientSocket.close();
            System.out.println("Terminado");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}