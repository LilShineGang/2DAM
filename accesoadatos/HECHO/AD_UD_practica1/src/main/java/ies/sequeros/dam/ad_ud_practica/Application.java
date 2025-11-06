package ies.sequeros.dam.ad_ud_practica;

import ies.sequeros.dam.ad_ud_practica.data.UsuarioDBRepository;
import ies.sequeros.dam.ad_ud_practica.model.IUsuarioRepository;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

import static java.lang.System.load;

public class Application extends javafx.application.Application {
    public String getConnectionString(){
        StandardPBEStringEncryptor encryptor = new
                StandardPBEStringEncryptor();
        encryptor.setAlgorithm("PBEWithMD5AndDES");
        encryptor.setPassword("contrasenya");

        Properties props = new Properties();
        try (FileInputStream fis = new FileInputStream("app.properties")) {
            props.load(fis);
        } catch (IOException e) {
            System.err.println("No se pudo leer el archivo de propiedades: " + e.getMessage());
        }
        for (String key : props.stringPropertyNames()) {
            String value = props.getProperty(key);
            System.out.println(key + " = " + value);
        }
        String connectionstring = props.getProperty("database.path");
        String user = (props.getProperty("database.user"));
        String password =
                encryptor.decrypt(props.getProperty("database.password"));
        return  connectionstring+";user="+user+";password="+password;
    }
    @Override
    public void start(Stage stage) throws IOException {


        IUsuarioRepository repository= new
                UsuarioDBRepository(this.getConnectionString());
                //"jdbc:derby:C:/Users/user/Desktop/AD_UP2_P1/AD_UD_practica1/bbdd/usuarios;user=pedro;password=picapiedra");

        FXMLLoader loader = new FXMLLoader(getClass().getResource("app-view.fxml"));
        Parent root = loader.load(); // FXMLLoader crea el controlador
        AppController controller = loader.getController(); // obtén el existente
        controller.setRepository(repository);
        Scene scene = new Scene(root, 800, 600);

        stage.setTitle("Práctica AD");
        stage.setScene(scene);
        stage.show();
    }
}
