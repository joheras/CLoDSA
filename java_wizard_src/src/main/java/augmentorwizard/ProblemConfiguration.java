/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package augmentorwizard;

import java.util.ArrayList;
import java.util.Hashtable;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

/**
 *
 * @author joheras
 */
public class ProblemConfiguration {

    String problem;
    String annotationMode;
    String outputMode;
    String generationMode;
    String inputFolder;
    Hashtable<String, String> parameters = new Hashtable<>();
    ArrayList<Technique> techniques = new ArrayList<>();

    public ProblemConfiguration() {
    }

    public String getProblem() {
        return problem;
    }

    public void setProblem(String problem) {
        this.problem = problem;
    }

    public String getAnnotationMode() {
        return annotationMode;
    }

    public void setAnnotationMode(String annotationMode) {
        this.annotationMode = annotationMode;
    }

    public String getOutputMode() {
        return outputMode;
    }

    public void setOutputMode(String outputMode) {
        this.outputMode = outputMode;
    }

    public String getGenerationMode() {
        return generationMode;
    }

    public void setGenerationMode(String generationMode) {
        this.generationMode = generationMode;
    }

    public String getInputFolder() {
        return inputFolder;
    }

    public void setInputFolder(String inputFolder) {
        this.inputFolder = inputFolder;
    }

    public void addParameter(String parameter, String value) {
        this.parameters.put(parameter, value);
    }

    public Hashtable<String, String> getParameters() {
        return this.parameters;
    }

    public void clearParameters() {
        this.parameters.clear();
    }

    @Override
    public String toString() {
        String result = "ProblemConfiguration{" + "problem=" + problem + ",\n annotationMode=" + annotationMode + ",\n outputMode=" + outputMode + ",\n generationMode=" + generationMode
                + ",\n inputFolder=" + inputFolder + ",\n parameters=" + parameters
                + ",\n techniques={\n";
        for (Technique t : techniques) {
            result = result + t.toString() + "\n";
        }
        return result + '}' + '}';
    }

    public ArrayList<Technique> getTechniques() {
        return techniques;
    }

    public void setTechniques(ArrayList<Technique> techniques) {
        this.techniques = techniques;
    }

    public JSONObject generateJSON() {

        JSONObject json = new JSONObject();
        json.put("problem", problem);
        json.put("annotation_mode", annotationMode);
        json.put("output_mode", outputMode);
        json.put("generation_mode", generationMode);
        json.put("input_path", inputFolder);

        JSONObject param = new JSONObject();
        for (Object p : parameters.keySet().toArray()) {
            param.put((String) p, parameters.get((String) p));
        }
        json.put("parameters", param);

        JSONArray arraytechniques = new JSONArray();

        for (Technique t : techniques) {
            JSONArray tech = new JSONArray();
            tech.add(t.getName());
            JSONObject pa = new JSONObject();
            for (Object p : t.getParameters().keySet().toArray()) {
                pa.put((String) p, t.getParameters().get((String) p));
            }
            tech.add(pa);
            arraytechniques.add(tech);

        }

        json.put("augmentation_techniques", arraytechniques);

        return json;

    }

}
