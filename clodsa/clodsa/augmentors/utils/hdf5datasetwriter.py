import h5py
import os
import sys

class HDF5DatasetWriterClassification:

    def __init__(self,dims,outputPath,dataKey="images",bufSize=1000):

        if os.path.exists(outputPath):
            raise ValueError("The output path already exists")

        self.db = h5py.File(outputPath,"w")
        self.data = self.db.create_dataset(dataKey,dims,dtype="float")
        self.labels = self.db.create_dataset("labels",(dims[0],),dtype="int")
        self.bufSize = bufSize
        self.buffer = {"data":[],"labels":[]}
        self.idx = 0

    def add(self,rows,labels):
        self.buffer["data"].extend(rows)
        self.buffer["labels"].extend(labels)
        if len(self.buffer["data"]) >= self.bufSize:
            self.flush()

    def flush(self):
        i = self.idx + len(self.buffer["data"])
        self.data[self.idx:i] = self.buffer["data"]
        self.labels[self.idx:i] = self.buffer["labels"]
        self.idx = i
        self.buffer = {"data": [], "labels":[]}

    def storeClassLabels(self,classLabels):
        if sys.version_info[0]<3:
            dt = h5py.special_dtype(vlen=unicode)
        else:
            dt = h5py.special_dtype(vlen=str)
        labelSet = self.db.create_dataset("label_names",
                                          (len(classLabels),),dtype=dt)
        labelSet[:] = classLabels

    def close(self):
        if len(self.buffer["data"]) > 0:
            self.flush()
        self.db.close()


class HDF5DatasetWriterSegmentation:

    def __init__(self,dims,outputPath,dataKey="images",bufSize=1000):

        if os.path.exists(outputPath):
            raise ValueError("The output path already exists")

        self.db = h5py.File(outputPath,"w")
        self.data = self.db.create_dataset(dataKey,dims,dtype="float")
        self.labels = self.db.create_dataset("labels",dims,dtype="float")
        self.bufSize = bufSize
        self.buffer = {"data":[],"labels":[]}
        self.idx = 0

    def add(self,rows,labels):
        self.buffer["data"].extend(rows)
        self.buffer["labels"].extend(labels)
        if len(self.buffer["data"]) >= self.bufSize:
            self.flush()

    def flush(self):
        i = self.idx + len(self.buffer["data"])
        self.data[self.idx:i] = self.buffer["data"]
        self.labels[self.idx:i] = self.buffer["labels"]
        self.idx = i
        self.buffer = {"data": [], "labels":[]}

    def close(self):
        if len(self.buffer["data"]) > 0:
            self.flush()
        self.db.close()


class HDF5DatasetWriterLocalization:

    def __init__(self,dims,outputPath,dataKey="images",bufSize=1000):

        if os.path.exists(outputPath):
            raise ValueError("The output path already exists")

        self.db = h5py.File(outputPath,"w")
        self.data = self.db.create_dataset(dataKey,dims,dtype="float")
        self.labels = self.db.create_dataset("labels",(dims[0],5),dtype="float")
        self.bufSize = bufSize
        self.buffer = {"data":[],"labels":[]}
        self.idx = 0

    def add(self,rows,labels):
        self.buffer["data"].extend(rows)
        self.buffer["labels"].extend(labels)
        if len(self.buffer["data"]) >= self.bufSize:
            self.flush()

    def flush(self):
        i = self.idx + len(self.buffer["data"])
        self.data[self.idx:i] = self.buffer["data"]
        self.labels[self.idx:i] = self.buffer["labels"]
        self.idx = i
        self.buffer = {"data": [], "labels":[]}

    def close(self):
        if len(self.buffer["data"]) > 0:
            self.flush()
        self.db.close()