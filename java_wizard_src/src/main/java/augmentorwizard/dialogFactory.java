/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package augmentorwizard;

import java.io.File;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

/**
 *
 * @author joheras
 */
public class dialogFactory {

    public static String pathDialog(javax.swing.JFrame dialog, String help) {
        JFileChooser fc = new JFileChooser();
        fc.setCurrentDirectory(new java.io.File(".")); // start at application current directory
        fc.setDialogTitle(help);
        fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        int returnVal = fc.showSaveDialog(dialog);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            File yourFolder = fc.getSelectedFile();
            return yourFolder.getAbsolutePath();
        } else {
            return "";
        }

    }

    public static String inputDialog(javax.swing.JFrame dialog, String help, String defaultValue) {
        String selection = JOptionPane.showInputDialog(dialog, help,defaultValue);
        return selection;
    }
    
    public static String optionDialog(javax.swing.JFrame dialog, String help, Object[] options,String defaultValue) {
        String selection =  (String) JOptionPane.showInputDialog(dialog, help,"",JOptionPane.DEFAULT_OPTION,null,options,defaultValue);
        return selection;
    }

}
