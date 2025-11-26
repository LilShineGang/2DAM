package ies.sequeros.dam.ad_ud_practica;

import ies.sequeros.dam.ad_ud_practica.model.IUsuarioRepository;
import ies.sequeros.dam.ad_ud_practica.model.Usuario;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;
import org.controlsfx.control.GridCell;
import org.controlsfx.control.GridView;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

import java.util.List;
import java.util.UUID;

public class AppController {
    public TextField txtNombre;
    public TextField txtApellidos;
    public TextField txtMail;
    public TextField txtUsuario;
    public PasswordField txtContrasena;
    public CheckBox chkActivo;
    public Button btnGuardar;
    public Button btnCancelar;
    private Usuario selected;
    @FXML
    private GridView<Usuario> gridView;
    private ObservableList<Usuario> listaUsuarios = FXCollections.observableArrayList();
    private IUsuarioRepository repository;
    private StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
    @FXML
    public void initialize() {
        //configuración encriptación
        encryptor.setAlgorithm("PBEWithMD5AndDES");
        encryptor.setPassword("contrasenya");
        gridView.setItems(listaUsuarios);
        gridView.setHorizontalCellSpacing(10);
        gridView.setVerticalCellSpacing(10);
        gridView.setCellWidth(150);
        gridView.setCellHeight(100);
        gridView.setCellFactory(view -> new GridCell<>() {
            private final VBox vbox = new VBox(5);
            private final Label nombre = new Label();
            private final Label mail = new Label();
            private final ImageView imagen = new ImageView();
            private final Button btnBorrar = new Button("🗑 Borrar");

            {
                // Configurar imagen
                imagen.setFitWidth(64);
                imagen.setFitHeight(64);
                imagen.setPreserveRatio(true);
                imagen.setOnMouseClicked(e -> {
                    Usuario item = getItem();
                    if (item != null) {

                        // Aquí puedes abrir un modal, editar usuario, etc.
                        selected = item;
                        txtNombre.setText(item.getNombre());
                        txtApellidos.setText(item.getApellidos());
                        txtMail.setText(item.getMail());
                        txtContrasena.setText(item.getContrasenya());
                        chkActivo.setSelected(item.isActivo());
                        txtUsuario.setText(item.getNick());

                    }
                });
                // Configurar layout
                vbox.setAlignment(Pos.CENTER);
                vbox.setPadding(new Insets(10));
                vbox.getChildren().addAll(imagen, nombre, mail, btnBorrar);

                // Acción del botón de borrar
                btnBorrar.setOnAction(e -> {
                    Usuario item = this.getItem();
                    if (item != null) {
                        repository.eliminar(item.getId());
                        if( selected!=null && item.getId()==selected.getId())
                            clearForm();
                        AppController.this.listaUsuarios.remove(item); // quita de la lista
                    }
                });
            }

            @Override
            protected void updateItem(Usuario item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null) {
                    setGraphic(null);
                } else {
                    nombre.setText(item.getNombre());
                    mail.setText(item.getMail());

                    // Cargar imagen desde resources
                    Image img = new Image(
                            getClass().getResourceAsStream("/user.jpg"),
                            64, 64, true, true
                    );
                    imagen.setImage(img);

                    setGraphic(vbox);
                }
            }
        });

    }
    public void setRepository(final IUsuarioRepository irepository) {
        this.repository = irepository;
        List<Usuario> tempo=this.repository.listaUsuarios().stream().map(usuario -> {
            String decrypt = this.encryptor.decrypt(usuario.getContrasenya());
            usuario.setContrasenya(decrypt);
            return usuario;
        }).toList();
        this.listaUsuarios.addAll(tempo);
    }
    public void onGuardarUsuario(ActionEvent actionEvent) {
        if(selected==null) {
            Usuario u = new Usuario(UUID.randomUUID());
            u.setNombre(txtNombre.getText());
            u.setApellidos(txtApellidos.getText());
            u.setMail(txtMail.getText());
            u.setActivo(chkActivo.isSelected());
            u.setContrasenya(this.encryptor.encrypt(txtContrasena.getText()));
            u.setNick(txtUsuario.getText());
            this.repository.insertar(u);
            AppController.this.listaUsuarios.add(u);
        }else{
            this.selected.setNombre(txtNombre.getText());
            this.selected.setApellidos(txtApellidos.getText());
            this.selected.setMail(txtMail.getText());
            this.selected.setActivo(chkActivo.isSelected());

            this.selected.setContrasenya(this.encryptor.encrypt(txtContrasena.getText()));
            this.selected.setNick(txtUsuario.getText());
            this.repository.actualizar(selected);
            final int index = listaUsuarios.indexOf(selected);
            listaUsuarios.set(index, selected);

        }
        this.clearForm();


    }
    private void clearForm(){
        txtNombre.clear();
        txtApellidos.clear();
        txtMail.clear();
        txtUsuario.clear();
        txtContrasena.clear();
        chkActivo.setSelected(false);
        this.selected=null;
    }
    public void onCancelar(ActionEvent actionEvent) {
        this.clearForm();

    }
}
