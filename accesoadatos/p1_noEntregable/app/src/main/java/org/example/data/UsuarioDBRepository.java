package org.example.data;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import org.example.data.model.IUsuarioRepository;
import org.example.data.model.Usuario;

public class UsuarioDBRepository implements IUsuarioRepository {

    private final String url;

    public UsuarioDBRepository(String url) {
        this.url = url;
    }

    @Override
    public List<Usuario> listaUsuarios() {
        final List<Usuario> usuarios = new ArrayList();
        String sql = "SELECT * FROM USUARIOS";

        try (
            Connection conn = DriverManager.getConnection(url);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql)
        ) {
            while (rs.next()) {
                usuarios.add(
                    new Usuario(
                        UUID.fromString(rs.getString("ID")),
                        rs.getString("NOMBRE"),
                        rs.getString("APELLIDOS"),
                        rs.getString("MAIL"),
                        rs.getBoolean("ACTIVO"),
                        rs.getString("NICK"),
                        rs.getString("CONTRASENA")
                    )
                );
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return usuarios;
    }

    @Override
    public Usuario buscaUsuarioPorId(UUID id) {
        String sql = "SELECT * FROM USUARIOS WHERE ID = ?";
        Usuario usuario = null;

        Connection conn = null;
        try {
            conn = DriverManager.getConnection("jdbc:derby:usuariosDB");
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, id.toString());
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                usuario = new Usuario(
                    UUID.fromString(rs.getString("ID")),
                    rs.getString("NOMBRE"),
                    rs.getString("APELLIDOS"),
                    rs.getString("MAIL"),
                    rs.getBoolean("ACTIVO"),
                    rs.getString("NICK"),
                    rs.getString("CONTRASENA")
                );
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return usuario;
    }

    @Override
    public boolean insertar(Usuario usuario) {
        String sql = """
            INSERT INTO USUARIOS (ID,NOMBRE, APELLIDOS, MAIL, ACTIVO, NICK, CONTRASENA)
            VALUES (?,?, ?, ?, ?, ?, ?)
            """;

        try (
            Connection conn = DriverManager.getConnection(url);
            PreparedStatement stmt = conn.prepareStatement(sql)
        ) {
            stmt.setString(1, usuario.getId().toString());
            stmt.setString(2, usuario.getNombre());
            stmt.setString(3, usuario.getApellidos());
            stmt.setString(4, usuario.getMail());
            stmt.setBoolean(5, usuario.isActivo());
            stmt.setString(6, usuario.getNick());
            stmt.setString(7, usuario.getContrasenya());

            return stmt.executeUpdate() > 0;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    @Override
    public boolean actualizar(Usuario usuario) {
        String sql =
            " UPDATE USUARIOS SET NOMBRE = ?, APELLIDOS = ?, MAIL = ?, ACTIVO = ?, NICK = ?, CONTRASENA = ? WHERE ID = ? ";

        try (
            Connection conn = DriverManager.getConnection(url);
            PreparedStatement stmt = conn.prepareStatement(sql)
        ) {
            stmt.setString(1, usuario.getNombre());
            stmt.setString(2, usuario.getApellidos());
            stmt.setString(3, usuario.getMail());
            stmt.setBoolean(4, usuario.isActivo());
            stmt.setString(5, usuario.getNick());
            stmt.setString(6, usuario.getContrasenya());
            stmt.setString(7, usuario.getId().toString()); // WHERE ID = ?

            return stmt.executeUpdate() > 0; // devuelve true si se actualizó al menos 1 fila
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    @Override
    public boolean eliminar(UUID id) {
        String sql = "DELETE FROM USUARIOS WHERE id = ?";

        try (
            Connection conn = DriverManager.getConnection(url);
            PreparedStatement stmt = conn.prepareStatement(sql)
        ) {
            stmt.setString(1, id.toString());
            int filas = stmt.executeUpdate();
            return filas > 0;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }
}
