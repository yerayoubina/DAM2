import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.Scanner;

public class Cliente {
    public static void main(String[] args) {
        try {
            System.out.println("Creando socket cliente");
            Socket clientSocket = new Socket();

            System.out.println("Estableciendo la conexión");
            InetSocketAddress addr = new InetSocketAddress("localhost", 6666);

            clientSocket.connect(addr);
            InputStream is = clientSocket.getInputStream();
            OutputStream os = clientSocket.getOutputStream();

            for (int i = 1; i <= 3; i++) {
                Scanner sc = new Scanner(System.in);

                String mensaje = "Mensaje " + i + " desde cliente ->  " + sc.nextLine();

                os.write(mensaje.getBytes());

                System.out.println("\n- Mensaje enviado: " + mensaje);

                byte[] respuesta = new byte[100];
                is.read(respuesta);

                System.out.println("- Respuesta recibida: " + new String(respuesta).trim());
            }

            System.out.println("\nCerrando el socket cliente");
            clientSocket.close();
            System.out.println("Terminado");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}