/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package com.bdd.guiswingorderwinbdd;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;

/**
 *
 * @author dan
 */
public class LoginForm extends javax.swing.JFrame {

    public static java.util.Map<String, String> usuariosExtra = new java.util.HashMap<>();

    private JTextField txtUser;
    private JPasswordField txtPass;
    private JFrame mainFrame;

    public LoginForm(JFrame main) {
        this.mainFrame = main;
        initManualComponents();
    }

    private void initManualComponents() {
        Color darkGrey = new Color(45, 45, 48);     // Fondo 
        Color vibrantGreen = new Color(40, 167, 69); // Verde 
        Color textWhite = Color.WHITE;

        this.setUndecorated(true);
        this.setAlwaysOnTop(true);
        this.setSize(450, 350);
        this.setLocationRelativeTo(null);
        this.getContentPane().setBackground(darkGrey);

        this.setLayout(new BorderLayout(20, 20));

        // Panel central para los campos 
        JPanel pnlCentral = new JPanel(new GridLayout(5, 1, 10, 10));
        pnlCentral.setBackground(darkGrey);
        pnlCentral.setBorder(BorderFactory.createEmptyBorder(20, 40, 20, 40));

        JLabel lblTitle = new JLabel("LOGIN", SwingConstants.CENTER);
        lblTitle.setFont(new Font("Arial", Font.BOLD, 22));
        lblTitle.setForeground(vibrantGreen); // Título en verde
        lblTitle.setBorder(BorderFactory.createEmptyBorder(30, 0, 10, 0));

        txtUser = new JTextField("admin"); // Default user
        txtPass = new JPasswordField("admin"); // Default pass

        // Estilo textFields
        txtUser.setBackground(new Color(60, 60, 60));
        txtUser.setForeground(textWhite);
        txtUser.setCaretColor(textWhite);
        txtUser.setBorder(BorderFactory.createTitledBorder(
                BorderFactory.createLineBorder(vibrantGreen), "Username", 0, 0, null, textWhite));

        txtPass.setBackground(new Color(60, 60, 60));
        txtPass.setForeground(textWhite);
        txtPass.setCaretColor(textWhite);
        txtPass.setBorder(BorderFactory.createTitledBorder(
                BorderFactory.createLineBorder(vibrantGreen), "Password", 0, 0, null, textWhite));

        // Estilo login
        JButton btnLogin = new JButton("LOGIN");
        btnLogin.setBackground(vibrantGreen);
        btnLogin.setForeground(textWhite);
        btnLogin.setFocusPainted(false);
        btnLogin.setFont(new Font("Arial", Font.BOLD, 14));

        // Estilo register
        JButton btnRegister = new JButton("Register Now");
        btnRegister.setForeground(vibrantGreen);
        btnRegister.setContentAreaFilled(false);
        btnRegister.setBorder(BorderFactory.createLineBorder(vibrantGreen));

        btnLogin.addActionListener(e -> validarAcceso());
        btnRegister.addActionListener(e -> {
            new SignUpForm(this).setVisible(true);
            this.setVisible(false);
        });

        this.add(lblTitle, BorderLayout.NORTH);
        pnlCentral.add(txtUser);
        pnlCentral.add(txtPass);
        pnlCentral.add(btnLogin);
        pnlCentral.add(btnRegister);
        this.add(pnlCentral, BorderLayout.CENTER);
    }

    private void validarAcceso() {
    String user = txtUser.getText();
    String pass = new String(txtPass.getPassword());

    boolean isAdmin = user.equals("admin") && pass.equals("admin");
    
    boolean isNewUser = usuariosExtra.containsKey(user) && usuariosExtra.get(user).equals(pass);

    if (isAdmin || isNewUser) {
        if (mainFrame != null) {
            mainFrame.setEnabled(true);
        }
        this.dispose();
    } else {
        JOptionPane.showMessageDialog(this, "Credenciales incorrectas", "Error", JOptionPane.ERROR_MESSAGE);
    }
}

    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 400, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 300, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    // Variables declaration - do not modify//GEN-BEGIN:variables
    // End of variables declaration//GEN-END:variables
}
