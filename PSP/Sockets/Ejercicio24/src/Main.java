public class Main {
    public static void main(String[] args) {


        Thread clienteH = new Thread(new ClienteUDP());
        Thread serverH = new Thread(new ServidorUDP());

        serverH.start();
        clienteH.start();
    }
    }