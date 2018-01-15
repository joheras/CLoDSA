from folderKerasLinearClassificationAugmentor import FolderKerasLinearClassificationAugmentor
from folderKerasSemanticSegmentationAugmentor import FolderKerasSemanticSegmentationAugmentor
from folderLinearClassificationAugmentor import FolderLinearClassificationAugmentor
from folderLinearSemanticSegmentationAugmentor import FolderLinearSemanticSegmentationAugmentor
from hdf5LinearClassificationAugmentor import HDF5LinearClassificationAugmentor
from hdf5LinearLocalizationAugmentor import  HDF5LinearLocalizationAugmentor
from hdf5LinearSegmentationAugmentor import HDF5LinearSegmentationAugmentor
from hdf5PowerClassificationAugmentor import HDF5PowerClassificationAugmentor
from hdf5PowerSegmentationAugmentor import HDF5PowerSegmentationAugmentor
from pascalVOCLinearDetectionAugmentor import PascalVOCLinearDetectionAugmentor
from pascalVOCLinearLocalizationAugmentor import PascalVOCLinearLocalizationAugmentor

# List of augmentors organized by problem, then annotation mode, then output mode, and
# finally generation
Augmentors = {
    "classification" : {
        "folders": {
            "folders": {
                "linear" : FolderLinearClassificationAugmentor,
                },
            "hdf5": {
                "linear" : HDF5LinearClassificationAugmentor,
                "power" : HDF5PowerClassificationAugmentor,
                },
            "keras": {
                "linear" : FolderKerasLinearClassificationAugmentor,
                },
            },
        },

    "localization" : {
        "pascalvoc": {
            "pascalvoc" : {
                "linear" :PascalVOCLinearLocalizationAugmentor
                },
            "hdf5": {
                "linear": HDF5LinearLocalizationAugmentor,
            },

            },
        },

    "detection" : {
        "pascalvoc": {
            "pascalvoc" : {
                "linear" : PascalVOCLinearDetectionAugmentor
                },

            },
        },

    "semantic_segmentation" : {
        "folders": {
            "folders": {
                "linear": FolderLinearSemanticSegmentationAugmentor,
            },
            "hdf5": {
                "linear": HDF5LinearSegmentationAugmentor,
                "power": HDF5PowerSegmentationAugmentor,
            },
            "keras": {
                "linear": FolderKerasSemanticSegmentationAugmentor,
            },
        },
    },
}


def createAugmentor(problem,annotationmode,outputmode,generationmode,inputPath,parameters):
    Augmentor = Augmentors[problem][annotationmode][outputmode][generationmode]
    if Augmentor is None:
        raise ValueError("These parameters are not currently supported")

    return Augmentor(inputPath,parameters)
