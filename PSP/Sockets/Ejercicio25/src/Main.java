public class Main {
    public static void main(String[] args) {

System.out.println("DETECTAR PALABRA MAS LARGA DE UNALISTA");

        Thread clienteH = new Thread(new ClienteUDP());
        Thread serverH = new Thread(new ServidorUDP());

        serverH.start();
        clienteH.start();
    }
}