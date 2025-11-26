module org.example {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.ikonli.javafx;
    requires java.sql;
    requires jasypt;

    opens org.example to javafx.fxml;
    exports org.example;
    exports org.example.model;
}
