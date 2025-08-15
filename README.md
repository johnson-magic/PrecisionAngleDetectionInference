# PrecisionAngleDetectionInference

- [PrecisionAngleDetectionInference](#precisionangledetectioninference)
  - [以可执行文件的方式运行](#以可执行文件的方式运行)
  - [以python的方式运行](#以python的方式运行)
    - [方式1: 傻瓜式安装、运行](#方式1-傻瓜式安装运行)
    - [方式2: 通过指令安装、运行](#方式2-通过指令安装运行)
  - [以c++的方式运行](#以c的方式运行)
  - [其他](#其他)
    - [耗时测试](#耗时测试)
    - [一致性测试](#一致性测试)
## 以可执行文件的方式运行
* 百度网盘链接
链接: https://pan.baidu.com/s/1x3SUV20z9mPBk_j4Bvj_lw
提取码: 1234
## 以python的方式运行
### 方式1: 傻瓜式安装、运行
* 双击*click_me_to_install.bat*安装程序
* 双击*click_me_to_run.bat*运行程序
  
### 方式2: 通过指令安装、运行
1. 安装python

* 在Windows Command下安装miniconda
```
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
.\miniconda.exe
del miniconda.exe
```

2. 安装环境
* 在Anaconda Prompt下通过conda env安装环境
```
conda create -n angle-detector
conda activate angle-detector
conda install python=3.10.12
git clone https://github.com/johnson-magic/PrecisionAngleDetectionInference
cd PrecisionAngleDetectionInference
python -m pip install --upgrade pip
pip install -r requirements.txt
```


3. 启动程序
```
python infer.py
```
## 以c++的方式运行
* 安装依赖
  * 安装依赖1 cmake version3.31.2
  1. 下载安装包[cmake-3.31.2-windows-x86_64.msi](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiiroap6LyKAxVvoK8BHSB1OTEQFnoECBsQAQ&url=https%3A%2F%2Fgithub.com%2FKitware%2FCMake%2Freleases%2Fdownload%2Fv3.31.2%2Fcmake-3.31.2-windows-x86_64.msi&usg=AOvVaw0ASiI58DNp2YXaovaNPeAI&opi=89978449)至合适位置。

  2. 双击cmake-3.31.2-windows-x86_64.msi安装
* 安装依赖2 opencv version4.10.0
  1. 下载安装包[opencv-4.10.0-windows.exe](https://objects.githubusercontent.com/github-production-release-asset-2e65be/5108051/9eeaf5f2-33b3-46dc-8442-55e9c3473acf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20241223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241223T022237Z&X-Amz-Expires=300&X-Amz-Signature=5dcd6941a55ba5eb162261dd18261b3de81a1d836acbbb6e4646f0d01dd27502&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3Dopencv-4.10.0-windows.exe&response-content-type=application%2Foctet-stream)至合适位置。
  2. 双击opencv-4.10.0-windows.exe安装

* 安装依赖3：onnxruntime version 1.15.1
  1. 下载安装包[onnxruntime-win-x64-1.15.1.zip](https://objects.githubusercontent.com/github-production-release-asset-2e65be/156939672/2fcf4e59-ff23-4de1-9070-f46aa9060367?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20241223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241223T022859Z&X-Amz-Expires=300&X-Amz-Signature=997a22499d5c284cee1e586ecc1f93e5173a07543eaa85a1e647c086094acdf4&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3Donnxruntime-win-x64-1.15.1.zip&response-content-type=application%2Foctet-stream)至合适位置。
  2. 解压onnxruntime-win-x64-1.15.1.zip



* 运行程序
```
git clone --recursive https://github.com/johnson-magic/PrecisionAngleDetectionInference.git
cd PrecisionAngleDetectionInference/cpp
```
打开CMakeLists.txt文件，修改以下三行为对应的路径
```
include_directories("C:/Users/24601/Desktop/fabu/code/PrecisionAngleDetectionInference/cpp")
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} "C:/Users/24601/Desktop/fabu/software/onnxruntime-win-x64-1.15.1/onnxruntime-win-x64-1.15.1/lib/onnxruntime.lib")
include_directories("C:/Users/24601/Desktop/fabu/software/onnxruntime-win-x64-1.15.1/onnxruntime-win-x64-1.15.1/include")
```
继续执行如下命令
```
mkdir build
cmake -B ./build -DCMAKE_BUILD_TYPE=Release
cmake --build ./build/ --config Release
```
可执行文件，会生成于```build\Release\ONNXInference.exe```
执行

```./ONNXInference.exe best.onnx A-2024-01-03-14-13-09_000032.jpg res.txt vis.png```

* 结果展示
会生成两个结果

文本结果res.txt如下：
```
Centerpoint: 572.353,1074.48
angle: -0.740156
SliderAngle: -120.123
Diameter: 927.943
SliderCenterPoint: 397,1362.01
Position: below
```

可视化vis.png如下：

<img src="./imgs/vis.png" height=500 width=300>

## 其他
### 耗时测试
&emsp;&emsp;如果想测试程序运行的事件消耗，可以执行如下指令：

* c++ version
```
cmake -B ./build -DCMAKE_BUILD_TYPE=Release -DSPEED_TEST=ON
cmake --build ./build/ --config Release
```

* python version
```
# 打开infer.py文件中的speed_test为True
python infer.py
```

|模块名称|c++耗时(ms)|python耗时(ms)|
|---|---|---|
|总|538|2023|
|inferencer总|274|1316|
|inferencer-preprocess|63|略|
|inferencer-inference|198|略|
|inferencer-postprocess|13|略|
|angle_detector-总|263|708|
|angle_detector-process|0|16|
|angle_detector-saveres|2|3|
|angle_detector-savevis|261|689|

### 一致性测试

|类别|python测试结果|c++测试结果|
|---|---|---|
|big_circle|(91, 1551), (1025, 1552), (1027, 617), (92, 616)|(91, 1551), (1025, 1552), (1027, 617), (92, 616)|
|plates|(1038, 1207), (1039, 961), (101, 960), (101, 1205)|(1038, 1207), (1039, 961), (101, 960), (101, 1205)|
|slide|(600, 847), (753, 934), (862, 742), (709, 655)|(600, 847), (753, 934), (862, 742), (709, 655)|
