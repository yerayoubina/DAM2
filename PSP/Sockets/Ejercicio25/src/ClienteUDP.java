
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;


public class ClienteUDP implements Runnable{
    static List<String> lista = Arrays.asList("Hola", "que", "encimera", "porgramar", "televidente");
    @Override
    public void run() {
        int puerto_servidor = 6666;
        byte[] bufferMandarDatos;
        byte[] bufferRecibeDatos = new byte[1024];

        try {
            InetAddress direccionServidor = InetAddress.getByName("localhost");
            DatagramSocket datagramSocket = new DatagramSocket();

                simulaTiempo(1.5);

                //enviar mensaje al server iterar sobre lista y mandarlo en el buffer
                StringBuilder sb = new StringBuilder();
                for(String p: lista){
                    sb.append(p).append(",");
                }

                String miPeticion = sb.toString();
                bufferMandarDatos = miPeticion.getBytes();

                DatagramPacket peticion = new DatagramPacket(bufferMandarDatos, bufferMandarDatos.length, direccionServidor, puerto_servidor);
                datagramSocket.send(peticion);

                //Preparar para recibir respuesta
                DatagramPacket miRespuesta = new DatagramPacket(bufferRecibeDatos, bufferRecibeDatos.length);
                datagramSocket.receive(miRespuesta);

                //Procesa la respuesta
                String msjServidor = new String(miRespuesta.getData(),0 , miRespuesta.getLength());
                System.out.println("Cliente -> Respuesta servidor: " + msjServidor);

            //close
            datagramSocket.close();

        } catch (SocketException ex) {
            ex.getMessage();
        } catch (IOException ex) {
            Logger.getLogger(ClienteUDP.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void simulaTiempo(double segundo){
        try{
            Thread.sleep((long)segundo * 1000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
