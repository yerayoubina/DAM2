import java.io.IOException;
import java.net.Socket;

public class Cliente {
    public static void main(String[] args) {
        String host = "localhost";
        int puerto = 7080;

        try(Socket socket = new Socket(host, puerto)){
            System.out.println("Conexión establecida con el servidor");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
