
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os,sys

caffe_root="/home/nsk/Project/caffe/"

image_path=sys.argv[1]


import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

plt.rcParams['figure.figsize']=(10,10)
plt.rcParams['image.interpolation']='nearest'
plt.rcParams['image.cmap']='gray'

caffe.set_mode_cpu()

net=caffe.Net(caffe_root+'models/bvlc_reference_caffenet/deploy.prototxt',caffe_root+'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel',
	caffe.TEST)
# input preprocessing: 'data' is the name of the input blob == net.inputs[0]
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_mean('data', np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1)) # mean pixel
transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB



# set net to batch size of 50
net.blobs['data'].reshape(50,3,227,227)

net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(image_path))
out = net.forward()
print("Predicted class is #{}.".format(out['prob'][0].argmax()))

plt.imshow(transformer.deprocess('data', net.blobs['data'].data[0]))

# load labels
imagenet_labels_filename = caffe_root + 'data/ilsvrc12/synset_words.txt'
try:
    labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')
except:
    os.system("../data/ilsvrc12/get_ilsvrc_aux.sh")
    labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

# sort top k predictions from softmax output
top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]

#print image_path
file_name=image_path.split("/")[-1]
file_name_temp=file_name.split(".")[0]
file_name2=file_name_temp+".txt"
path="/home/nsk/Desktop/Start/Begin1/Files/"
dest_file_path=path+file_name2
#print dest_file_path

key_path=dest_file_path.replace(".",";")
value_path=image_path.replace(".",";")

print key_path
print value_path

fp1=open(dest_file_path,"wb+")

for i in range (0,len(top_k)):
	fp1.write(labels[top_k[i]][10:])

fp1.close()

a=Database("MuDaM")
a.set_collection("Files")
a.add_entry(key_path,value_path)
a.close()





