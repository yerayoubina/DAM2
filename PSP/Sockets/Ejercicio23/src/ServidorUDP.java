import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;


public class ServidorUDP {
    public static void main(String[] args) {
        String whoami = "Servidor";
        int puerto = 6666;
        byte[] buffer = new byte[2048]; //Almacena los datos recibidos
        try {
            System.out.println("Servidor arrancando");
    // El constructor crea un DatagramSocket y lo asocia (o "vincula") al puerto especificado.
            DatagramSocket datagramSocket = new DatagramSocket(puerto);

            for(int i = 1; i <=3; i++){// recibe y enviarPaquetes
                // Se crea un DatagramPacket con el tamaño de buffer especificado.
                // Este paquete se utilizará para recibir los datos enviados por el cliente.

                DatagramPacket peticion = new DatagramPacket(buffer, buffer.length);//Paqute UPD cone l buffer para recibir datos
    /*
    * Al ejecutar este método, el buffer se llena con el mensaje enviado
    * por el cliente.
    * Este método BLOQUEA la ejecución del código hasta que se reciba el paquete completo.
    Si el mensaje enviado es más grande que el tamaño del buffer, el mensaje se truncará.
    *
     */         datagramSocket.receive(peticion);//Espera a que llegue mensaje y lo almacena.
                String msjCliente = new String(peticion.getData(), 0, peticion.getLength()); // Convierte el contenido del buffer recibido en un String para poder procesarlo.


                //DATOS CLIENTE
                int puertoCliente = peticion.getPort();// La información del cliente (dirección IP y puerto) está contenida en el DatagramPacket,por lo que extraemos estos datos para poder enviarle una respuesta.

                InetAddress direccion = peticion.getAddress();// Envio la respuesta al cliente utilizando su dirección IP y puerto extraídos previamente.

                String answerToClient = "Hola " + i + whoami;
                buffer = answerToClient.getBytes();

                DatagramPacket respuesta = new DatagramPacket(buffer, buffer.length, direccion, puertoCliente); //empaqueta la respuesta en un buffer nuevo y lo envia
                datagramSocket.send(respuesta);
            }
            datagramSocket.close();

        } catch (IOException ex) {
            ex.getMessage();
        }
    }
}
