package org.example.data.model;

import java.util.List;
import java.util.UUID;

public interface IUsuarioRepository {
    public List<Usuario> listaUsuarios();
    public Usuario buscaUsuarioPorId(UUID id);
    public boolean insertar(Usuario usuario);
    public boolean actualizar(Usuario usuario);
    public boolean eliminar(UUID id);
}
