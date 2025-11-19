/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ies.pedro.model;

import com.google.gson.*;
import ies.pedro.utils.Rectangle2DAdapterJSON;
import ies.pedro.utils.Size;
import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;
import jakarta.xml.bind.annotation.*;
import java.io.*;
import java.util.*;
import javafx.geometry.Rectangle2D;

// Puede ser serializada en XML, JSON o formato binario
@XmlRootElement // Marca esta clase como elemento raíz para XML
@XmlAccessorType(XmlAccessType.FIELD) // JAXB accede directamente a los campos
public class Level implements Serializable {

    // Dimensiones del nivel (ancho y alto en celdas)
    private Size size;

    // Lista de todos los bloques que componen el nivel
    private ArrayList<Block> elementos;

    // Tiempo límite para completar el nivel (en segundos)
    private double time;

    // Ruta del archivo de música de fondo
    private String sound;

    // Nombre identificativo del nivel
    private String name;

    // Ruta de la imagen de fondo del nivel
    private String backgroundImage;

    // Constructor con solo nombre
    public Level(String name) {
        this.name = name;
        this.elementos = new ArrayList<>();
    }

    // Constructor con nombre y tamaño
    public Level(String name, Size size) {
        this.name = name;
        this.size = size;
        this.elementos = new ArrayList<>();
    }

    // Constructor por defecto necesario para deserialización
    public Level() {
        this.elementos = new ArrayList<>();
    }

    // Inicializa el nivel (puede ser extendido en el futuro)
    public void init() {}

    // Resetea el nivel eliminando todos los elementos y configuraciones
    public void reset() {
        this.elementos.clear();
        this.backgroundImage = null;
        this.sound = null;
        this.init();
    }

    // Añade un bloque al nivel
    public void addElement(Block block) {
        this.elementos.add(block);
    }

    // Elimina un bloque del nivel
    public void removeElement(Block block) {
        this.elementos.remove(block);
    }

    // Verifica si un bloque intersecta con algún bloque existente en el nivel
    public boolean intersects(Block b) {
        for (Block block : this.elementos) {
            if (block.getRectangle().intersects(b.getRectangle())) {
                return true;
            }
        }
        return false;
    }

    // Busca un bloque en una posición específica (x, y)
    // Devuelve Optional para manejar el caso de no encontrar nada
    public Optional<Block> getByPosition(int x, int y) {
        for (Block block : this.elementos) {
            if (block.getRectangle().contains(x, y)) {
                return Optional.of(block);
            }
        }
        return Optional.empty();
    }

    public Size getSize() {
        return size;
    }

    public void setSize(Size size) {
        this.size = size;
    }

    public double getTime() {
        return time;
    }

    public void setTime(double time) {
        this.time = time;
    }

    public String getSound() {
        return sound;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    public List<Block> getElements() {
        return Collections.unmodifiableList(this.elementos);
    }

    public String getBackgroundImage() {
        return backgroundImage;
    }

    public void setBackgroundImage(String path) {
        this.backgroundImage = path;
    }

    public void setBackgroundPosition(String backgroundImage) {
        this.backgroundImage = backgroundImage;
    }

    // Carga un nivel desde un archivo
    // Detecta automáticamente el formato según la extensión (.xml, .json, .bin)
    public static Level load(File file) throws Exception {
        String extension = file
            .getName()
            .substring(file.getName().lastIndexOf(".") + 1);
        Level m = null;
        if (extension.equals("xml")) {
            // Carga desde XML usando JAXB
            JAXBContext context = JAXBContext.newInstance(Level.class);
            Unmarshaller UnSh = context.createUnmarshaller();
            m = (Level) UnSh.unmarshal(file);
        } else {
            if (extension.equals("json")) {
                // Carga desde JSON usando Gson con adaptador para Rectangle2D
                FileReader reader = new FileReader(file);
                Gson gson = new GsonBuilder()
                    .registerTypeAdapter(
                        Rectangle2D.class,
                        new Rectangle2DAdapterJSON()
                    )
                    .create();
                m = gson.fromJson(reader, Level.class);
            } else {
                if (extension.equals("bin")) {
                    // Carga desde formato binario usando serialización de Java
                    FileInputStream FileInStr = new FileInputStream(file);
                    ObjectInputStream ObjInStr = new ObjectInputStream(
                        FileInStr
                    );
                    m = (Level) ObjInStr.readObject();
                } else {
                    throw new Exception(
                        "Extensión " + extension + " no permitida"
                    );
                }
            }
        }
        return m;
    }

    // Guarda un nivel en un archivo
    // El formato se determina por la extensión del archivo (.xml, .json, .bin)
    public static void save(Level level, File file) throws Exception {
        String extension = file
            .getName()
            .substring(file.getName().lastIndexOf(".") + 1);
        if (extension.equals("xml")) {
            // Guarda en XML usando JAXB con formato legible
            JAXBContext context = JAXBContext.newInstance(Level.class);
            Marshaller mar = context.createMarshaller();
            mar.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true); // Formato con indentación
            mar.marshal(level, file);
        } else {
            if (extension.equals("json")) {
                // Guarda en JSON usando Gson con adaptador para Rectangle2D
                FileWriter writer = new FileWriter(file);
                Gson gson = new GsonBuilder()
                    .registerTypeAdapter(
                        Rectangle2D.class,
                        new Rectangle2DAdapterJSON()
                    )
                    .create();
                gson.toJson(level, writer);
            } else {
                if (extension.equals("bin")) {
                    // Guarda en formato binario usando serialización de Java
                    FileOutputStream FileOutStr = new FileOutputStream(file);
                    ObjectOutputStream ObjOutStr = new ObjectOutputStream(
                        FileOutStr
                    );
                    ObjOutStr.writeObject(level);
                } else {
                    throw new Exception(
                        "Extensión " + extension + " no permitida"
                    );
                }
            }
        }
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
