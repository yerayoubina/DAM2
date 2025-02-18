import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.Arrays;
import java.util.Map;
import java.util.TreeMap;


public class ServidorUDP implements Runnable {
    @Override
    public void run() {
        int puerto = 6666;
        byte[] bufferRecibir = new byte[1024];
        byte[] bufferEnviar;
        try {
            System.out.println("Servidor arrancando --------");

            //Crear el socker del servidor y asociarlo al puerto
            DatagramSocket datagramSocket = new DatagramSocket(puerto);
            //Preparar para recibir paquete

            DatagramPacket peticion = new DatagramPacket(bufferRecibir, bufferRecibir.length);
            datagramSocket.receive(peticion);

            //Procesar el mensaje recibido
            String msj = new String(peticion.getData(), 0, peticion.getLength());

            //Determinar la plabra más larga (recorrer Array de msj y ternario para acutalizar el pMaxLength)
                String pMaxLength = "";
            for (String p : msj.split(",")) {
                pMaxLength = pMaxLength.length() < p.length() ? p : pMaxLength ;
            }

            System.out.println("Servidor -> Enviada Palabra más larga de " + Arrays.toString(msj.split(",")));

            //Obetener la informacion del cliente
            int puertoCliente = peticion.getPort();
            InetAddress direccion = peticion.getAddress();

            //Enviar la respuesta
            String msjServidor = "Palabra más larga " + pMaxLength + " - Longitud: " + pMaxLength.length();
            bufferEnviar = msjServidor.getBytes();
            DatagramPacket respuesta = new DatagramPacket(bufferEnviar, bufferEnviar.length, direccion, puertoCliente);

            // Enviar la respuesta al cliente y cerrar
            datagramSocket.send(respuesta);
            datagramSocket.close();
        } catch (IOException ex) {
            ex.getMessage();
        }
    }


}
