package ies.pedro.usuario.repository.dao;

import ies.pedro.datalayer.DataBaseConnection;
import ies.pedro.usuario.model.Usuario;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

public class UsuarioDao implements IDao<Usuario> {
    private DataBaseConnection conn;
    private final String table_name = "USUARIO";
    private final String selectall = "select * from " + table_name;
    private final String selectbyid = "select * from " + table_name + " where id=?";
    private final String deletebyid = "delete from " + table_name + " where id=?";
    private final String insertsql = "insert into " + table_name + " (NOMBRE,CORREO,CLAVE,ACTIVO)VALUES(?,?,?,?)";
    private final String updatesql = "update " + table_name + " set NOMBRE=?,CORREO=?,CLAVE=?,ACTIVO=? WHERE ID=?";

    public UsuarioDao() {
    }

    public DataBaseConnection getConn() {
        return this.conn;
    }

    public void setConn(final DataBaseConnection conn) {
        this.conn = conn;
    }

    @Override
    public Usuario getById(final int id) {
        Usuario sp = new Usuario();
        try {
            final PreparedStatement pst = conn.getConnection().prepareStatement(selectbyid);
            pst.setInt(1, id);
            final ResultSet rs = pst.executeQuery();
            sp = registerToObject(rs);
            return sp;
        } catch (final SQLException ex) {
            Logger.getLogger(UsuarioDao.class.getName()).log(Level.SEVERE,
                    null, ex);
        }
        return sp;
    }

    @Override
    public List<Usuario> getAll() {
        final ArrayList<Usuario> scl = new ArrayList<>();
        Usuario tempo;
        PreparedStatement pst = null;
        try {
            try {
                pst = conn.getConnection().prepareStatement(selectall);
            } catch (final SQLException ex) {
                Logger.getLogger(UsuarioDao.class.getName()).log(Level.SEVERE,
                        null, ex);
            }
            final ResultSet rs = pst.executeQuery();
            while (rs.next()) {
                tempo = registerToObject(rs);
                scl.add(tempo);
            }
        } catch (final SQLException ex) {
            Logger.getLogger(UsuarioDao.class.getName()).log(Level.SEVERE,
                    null, ex);
        }
        return scl;
    }

    @Override
    public void update(final Usuario item) {
        try {
            final PreparedStatement pst =
                    conn.getConnection().prepareStatement(updatesql);
            pst.setString(1, item.getNombre());
            pst.setString(2, item.getCorreo());
            pst.setString(3, item.getClave());
            pst.setBoolean(4, item.isActivo());
            pst.setInt(5, item.getId());
            pst.executeUpdate();
        } catch (final SQLException ex) {
            Logger.getLogger(UsuarioDao.class.getName()).log(Level.SEVERE,
                    null, ex);
        }
    }

    @Override
    public void delete(final Usuario item) {
        try {
            final PreparedStatement pst =
                    conn.getConnection().prepareStatement(deletebyid);
            pst.setInt(1, item.getId());
            pst.executeUpdate();
        } catch (final SQLException ex) {
            Logger.getLogger(UsuarioDao.class.getName()).log(Level.SEVERE,
                    null, ex);
        }
    }

    @Override
    public void insert(final Usuario item) {
        final PreparedStatement pst;
        try {
            pst = conn.getConnection().prepareStatement(insertsql,
                    Statement.RETURN_GENERATED_KEYS);
            pst.setString(1, item.getNombre());
            pst.setString(2, item.getCorreo());
            pst.setString(3, item.getClave());
            pst.setBoolean(4, item.isActivo());

            pst.executeUpdate();
            final ResultSet rs = pst.getGeneratedKeys();
            if (rs.next())
                item.setId(rs.getInt(1));
            // }
        } catch (final SQLException ex) {
            Logger.getLogger(UsuarioDao.class.getName()).log(Level.SEVERE,
                    null, ex);
        }
    }

    //pasar de registro a objeeto
    private Usuario registerToObject(final ResultSet r) {
        final Usuario sc = new Usuario();
        try {
            sc.setId(r.getInt("ID"));
            sc.setNombre(r.getString("NOMBRE"));
            sc.setActivo(r.getBoolean("ACTIVO"));
            sc.setClave(r.getString("CLAVE"));
            sc.setCorreo(r.getString("CORREO"));
            return sc;
        } catch (final SQLException ex) {
            Logger.getLogger(UsuarioDao.class.getName()).log(Level.SEVERE,
                    null, ex);
        }
        return sc;
    }
}
