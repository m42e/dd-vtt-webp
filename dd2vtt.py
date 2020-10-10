import sys
import subprocess
import json
import base64
import io
with open(sys.argv[1]) as fin:
    data = json.load(fin)

print(data.keys())
with open('_tmpimg.png' ,'wb') as imgout:
    imgout.write(base64.b64decode(data['image']))

subprocess.check_output(['cwebp', '-q', '85', '_tmpimg.png', '-o', 'tmpimg.webp'])

with open('tmpimg.webp', 'rb') as imgin:
    newimage = base64.b64encode(imgin.read()).decode('utf8')

data['image'] = newimage


with open(sys.argv[1], 'w') as fout:
    json.dump(data, fout)
