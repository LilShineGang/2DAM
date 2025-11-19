package ies.pedro.utils;

import com.google.gson.*;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonToken;
import com.google.gson.stream.JsonWriter;
import javafx.geometry.Point2D;
import javafx.geometry.Rectangle2D;

import java.io.IOException;
import java.lang.reflect.Type;

// implementacion adaptador
public class Rectangle2DAdapterJSON implements JsonSerializer<Rectangle2D>, JsonDeserializer<Rectangle2D> {
    
    // Convierte un Rectangle2D a formato JSON
    // Crea un objeto JSON con las propiedades: 
    @Override
    public JsonElement serialize(Rectangle2D src, Type typeOfSrc, JsonSerializationContext context) {
        JsonObject obj = new JsonObject();
        obj.addProperty("minX", src.getMinX());        // Posición X mínima
        obj.addProperty("minY", src.getMinY());        // Posición Y mínima
        obj.addProperty("width", src.getWidth());      // Ancho del rectángulo
        obj.addProperty("height", src.getHeight());    // Alto del rectángulo
        return obj;
    }

    // Convierte un objeto JSON a Rectangle2D
    // Lee las propiedades del JSON y crea un nuevo Rectangle2D
    @Override
    public Rectangle2D deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context)
            throws JsonParseException {
        JsonObject obj = json.getAsJsonObject();
        // Crea el Rectangle2D con los valores extraídos del JSON
        return new Rectangle2D(
                obj.get("minX").getAsDouble(),      // Posición X
                obj.get("minY").getAsDouble(),      // Posición Y
                obj.get("width").getAsDouble(),     // Ancho
                obj.get("height").getAsDouble()     // Alto
        );
    }
}
