# Image Filtering Implementation from Scratch

This script demonstrates how to apply spatial filtering to images using a custom convolution function in Python, rather than relying on OpenCV's built-in `cv2.filter2D`. It applies a 9x9 Average Filter (Box Filter) to a grayscale image to visualize the blurring effect.

## Prerequisites

Ensure you have the required Python libraries installed:

    pip install opencv-python matplotlib numpy

## How to Use

1. Update the image path in the script. It currently reads from `/content/drive/MyDrive/dove.jpg`. Change this to your local image path:
       
       img = cv2.imread('path/to/your/image.jpg')
       
2. Run the script in your terminal or Python environment.
### Note: You can directly open the `.ipynb` file in Colab or Jupyter Notebook.

## How it Works

1. **Image Loading**: The image is loaded and converted to grayscale mode using `cv2.cvtColor`.
2. **Custom Convolution**: The `image_filtering` function manually calculates the convolution using nested loops, which mimics the behavior of a CNN convolutional layer or a spatial filter.
3. **Kernel Creation**: Creates a mathematically normalized 9x9 matrix.
4. **Visualization**: Uses Matplotlib to display a side-by-side comparison of the original image against the blurred output.

#OUTPUT
<img width="1224" height="591" alt="image" src="https://github.com/user-attachments/assets/6df2efc1-6d70-43d0-ad87-738005b4cd84" />
