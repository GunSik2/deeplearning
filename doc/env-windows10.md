## Deeplearning experiment environment
### Env
- Windows 10

### Installation
- Cygwin: https://www.cygwin.com/ 
  - + winpty: https://github.com/rprichard/winpty
- Visual Studio (Visual C++ 14.0): https://www.visualstudio.com/downloads/
- CUDA Installation: https://developer.nvidia.com/cuda-downloads
- CUDNN - CUDA for Deep Neural Networks: https://developer.nvidia.com/cudnn
  - add "C:\tools\cuda\bin" to PATH (the directory including cudnn64_5.dll)
- Anaconda 
- Conda without GPU
```
conda create --name tensorflow python=3.5
source activate tensorflow
conda install jupyter
conda install scipy
pip install tensorflow-gpu
```
- Conda with GPU 
```
conda create --name tensorflow-gpu python=3.5
source activate tensorflow-gpu
conda install jupyter
conda install scipy
pip install tensorflow-gpu
```
### Test
- test program
```
$ cat gpu.py

import tensorflow as tf

a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))
```
- run in tensorflow env.
```
$ source activate tensorflow
$ python gpu.py
Device mapping:
MatMul: (MatMul): /job:localhost/replica:0/task:0/cpu:0
$ source deactivate tensorflow
```
- run in tensorflow-gpu env.
```
$ source activate tensorflow-tf
$ python gpu.py
Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GeForce GT 710, pci bus id: 0000:01:00.0
MatMul: (MatMul): /job:localhost/replica:0/task:0/gpu:0
$ source deactivate tensorflow-tf
```
## Reference
- http://www.heatonresearch.com/2017/01/01/tensorflow-windows-gpu.html
- https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/g3doc/how_tos/using_gpu/
- https://community.cablelabs.com/wiki/display/OCORI/Build+Environment+-+Cygwin+MinGW
