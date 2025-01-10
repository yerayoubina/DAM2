import java.io.IOException;
import java.net.PortUnreachableException;
import java.net.ServerSocket;
import java.net.Socket;

public class Servidor {
    public static void main(String[] args) {
        int puerto = 7080; // Puerto en el que el servidor escuchará

       try(ServerSocket serverSocket = new ServerSocket(puerto)){
           System.out.println("Servidor escuchando en el puerto " + puerto);
           Socket socket = serverSocket.accept();
           System.out.println("Cliente conectado");

           socket.close();

       } catch (IOException e) {
           throw new RuntimeException(e);
       }
    }
}
