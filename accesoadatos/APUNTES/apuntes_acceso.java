// Adaptador aparte de una clase
public class Rectangle2DAdapterJSON implements JsonSerielizer<Rectangle2D>, JsonDeserializer<Rectangle2D> {

    @Override
    public JsonElement serialize(Rectangle2D src, Type typeOfSrc, JsonSerializationContext context) {
        JsonObject obj = new JsonObject();
        obj.addProperty("minX", src.getMinX());
        return obj;
    }
    @Override
    public Rectangle2D deserialize(JsonElement json, Type typeofT, JsonDeserializationContext context) throws JsonParseException {
        JsonObject obj = json.getAsJsonObject();
        return new Rectangle2D(
                obj.get("minX").getAsDouble()
                );
    }
}

// Pasar y guardar JSON
private static void saveJSON(Levels levels, File file) throws IOException {
    Gson gson = new GsonBuilder().registerTypeAdapter(Rectangle2D.class, new Rectangle2DAdapterJSON())
    .setPrettyPrinting().create();

    try (DileWriter writer = new FileWriter(file)) {
        gson.toJson(levels, writer);
    }
}

// Marshal, adaptador XML
// SAVE
private static void saveXML(Levels levels, File file) throws IOException, JABXException {
    JABXContent levelsContext = JAXBContent.newInstance(Levels.class);
    Marshaller levelsMarshaller = levelsContext.createMarshaller();
    levelsMarshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
    levelsContext.setAdapter(new Rectangle2DAdapterXML());
    levelsMarshaller.marshal(levels, file);
}

//LOAD
private static void loadXML(File file) throws JAXBException {
    JAXBContent levelsContext = JAXBContent.newInstance(Levels.class);
    Unmarshaller levelsUnMarshaller = levelsContext.createUnMarshaller();
    return (Levels) levelsUnMarshaller.unmarshal(file);
}

// ADAPTER
public clalss Rectangle2DAdapterXML extends XmlAdapter<String, Rectangle2D> {
    @Override
    public Rectangle2D unmarshal(String v) throws Exception {
        if (v == null || v.isEmpty()) {
            return null;
        }
        String[] parts = v.split(",");
        double x = Double.parseDouble(parts[0]);
        return new Rectangle2D(x);
    }
    @Override
    public String marshal(Rectangle2D v) throws Exception {
        if (v == null) {
            return null;
        }
        return v.getMinX() + ",";
    }
}