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

