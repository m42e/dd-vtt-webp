# DD VTT WEBP

Very, very simple script to convert a dd2vtt file from png to webp format.

It is using cwebp and the quality is 85.


## Usge
```
python3 dd2vtt.py <filename>.dd2vtt

```
Advanced:
```
usage: dd2vtt.py [-h] [-q QUALITY] [-t TEMP] [-o OUTPUT] files [files ...]

positional arguments:
  files                 files to convert

optional arguments:
  -h, --help            show this help message and exit
  -q QUALITY, --quality QUALITY
                        set image quality
  -t TEMP, --temp TEMP  temp path
  -o OUTPUT, --output OUTPUT
                        output path
```

WARNING: It overwrites the original file.

## Requirements 
- Python3
- cwebp - should be either in the same directory or in path.
