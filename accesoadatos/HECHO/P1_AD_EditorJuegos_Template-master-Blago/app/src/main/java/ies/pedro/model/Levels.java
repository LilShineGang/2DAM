package ies.pedro.model;

import com.google.gson.*;
import ies.pedro.utils.Rectangle2DAdapterJSON;
import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;
import jakarta.xml.bind.annotation.*;
import java.io.*;
import java.util.ArrayList;
import javafx.geometry.Rectangle2D;

// Permite guardar/cargar colecciones completas de niveles en XML, JSON o binario
@XmlRootElement // Elemento raíz para serialización XML
@XmlAccessorType(XmlAccessType.FIELD) // JAXB accede directamente a los campos
public class Levels implements Serializable {

    // Nivel actualmente seleccionado en el editor
    private Level selected;

    // Lista con todos los niveles del juego
    private final ArrayList<Level> levels;

    // Constructor que inicializa la lista de niveles vacía
    public Levels() {
        this.levels = new ArrayList<>();
    }

    // Limpia todos los niveles de la colección
    public void reset() {
        this.levels.clear();
    }

    // Guarda la colección de niveles en un archivo
    // El formato se determina automáticamente por la extensión (.xml, .json, .bin)
    public static void save(Levels levels, File file) throws Exception {
        String extension = file
            .getName()
            .substring(file.getName().lastIndexOf(".") + 1);
        if (extension.equals("xml")) {
            Levels.saveXML(levels, file);
        } else {
            if (extension.equals("json")) {
                Levels.saveJSON(levels, file);
            } else {
                if (extension.equals("bin")) {
                    Levels.saveBin(levels, file);
                } else {
                    throw new Exception(
                        "Exensión " + extension + " no permitida"
                    );
                }
            }
        }
    }

    // Carga una colección de niveles desde un archivo
    // Detecta automáticamente el formato según la extensión del archivo
    public static Levels load(File file)
        throws IOException, FileNotFoundException, ClassNotFoundException, Exception {
        String extension = file
            .getName()
            .substring(file.getName().lastIndexOf(".") + 1);
        Levels m = null;
        if (extension.equals("xml")) {
            m = Levels.loadXML(file);
        } else {
            if (extension.equals("json")) {
                m = Levels.loadJSON(file);
            } else {
                if (extension.equals("bin")) {
                    m = Levels.loadBin(file);
                } else {
                    throw new Exception(
                        "Exencsión " + extension + " no permitida"
                    );
                }
            }
        }
        return m;
    }

    // Carga niveles desde un archivo JSON
    // usamos gson, adaptator para Rectangle2D
    private static Levels loadJSON(File file)
        throws FileNotFoundException, IOException {
        FileReader reader = new FileReader(file);
        Gson gson = new GsonBuilder()
            .registerTypeAdapter(
                Rectangle2D.class,
                new Rectangle2DAdapterJSON()
            )
            .create();
        Levels m = gson.fromJson(reader, Levels.class);
        return m;
    }

    // Carga niveles desde un archivo XML
    private static Levels loadXML(File file) throws IOException {
        try {
            JAXBContext context = JAXBContext.newInstance(Levels.class);
            Unmarshaller un = context.createUnmarshaller();
            Levels m = (Levels) un.unmarshal(file);
            return m;
        } catch (Exception e) {
            throw new IOException("Error al cargar XML", e);
        }
    }

    // Carga niveles desde un archivo binario usando serialización de Java
    public static Levels loadBin(File file)
        throws FileNotFoundException, IOException, ClassNotFoundException {
        FileInputStream FileInStr = new FileInputStream(file);
        ObjectInputStream ObjInStr = new ObjectInputStream(FileInStr);
        Levels m = (Levels) ObjInStr.readObject();
        return m;
    }

    // Guarda niveles en formato JSON
    private static void saveJSON(Levels levels, File file)
        throws FileNotFoundException, UnsupportedEncodingException {
        try (FileWriter writer = new FileWriter(file)) {
            Gson gson = new GsonBuilder()
                .registerTypeAdapter(
                    Rectangle2D.class,
                    new Rectangle2DAdapterJSON()
                )
                .create();
            gson.toJson(levels, writer);
        } catch (IOException e) {
            throw new RuntimeException("Error al guardar JSON", e);
        }
    }

    // Guarda niveles en formato XML
    private static void saveXML(Levels levels, File file) throws IOException {
        try {
            JAXBContext context = JAXBContext.newInstance(Levels.class);
            Marshaller mr = context.createMarshaller();
            mr.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true); // Formato con indentación
            mr.marshal(levels, file);
        } catch (Exception e) {
            throw new IOException("Error al guardar XML", e);
        }
    }

    // Guarda niveles en formato binario usando serialización
    public static void saveBin(Levels levels, File file)
        throws FileNotFoundException, IOException {
        FileOutputStream FileOutStr = new FileOutputStream(file);
        ObjectOutputStream ObjOutStr = new ObjectOutputStream(FileOutStr);
        ObjOutStr.writeObject(levels);
    }

    // Añade un nivel a la colección
    public void addLevel(Level level) {
        this.levels.add(level);
    }

    // Obtiene el nivel actualmente seleccionado
    public Level getSelected() {
        return this.selected;
    }

    // Obtiene la lista completa de niveles
    public ArrayList<Level> getLevels() {
        return this.levels;
    }

    // Establece el nivel seleccionado directamente
    public void setSelected(Level selected) {
        this.selected = selected;
    }

    // Establece el nivel seleccionado por su índice en la lista
    public void setSelected(int index) {
        this.selected = this.levels.get(index);
    }

    // Establece el nivel seleccionado buscando por nombre
    public void setSelected(String name) {
        this.selected = this.levels.stream()
            .filter(l -> l.getName().equals(name))
            .findFirst()
            .get();
    }

    // Resetea el nivel actualmente seleccionado
    public void resetSelected() {
        this.selected.reset();
    }

    // Obtiene un nivel por su índice
    public Level getLevelByIndex(int index) {
        return this.levels.get(index);
    }

    // Busca un nivel por su nombre
    public Level getLevelByName(String name) {
        return this.levels.stream()
            .filter(l -> l.getName().equals(name))
            .findFirst()
            .get();
    }

    // Elimina un nivel de la colección por su nombre
    public void removeLevel(String name) {
        this.levels.removeIf(level -> level.getName().equals(name));
    }
}
