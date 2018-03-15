Follow these steps for execution:
1. Download and install 'caffe', with CPU_ONLY:=1 (parameter in Makefile.config). The caffe folder should reside in:
/home/nsk/Project/
(The project code uses the python wrappers of caffe. So run: make pycaffe after installation. Also, download and install the bvlc_caffenet_reference model. If not, it will be installed when the caffe_example.py file is run for the first time from the code automatically).
2. Extract the contents of the 'Code' folder from the zip file to the folder:
/home/nsk/Desktop/Start/Begin1
3. Copy the database.py and caffe_example.py files to the following foler:
/home/nsk/Project/caffe/examples/
4. Place the Test_Folder in:
/home/nsk/
5. The following dependencies are needed for caffe and python: (can be installed via pip)
Cython>=0.19.2
numpy>=1.7.1
scipy>=0.13.2
scikit-image>=0.9.3
matplotlib>=1.3.1
ipython>=3.0.0
h5py>=2.2.0
leveldb>=0.191
networkx>=1.8.1
nose>=1.3.0
pandas>=0.12.0
python-dateutil>=1.4,<2
protobuf>=2.5.0
python-gflags>=2.0
pyyaml>=3.10
Pillow>=2.3.0
six>=1.1.0

6. Following are the dependencies required for the entire project:
python magic
hachoir-metadata and hachoir-core (python)
pyqt4
pyuic4
mongodb
R:
    The following R packages are required:
    1.tm
    2.topicmodels
    3.cluster
    4.ade4
    5.SnowballC
    6.LDAvis
    
7. Run the main program as:
    $python Run1.py
    Select Basic Clustering and select Test_Folder located in: /home/nsk/Test_Folder
