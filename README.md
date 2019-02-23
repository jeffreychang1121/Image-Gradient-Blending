# Image-Gradient-Blending

## 1. Gradient Domain Blending
### 1.1 Align the Source Image and Create its Mask
       [mask]=maskImage(img)
  - (INPUT) img: *h* x *w* x 3 matrix representing the source image
  - (OUTPUT) mask: *h* x *w* matrix representing the logical mask
### 1.2 Index the Pixels
       [indexes] = getIndexes(mask, targetH, targetW, offsetX, offsetY)
   - (INPUT) mask: The logical matrix *h* x *w* representing the replacement region
   - (INPUT) targetH: The height of the target image, *h0*
   - (INPUT) targetW: The width of the target image, *w0*
   - (INPUT) offsetX: The x-axis offset of the source image with respect to the target image
   - (INPUT) offsetY: The y-axis offset of the source image with respect to the target image
   - (OUTPUT) indexes: *h0* x *w0* matrix representing the indices of each replacement pixel, and the value 0 means that is not a replacement pixel
### 1.3 Compute the Coefficient Matrix
        [coeffA] = getCoefficientMatrix(indexes)
- (INPUT) indexes: *h0* x *w0* matrix representing the indices of each replacement pixel
- (OUTPUT) coeffA: an *N* x *N* sparse matrix representing the Coefficient Matrix, where N is the number of replacement pixels
### 1.4 Compute the Solution Vector
        [solVectorb] = getSolutionVect(indexes, source, target, offsetX, offsetY)
- (INPUT) indexes: *h0* x *w0* matrix representing the indices of each replacement pixel
- (INPUT) source: *h* x *w* matrix representing one color channel of the source image
- (INPUT) target: *h0* x *w0* matrix representing one color channel of target image
- (INPUT) offsetX: The x-axis offset of the source image with respect to the target image
- (INPUT) offsetY: The y-axis offset of the source image with respect to the target image
- (OUTPUT) solVectorb: 1 x *N* vector representing the solution vector
### 1.5 Seamlessly Clone the Image
        [resultImg] = reconstructImg(indexes, red, green, blue, targetImg)
- (INPUT) indexes: *h0* x *w0* matrix representing the indices of each replacement pixel
- (INPUT) red: 1 x *N* vector representing the intensity of the red channel replacement pixel
- (INPUT) green: 1 x *N* vector representing the intensity of the green channel replacement pixel
- (INPUT) blue: 1 x *N* vector representing the intensity of the blue channel replacement pixel
- (INPUT) targetImg: *h0* x *w0* x 3 matrix representing the target image
- (OUTPUT) resultImg: *h0* x *w0* x 3 matrix representing the resulting cloned image
### 1.6 Wrapper Function
        [resultImg] = seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY)
- (INPUT) sourceImg: *h* x *w* x 3 matrix representing the source image.
- (INPUT) targetImg: *h0* x *w0* x 3 matrix representing the target image.
- (INPUT) mask: The logical matrix *h* x *w* representing the replacement region.
- (INPUT) offsetX: The x-axis offset of the source image with respect to the target image.
- (INPUT) offsetY: The y-axis offset of the source image with respect to the target image.
- (OUTPUT) resultImg: *h0* x *w0* x 3 matrix representing the resulting cloned image.
