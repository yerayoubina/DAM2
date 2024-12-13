package com.dam.pruebasHibernate;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Database {
    public static void main(String[] args) {
        String url ="jdbc:mariadb://localhost:3306/pruebasHibernate";
        String user = "root";
        String pass = "admin";


        try {
            Connection connection = DriverManager.getConnection(url,user,pass);

            if(connection !=null){
                System.out.println("Conexion exitosa a MARIADB");
            }
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }
}
