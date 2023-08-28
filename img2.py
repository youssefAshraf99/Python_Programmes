import numpy as np
import matplotlib.pyplot as plt
from skimage import data, io
from skimage.restoration import  denoise_bilateral
from skimage.filters import threshold_otsu
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb, rgb2gray


image = io.imread('http://upload.wikimedia.org/wikipedia/commons/6/60/Gel_electrophoresis_2.jpg')


#grayscaling
gray_image = rgb2gray(image)

# bilateral filtering
bilat=denoise_bilateral(gray_image,sigma_color=0.05,sigma_spatial=20)

# apply threshold Otsu
thresh = threshold_otsu(bilat)
bw = closing(bilat > thresh, square(1))

#print process
def show_images(images,titles=None):
    """Display a list of images"""
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n) 
        if image.ndim == 2: 
            plt.gray() 
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()

#print data
show_images(images=[image, bilat, bw], titles=['Normal', 'Bilateral filter', 'Otsu Threshold'])
