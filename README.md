# Asyncio image load benchmark

Synchronous, with cv2.imread
```
$ python3 main_sync_imread.py /Users/minhngo/Desktop/Content
Got 1317 files in 26.190 seconds.
```

Synchronous with binary file read
```
$ python3 main_sync.py /Users/minhngo/Desktop/Content
Got 1317 files in 25.528 seconds
```

Asynchronous with binary file read
```
$ python3 main_async.py /Users/minhngo/Desktop/Content
Got 1317 files in 10.839 seconds.
```
