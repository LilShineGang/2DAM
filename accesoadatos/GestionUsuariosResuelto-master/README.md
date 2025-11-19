# Práctica AD Gestión de Usuarios.

# Enunciado.

A partir de la clase UsuarioRepository que extiende de ARepository
crear una nueva clase que herede de ARepository pero que almacene
los datos en una base de datos Derby.

Este nuevo repositorio, internamente ha de implementar el patrón Dao, además
se le ha de pasar una cadena con la ruta del fichero properties.

```` Java


public class UsuarioRepository extends ARepository<Usuario> {
private static int counter=0;
public UsuarioRepository() {
super();
this.reload();
}



    @Override
    public void add(Usuario item) {

            this.data.add(item);
            //simula la clave primaria
            item.setId(counter);
            counter++;
    }

    @Override
    public void remove(Usuario item) {
            this.data.remove(item);
    }



    @Override
    public void update(Usuario item) {

    }
    public void reload(){
        //el primero que aparece para añadir
        this.data.clear();
        this.data.add(new Usuario());

    }
    //se hace para que en las actualizaciones se repinte
    //o "avise" a quien esté escuchando
    public void refresh(){
        Usuario usuario = new Usuario();
        this.data.add(usuario);
        this.data.remove(usuario);
    }
}
````

Además se ha de modificar el código para que pueda utilizarse cualquier
repositorio.

## Solución.

### DataBaseConnection
Se tiene una conexión, encargada de leer el fichero de configuración y 
ofrecer la conexión a lo dao:

```` java

package ies.pedro.datalayer;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.util.Properties;
import java.util.logging.Level;
import java.util.logging.Logger;

public class DataBaseConnection {
private String config_path;
private String connection_string;
private Connection conexion;

    public DataBaseConnection() {
    }
    public void open() throws Exception {
        FileReader fr = null;
        File f =new File(System.getProperty("user.dir")+
                this.getConfig_path());
        fr = new FileReader(f);
        Properties props = new Properties();
        try {
            props.load(fr);
        } catch (IOException ex) {
           ex.printStackTrace();
        }

        String user = props.getProperty("database.user");
        String password = props.getProperty("database.password");
        this.connection_string = props.getProperty("database.path")
                + ";user=" + user + ";password=" + password;
        this.conexion =
                DriverManager.getConnection(this.connection_string);
    }

    public Connection getConnection() {
        return this.conexion;
    }
    public void close() throws SQLException {
        conexion.close();
         conexion = null;
    }
    public String getConfig_path() {
        return config_path;
    }
    public void setConfig_path(String config_path) {
        this.config_path = config_path;
    }
}
````

### Patrón DAO.

Siguiendo los apuntes, se define la interfaz:

``` java

package ies.pedro.usuario.repository.dao;

import java.util.List;

public interface IDao<T> {
public T getById(int id);
public List<T> getAll();
public void update(T item);
public void delete(T item);
public void insert(T item);
}

```

Y la implementación para Usuarios:

```` java

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

´´´

### Repositorio.

En primer lugar sa de cambiar en el código las referencias a UsuarioRepositorio por ARepository<Usuario> y añadir
los métodos reload y refresh, el repositorio concreto solo ha de aparecer al hacer el new.

```` java

public class MainController implements Initializable {
    private final Stage stage;
    private double xOffset;
    private double yOffset;
    private final ToggleGroup toggleGroup;
    private Router router;
    private IRepository<Usuario> repository;
...
    private void configUsuarios() {
        try {
            this.repository = new BBDDUserRepository("./app.properties");
            this.viewModel = new UsuarioViewModel();
            this.viewModel.setRepository(this.repository);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

````

Ahora solo queda implementar el repositorio:

``` java

package ies.pedro.usuario.repository;

import ies.pedro.datalayer.ARepository;
import ies.pedro.datalayer.DataBaseConnection;
import ies.pedro.usuario.repository.dao.UsuarioDao;
import ies.pedro.usuario.model.Usuario;

import java.util.List;


public class BBDDUserRepository extends ARepository<Usuario> {
private final DataBaseConnection db;
private UsuarioDao dao;
public BBDDUserRepository(String path) throws Exception {
super();
this.db = new DataBaseConnection();
this.db.setConfig_path(path);
this.db.open();
dao= new UsuarioDao();
dao.setConn(this.db);
this.reload();
}
    private List<Usuario> listaUsuarios() throws Exception {
        return dao.getAll();
    }
    @Override
    public void add(Usuario usuario) {
        dao.insert(usuario);
        this.data.add(usuario);
    }
    @Override
    public void remove(Usuario usuario) {
        dao.delete(usuario);
        this.data.remove(usuario);
    }

    @Override
    public void update(Usuario usuario) {
       dao.update(usuario);
       this.refresh();
    }

    @Override
    public void reload() {
        this.data.clear();
        //el primero que aparece para añadir
        this.data.add(new Usuario());
        this.data.addAll(dao.getAll());
    }
    @Override
    public void refresh() {
        Usuario usuario = new Usuario();
        this.data.add(usuario);
        this.data.remove(usuario);
    }
}

```
