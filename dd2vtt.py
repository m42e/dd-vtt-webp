import logging
import pathlib
import subprocess
import json
import base64
import io

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def parse_args(args=None):
    import sys
    import argparse
    if args is None:
        args = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='+', type=str, help="files to convert")
    parser.add_argument("-q", "--quality", type=int, help="set image quality", default=85)
    parser.add_argument("-t", "--temp", type=str, help="temp path", default=".")
    parser.add_argument("-o", "--output", type=str, help="output path", default=".")
    return parser.parse_args(args)


def convert_file(file, quality=85, output=pathlib.Path('.'), temp=pathlib.Path('.')):
    _logger.info("COnverting %s", file)
    try:
        with open(file) as fin:
            data = json.load(fin)
        imagedata = base64.b64decode(data['image'])
    except:
        _logger.error("Could not load file %s", file)
        return


    try:
        with open(temp /'_tmpimg.png' ,'wb') as imgout:
            imgout.write(imagedata)
    except:
        _logger.error("could not write temp file")
        return

    try:
        res = subprocess.check_output(['cwebp', '-q', str(quality), temp / '_tmpimg.png', '-o', temp / 'tmpimg.webp'])
        with open(temp / 'tmpimg.webp', 'rb') as imgin:
            newimage = base64.b64encode(imgin.read()).decode('utf8')
    except:
        _logger.error("could not run cwebp")
        _logger.error(res)
        return

    data['image'] = newimage

    try:
        with open(output / file.name, 'w') as fout:
            json.dump(data, fout)
    except:
        _logger.error("could not write file")
        return

def main():
    args = parse_args()
    for file in args.files:
        convert_file(pathlib.Path(file).resolve(), args.quality, pathlib.Path(args.temp), pathlib.Path(args.output))

if __name__ == '__main__':
    main()
