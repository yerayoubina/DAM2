
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;


public class ClienteUDP implements Runnable{

    @Override
    public void run() {
        int puerto_servidor = 6666;
        byte[] bufferMandarDatos;
        byte[] bufferRecibeDatos = new byte[1024];
        Scanner sc = new Scanner(System.in);
        try {
            InetAddress direccionServidor = InetAddress.getByName("localhost");
            DatagramSocket datagramSocket = new DatagramSocket();

            //enviar mensaje al server
            for(int i = 1; i<= 3; i++){
                System.out.print("Escribe mensaje al servidor: ");
                String miPeticion = sc.nextLine();
                bufferMandarDatos = miPeticion.getBytes();
                DatagramPacket peticion = new DatagramPacket(bufferMandarDatos, bufferMandarDatos.length, direccionServidor, puerto_servidor);
                datagramSocket.send(peticion);

                //Preparar para recibir respuesta
                DatagramPacket miRespuesta = new DatagramPacket(bufferRecibeDatos, bufferRecibeDatos.length);
                datagramSocket.receive(miRespuesta);

                //Procesa la respuesta
                String msjServidor = new String(miRespuesta.getData(),0 , miRespuesta.getLength());
                System.out.println("Cliente -> Respuesta servidor: " + msjServidor);
            }


            //close
            datagramSocket.close();

        } catch (SocketException ex) {
            ex.printStackTrace();
        } catch (IOException ex) {
            Logger.getLogger(ClienteUDP.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
