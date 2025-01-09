import java.io.*;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.DoubleSummaryStatistics;
import java.util.List;

public class Servidor implements  Runnable{

    @Override
    public void run() {
        try {
            // Sockets
            ServerSocket serverSocket = new ServerSocket();
            InetSocketAddress addr = new InetSocketAddress("localhost", 6666);
            serverSocket.bind(addr);
            Socket newSocket = serverSocket.accept();

            System.out.println(" CONEXION RECIBIDA!!!");

            //Streams
            ObjectOutputStream oos = new ObjectOutputStream(newSocket.getOutputStream());
            ObjectInputStream ois = new ObjectInputStream(newSocket.getInputStream());

            //Leer ArrayList
            List<Integer> listaRecibida = (List<Integer>) ois.readObject();


            //Operar con stream y enviar suma
            oos.writeObject(listaRecibida.stream().mapToInt(Integer::intValue).sum());

            //Closes
            ois.close();
            oos.close();
            newSocket.close();
            serverSocket.close();
        } catch (IOException | ClassNotFoundException e) {
            System.err.println(e.getMessage());
        }
    }
}