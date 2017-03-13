
## Env
- [Visual C++ Compiler 2015](http://landinghub.visualstudio.com/visual-cpp-build-tools)  - Visual C++ 2015 Build Tool 설치
- [CUDA Drivers 8.0](https://developer.nvidia.com/cuda-downloads)  - cuda_8.0.61_win10 설치
- [CUDNN 5.1](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v5.1/prod_20161129/8.0/cudnn-8.0-windows10-x64-v5.1-zip) - 다운 받은 파일을 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0 에 복사
- [Python 3.6](https://www.python.org/downloads/) : Windows x86-64 executable installer
- [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows)

### virtualenv
```
pip install virtualenv
pip install virtualenwrapper-win
mkvirtualenv tensorflow
> deactivate
workon tensorflow
```

### jupyter
```
pip install jupyter
git clone https://github.com/GunSik2/deeplearning
cd deeplearning
jupyter notebook
```

### [GPU Test](http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html)
```
(tensorflow-gpu) >python
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> import tensorflow as tf
I c:\tf_jenkins\home\workspace\release-win\device\gpu\os\windows\tensorflow\stream_executor\dso_loader.cc:135] successfully opened CUDA library cublas64_80.dll locally
I c:\tf_jenkins\home\workspace\release-win\device\gpu\os\windows\tensorflow\stream_executor\dso_loader.cc:135] successfully opened CUDA library cudnn64_5.dll locally
I c:\tf_jenkins\home\workspace\release-win\device\gpu\os\windows\tensorflow\stream_executor\dso_loader.cc:135] successfully opened CUDA library cufft64_80.dll locally
I c:\tf_jenkins\home\workspace\release-win\device\gpu\os\windows\tensorflow\stream_executor\dso_loader.cc:135] successfully opened CUDA library nvcuda.dll locally
I c:\tf_jenkins\home\workspace\release-win\device\gpu\os\windows\tensorflow\stream_executor\dso_loader.cc:135] successfully opened CUDA library curand64_80.dll locally

>>> sess = tf.Session()
I c:\tf_jenkins\home\workspace\release-win\device\gpu\os\windows\tensorflow\core\common_runtime\gpu\gpu_device.cc:885] Found device 0 with properties:
name: GeForce GTX 1060 6GB
major: 6 minor: 1 memoryClockRate (GHz) 1.759
pciBusID 0000:02:00.0
Total memory: 6.00GiB
Free memory: 5.01GiB
W c:\tf_jenkins\home\workspace\release-win\device\gpu\os\windows\tensorflow\stream_executor\cuda\cuda_driver.cc:590] creating context when one is currently active; existing: 0000024C399F1A20

>>> hello_world = tf.constant("Hello, TensorFlow!") 

>>> print sess.run(hello_world) 
Hello, TensorFlow! 

>>> print sess.run(tf.constant(123)*tf.constant(456)) 
56088 - See more at: http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html#sthash.8PqQ4Fe9.dpuf
```
