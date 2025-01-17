
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;


public class ServidorUDP implements Runnable{
    @Override
    public void run() {
        int puerto = 6666;
        byte[] bufferRecibir = new byte[1024];
        byte[] bufferEnviar ;
        try {
            System.out.println("Servidor arrancando --------");

            //Crear el socker del servidor y asociarlo al puerto
            DatagramSocket datagramSocket = new DatagramSocket(puerto);

            //Preparar para recibir paquete
            DatagramPacket peticion = new DatagramPacket(bufferRecibir, bufferRecibir.length);
            datagramSocket.receive(peticion);

            //Procesar el mensaje recibido
            String msj = new String(peticion.getData(), 0 , peticion.getLength());
            System.out.println("Servidor: " + msj);

            //Obetener la informacion del cliente
            int puertoCliente = peticion.getPort();
            InetAddress direccion = peticion.getAddress();

            //Enviar la respuesta
            String msjServidor = "Mensaje 1 desde el servidor";
            bufferEnviar = msjServidor.getBytes();
            DatagramPacket respuesta = new DatagramPacket(bufferEnviar, bufferEnviar.length, direccion, puertoCliente);

            // Enviar la respuesta al cliente
            datagramSocket.send(respuesta);

            datagramSocket.close();

        } catch (SocketException ex) {
            ex.printStackTrace();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
