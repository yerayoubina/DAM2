import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;

public class Servidor {
    public static void main(String[] args) {
        try {
            System.out.println("Creando socket servidor");
            ServerSocket serverSocket = new ServerSocket();

            System.out.println("Realizando el bind");
            InetSocketAddress addr = new InetSocketAddress("localhost", 6666);
            serverSocket.bind(addr);

            System.out.println("Aceptando conexiones");
            Socket newSocket = serverSocket.accept();

            System.out.println("Conexión recibida");
            InputStream is = newSocket.getInputStream();
            OutputStream os = newSocket.getOutputStream();

            for (int i = 1; i <= 3; i++) {
                byte[] mensaje = new byte[100];

                is.read(mensaje);

                System.out.println("Mensaje reci------------------------bido: " + new String(mensaje).trim());
                String respuesta = "Mensaje " + i + " desde servidor";
                os.write(respuesta.getBytes());

                System.out.println("- Mensaje enviado: " + respuesta);
            }

            System.out.println("Cerrando el nuevo socket");
            newSocket.close();
            System.out.println("Cerrando el socket servidor");
            serverSocket.close();
            System.out.println("Terminado");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}