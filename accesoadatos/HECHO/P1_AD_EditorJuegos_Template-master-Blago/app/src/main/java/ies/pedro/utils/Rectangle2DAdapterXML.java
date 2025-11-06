package ies.pedro.utils;

import jakarta.xml.bind.annotation.adapters.XmlAdapter;
import javafx.geometry.Rectangle2D;

// adaptador para serializar
public class Rectangle2DAdapterXML extends XmlAdapter<String, Rectangle2D> {

    // Convierte una cadena XML a un objeto Rectangle2D
    // Formato esperado: "x,y,ancho,alto"
    @Override
    public Rectangle2D unmarshal(String v) throws Exception {
        if (v == null || v.isEmpty()) {
            return null;
        }

        String[] parts = v.split(",");
        double x = Double.parseDouble(parts[0]);      // Posición X
        double y = Double.parseDouble(parts[1]);      // Posición Y
        double w = Double.parseDouble(parts[2]);      // Ancho
        double h = Double.parseDouble(parts[3]);      // Alto
        return new Rectangle2D(x, y, w, h);
    }

    // Convierte un Rectangle2D a String para guardarlo en XML
    // Formato de salida: "x,y,ancho,alto"
    @Override
    public String marshal(Rectangle2D v) throws Exception {
        if (v == null) {
            return null;
        }
        return v.getMinX() + "," + v.getMinY() + "," + v.getWidth() + "," + v.getHeight();
    }
}
