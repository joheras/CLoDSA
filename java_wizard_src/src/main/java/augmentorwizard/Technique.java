/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package augmentorwizard;

import java.util.Hashtable;

/**
 *
 * @author joheras
 */
public class Technique {
    
    private String name;
    private Hashtable<String,String> parameters = new Hashtable<>();

    public Technique(String name) {
        this.name = name;
    }
    
    
    public void addParameters(String parameter, String value){
        this.parameters.put(parameter, value);
    }

    public String getName() {
        return name;
    }

    public Hashtable<String, String> getParameters() {
        return parameters;
    }

    @Override
    public String toString() {
        return "Technique{" + "name=" + name + ", parameters=" + parameters + '}';
    }
    
    
    
    
    
}
