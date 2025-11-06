package org.example.data.model;

import java.util.UUID;

public class Usuario {

    private UUID id;
    private String nombre;
    private String apellidos;
    private String mail;
    private boolean activo;
    private String nick;
    private String contrasenya;

    // 🔹 Constructor vacío (necesario para frameworks o serialización)
    public Usuario(UUID id) {
        this.id = id;
    }

    // 🔹 Constructor con todos los campos
    public Usuario(
        UUID id,
        String nombre,
        String apellidos,
        String mail,
        boolean activo,
        String nick,
        String contrasenya
    ) {
        this.id = id;
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.mail = mail;
        this.activo = activo;
        this.nick = nick;
        this.contrasenya = contrasenya;
    }

    // 🔹 Getters y Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public String getMail() {
        return mail;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public UUID getId() {
        return id;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }

    public boolean isActivo() {
        return activo;
    }

    public void setActivo(boolean activo) {
        this.activo = activo;
    }

    public String getNick() {
        return nick;
    }

    public void setNick(String nick) {
        this.nick = nick;
    }

    public String getContrasenya() {
        return contrasenya;
    }

    public void setContrasenya(String contrasenya) {
        this.contrasenya = contrasenya;
    }

    // 🔹 Método útil para depuración
    @Override
    public String toString() {
        return (
            "Usuario{" +
            "nombre='" +
            nombre +
            '\'' +
            ", apellidos='" +
            apellidos +
            '\'' +
            ", mail='" +
            mail +
            '\'' +
            ", activo=" +
            activo +
            ", nick='" +
            nick +
            '\'' +
            '}'
        );
        // ⚠️ No incluir la contrasenya en toString() por seguridad
    }
}
