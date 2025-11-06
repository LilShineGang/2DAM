module ies.sequeros.dam.ad_ud_practica {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.ikonli.javafx;
    requires java.sql;
    requires jasypt;

    opens ies.sequeros.dam.ad_ud_practica to javafx.fxml;
    exports ies.sequeros.dam.ad_ud_practica;
    exports ies.sequeros.dam.ad_ud_practica.model;
}