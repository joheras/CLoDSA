from __future__ import absolute_import
from .transformerForImageClassification import TransformerForImageClassification
from .transformerForImageDetection import TransformerForImageDetection
from .transformerForImageInstanceSegmentation import TransformerForImageInstanceSegmentation
from .transformerForImageLocalization import TransformerForImageLocalization
from .transformerForImageSegmentation import TransformerForImageSegmentation
from .transformerForImageStackClassification import TransformerForImageStackClassification


Transformers = {
    "classification" : TransformerForImageClassification,
    "localization" : TransformerForImageLocalization,
    "detection" : TransformerForImageDetection,
    "semantic_segmentation" : TransformerForImageSegmentation,
    "instance_segmentation" : TransformerForImageInstanceSegmentation,
    "stackclassification" : TransformerForImageStackClassification,
    
}