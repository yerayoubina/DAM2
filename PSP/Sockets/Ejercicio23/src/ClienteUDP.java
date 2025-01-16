import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.logging.Level;
import java.util.logging.Logger;


public class ClienteUDP{
    public static void main(String[] args) {
        String whoami = "Cliente : ";

        int puerto_servidor = 6666;
        byte[] bufferEviar;
        byte[] bufferRecibir = new byte[2048];
        try {
            InetAddress direccionServidor = InetAddress.getByName("localhost");
// Se crea el DatagramSocket sin especificar un puerto, lo que hace que el sistema asigne un puerto aleatorio.
// Esto es suficiente para recibir datagramas, ya que el servidor enviará los datos al puerto en el que el cliente está escuchando.
            DatagramSocket datagramSocket = new DatagramSocket();

            for (int i = 1; i <=3 ; i++){
                String msj = whoami + "Hola";
                bufferEviar = msj.getBytes();
                DatagramPacket pregunta = new DatagramPacket(bufferEviar, bufferEviar.length, direccionServidor, puerto_servidor);
                datagramSocket.send(pregunta);

                // Se crea un DatagramPacket con el tamaño de buffer especificado.
// Este paquete se utilizará para recibir los datos enviados por el cliente.
                DatagramPacket peticion = new DatagramPacket(bufferRecibir, bufferRecibir.length);

// Al ejecutar este método, el buffer se llena con el mensaje enviado por el cliente.
// Este método BLOQUEA la ejecución del código hasta que se reciba el paquete completo.
// Si el mensaje enviado es más grande que el tamaño del buffer, el mensaje se truncará.
                datagramSocket.receive(peticion);

// Convierte el contenido del buffer recibido en un String para poder procesarlo.
                String msjServidor = new String(peticion.getData(),0,peticion.getLength());

                System.out.println(msjServidor);
            }

        } catch (SocketException ex) {
            ex.getMessage();
        } catch (IOException ex) {
            Logger.getLogger(ClienteUDP.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
