# internlm2-1.8b-assistant-demo

## 记录
推荐的目录结构
```shell
├─GitHub_Repo_Name
│  ├─app.py                 # Gradio 应用默认启动文件为app.py，应用代码相关的文件包含模型推理，应用的前端配置代码
│  ├─requirements.txt       # 安装运行所需要的 Python 库依赖（pip 安装）
│  ├─packages.txt           # 安装运行所需要的 Debian 依赖项（ apt-get 安装）
|  ├─README.md              # 编写应用相关的介绍性的文档
│  └─... 
```

其他环境安装：若需要安装除了 Python 以外的包，如需要通过 mim 安装 mmcv，可先在 requirement.txt 中填写 mim，然后在 app.py 中写入以下代码，即可完成相关包的安装：
```python
import os
os.system("mim install mmcv-full")
```
