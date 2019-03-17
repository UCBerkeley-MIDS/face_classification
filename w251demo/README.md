# Concatenate video files

```console
ls *.avi | while read each; do echo "file '$each'" >> angrylist.txt; done
ffmpeg -f concat -i angrylist.txt -c copy afew_train_angry.avi
```
