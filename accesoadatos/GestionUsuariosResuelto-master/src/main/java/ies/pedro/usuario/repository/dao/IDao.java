package ies.pedro.usuario.repository.dao;

import java.util.List;

public interface IDao<T> {
    public T getById(int id);
    public List<T> getAll();
    public void update(T item);
    public void delete(T item);
    public void insert(T item);
}