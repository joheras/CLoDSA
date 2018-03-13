from techniqueList import  Techniques

def createTechnique(technique,parameters):
    Technique = Techniques[technique]
    if Technique is None:
        raise ValueError("That technique is not available")
    return Technique(parameters)