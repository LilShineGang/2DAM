/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ies.pedro.model;


import javafx.geometry.Rectangle2D;
import jakarta.xml.bind.annotation.*;
import jakarta.xml.bind.annotation.adapters.XmlJavaTypeAdapter;

import java.io.Serializable;
import ies.pedro.utils.Rectangle2DAdapterXML;

// serializable para poder trabajar con binario
@XmlAccessorType(XmlAccessType.FIELD) // Indica que JAXB debe acceder a los campos directamente para XML
public class Block implements Serializable {

    // tipo de bloque
    private String type;

    // Rectángulo que define la posición y tamaño del bloque en el nivel
    // Usa un adaptador personalizado para convertir Rectangle2D a/desde XML
    @XmlJavaTypeAdapter(Rectangle2DAdapterXML.class)
    private Rectangle2D rect;
    
    // constructor para deserialización
    public Block(){
        this.type=null;
    }
    
    // para crear bloque con tipo y posicion
    public Block(String type,Rectangle2D rectangle){
        this.type=type;
        this.rect=rectangle;
    }

    // Obtiene el rectángulo (posición y dimensiones) del bloque
    public Rectangle2D getRectangle() {
        return rect;
    }
    
    // Establece el rectángulo (posición y dimensiones) del bloque
    public void setRectangle(Rectangle2D rectangle) {
        this.rect=rectangle;
    }
    
    // me da el tipo de bloque
    public String getType(){
        return this.type;
    }
    
    // me dice el tipo de bloque
    public void setType(String type){
        this.type=type;
    }
    
    // mira a ver si el bloque está vacío
    public boolean isEmpty(){
        return this.type==null;
    }
    
    // Representación en texto del bloque para debugging
    @Override
    public String toString(){
        return this.type+" "+this.rect;
    }

}
