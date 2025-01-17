public class Main {
    public static void main(String[] args) {

        Thread serverH = new Thread(new ServidorUDP());
        Thread clienteH = new Thread(new ClienteUDP());

        serverH.start();
    }
}
