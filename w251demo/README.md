# Concatenate video files

```console
ls *.avi | while read each; do echo "file '$each'" >> angrylist.txt; done
ffmpeg -f concat -i angrylist.txt -c copy afew_train_angry.avi
```

# Tk issue on TX2

You may see the error message like the following:

```console
(w251py) nvidia@tegra-ubuntu:/mnt/w251/pei/w251/face_classification/src$ python video_playback_emotion_demo.py
Using TensorFlow backend.
Traceback (most recent call last):
  File "/usr/lib/python3.5/tkinter/__init__.py", line 36, in <module>
    import _tkinter
ImportError: No module named '_tkinter'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "video_playback_emotion_demo.py", line 11, in <module>
    from utils.inference import detect_faces
  File "/mnt/w251/pei/w251/face_classification/src/utils/inference.py", line 2, in <module>
    import matplotlib.pyplot as plt
  File "/mnt/w251/pei/w251/w251py/lib/python3.5/site-packages/matplotlib/pyplot.py", line 2372, in <module>
    switch_backend(rcParams["backend"])
  File "/mnt/w251/pei/w251/w251py/lib/python3.5/site-packages/matplotlib/pyplot.py", line 207, in switch_backend
    backend_mod = importlib.import_module(backend_name)
  File "/mnt/w251/pei/w251/w251py/lib/python3.5/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/mnt/w251/pei/w251/w251py/lib/python3.5/site-packages/matplotlib/backends/backend_tkagg.py", line 1, in <module>
    from . import _backend_tk
  File "/mnt/w251/pei/w251/w251py/lib/python3.5/site-packages/matplotlib/backends/_backend_tk.py", line 5, in <module>
    import tkinter as Tk
  File "/usr/lib/python3.5/tkinter/__init__.py", line 38, in <module>
    raise ImportError(str(msg) + ', please install the python3-tk package')
ImportError: No module named '_tkinter', please install the python3-tk package
```

But the __python3-tk packages__ is already installed.


```console
(w251py) nvidia@tegra-ubuntu:/mnt/w251/pei/w251/face_classification/src$ sudo apt-get install python3-tk
Reading package lists... Done
Building dependency tree
Reading state information... Done
python3-tk is already the newest version (3.5.1-1).
0 upgraded, 0 newly installed, 0 to remove and 281 not upgraded.
(w251py) nvidia@tegra-ubuntu:/mnt/w251/pei/w251/face_classification/src$ dpkg -l python3-tk
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                          Version             Architecture        Description
+++-=============================-===================-===================-================================================================
ii  python3-tk                    3.5.1-1             arm64               Tkinter - Writing Tk applications with Python 3.x
```

You have two options:

   - uncomment the following two lines in `video_playback_emotion_demo.py`:

     ```python
        import matplotlib
        matplotlib.use('agg')
      ```
   - or use the matplotlib configuration file as following:

     ```console
        echo "backend : Agg" > /home/nvidia/.config/matplotlib/matplotlibrc
     ```
