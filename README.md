# Image Thresholding using Bradley-Roth Method

The python file thresholding.py contains functions to process an input image using Bradley-Roth algorithm to threshold the image. Currently used in the course: Observing the Cosmos (AST-1080) at Ashoka University.


Follow the following steps to use the code:

1) Ensure that numba is installed in your conda environment (generally ast1080 for students). If not install using the following command after activating your environment:

   ``` conda install numba ```

   numba is a python package that uses Just-In-Time (JIT) compilation to increase code performance.

2) Download the thresholding.py file at a convenient location on your computer.

3) Use the following command to import the code:

   ```import thresholding as thr ```

4) Access the functions in the file as:

   ``` thr.integral_im(*image_file*) ```

5) First apply the integral_im function to the background separated (masked) image and then use the bradleyroth function.


The bradleyroth function takes 4 arguments: masked image, intergal image, window size, threshold value.

Bsed on: https://people.scs.carleton.ca/~roth/iit-publications-iti/docs/gerh-50002.pdf



Credits: Keerthana Sudarshan for developing the code to implement Bradley-Roth thresholding.
