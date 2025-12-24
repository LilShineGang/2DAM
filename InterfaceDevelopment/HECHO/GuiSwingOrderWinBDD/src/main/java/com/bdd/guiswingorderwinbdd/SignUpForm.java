/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package com.bdd.guiswingorderwinbdd;

import javax.swing.*;
import java.awt.*;

/**
 *
 * @author dan
 */
public class SignUpForm extends javax.swing.JFrame {
    
    private JTextField txtNewUser;
    private JPasswordField txtNewPass, txtConfirmPass;
    private JFrame loginFrame;

    public SignUpForm(JFrame login) {
        this.loginFrame = login;
        initManualComponents();
    }

    private void initManualComponents() {
        Color darkGrey = new Color(45, 45, 48);
        Color vibrantGreen = new Color(40, 167, 69);
        Color textWhite = Color.WHITE;

        this.setUndecorated(true);
        this.setAlwaysOnTop(true);
        this.setSize(400, 480);
        this.setLocationRelativeTo(null);
        this.getContentPane().setBackground(darkGrey);
        this.setLayout(new BorderLayout(10, 10));

        JLabel lblTitle = new JLabel("REGISTER", SwingConstants.CENTER);
        lblTitle.setFont(new Font("Arial", Font.BOLD, 22));
        lblTitle.setForeground(vibrantGreen);
        lblTitle.setBorder(BorderFactory.createEmptyBorder(30, 0, 10, 0));

        JPanel pnl = new JPanel(new GridLayout(6, 1, 15, 15));
        pnl.setBackground(darkGrey);
        pnl.setBorder(BorderFactory.createEmptyBorder(10, 45, 30, 45));

        txtNewUser = new JTextField();
        txtNewPass = new JPasswordField();
        txtConfirmPass = new JPasswordField();

        txtNewUser.setBorder(BorderFactory.createTitledBorder(BorderFactory.createLineBorder(vibrantGreen), "New Username", 0, 0, null, textWhite));
        txtNewPass.setBorder(BorderFactory.createTitledBorder(BorderFactory.createLineBorder(vibrantGreen), "New Password", 0, 0, null, textWhite));
        txtConfirmPass.setBorder(BorderFactory.createTitledBorder(BorderFactory.createLineBorder(vibrantGreen), "Confirm Password", 0, 0, null, textWhite));
        
        JTextField[] fields = {txtNewUser, txtNewPass, txtConfirmPass};
        for(JTextField f : fields) { 
            f.setBackground(new Color(60, 60, 60)); 
            f.setForeground(textWhite); 
            f.setCaretColor(textWhite);
        }

        JButton btnRegister = new JButton("REGISTER");
        btnRegister.setBackground(vibrantGreen);
        btnRegister.setForeground(Color.BLACK);
        btnRegister.setFont(new Font("Arial", Font.BOLD, 14));
        
        JButton btnBack = new JButton("Back to Login");
        btnBack.setForeground(vibrantGreen);
        btnBack.setContentAreaFilled(false);
        btnBack.setBorder(BorderFactory.createLineBorder(vibrantGreen));

        btnRegister.addActionListener(e -> {
            String user = txtNewUser.getText();
            String pass = new String(txtNewPass.getPassword());
            String confirm = new String(txtConfirmPass.getPassword());

            if (user.isEmpty() || pass.isEmpty()) {
                JOptionPane.showMessageDialog(this, "Fields cannot be empty");
            } else if (!pass.equals(confirm)) {
                JOptionPane.showMessageDialog(this, "Passwords do not match");
            } else {
                LoginForm.usuariosExtra.put(user, pass);
                JOptionPane.showMessageDialog(this, "User " + user + " registered!");
                loginFrame.setVisible(true);
                this.dispose();
            }
        });

        btnBack.addActionListener(e -> { 
            loginFrame.setVisible(true); 
            this.dispose(); 
        });

        pnl.add(txtNewUser);
        pnl.add(txtNewPass);
        pnl.add(txtConfirmPass);
        pnl.add(btnRegister);
        pnl.add(btnBack);

        this.add(lblTitle, BorderLayout.NORTH);
        this.add(pnl, BorderLayout.CENTER);
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
