package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {


        String jdbcUrl ="jdbc:postgresql://192.168.1.185:5500/pruebasHibernate";
        String USER = "admin";
        String PASSWORD = "admin";

        try {
            Connection miConexin = DriverManager.getConnection(jdbcUrl,USER,PASSWORD);
            System.out.println("Conexión exitosa");
        } catch (SQLException e) {
            System.out.println("ALGO HA FALLADO " + e.getMessage());

        }
    }
}