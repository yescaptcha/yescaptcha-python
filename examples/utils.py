from PIL import Image
import base64
from os import remove

def resize_base64_image_from_file(filename, size=None):
    img = Image.open(filename)
    temp_filename = 'temp.png'
    if size:
        width, height = size
        new_img = img.resize((width, height))
        new_img.save(temp_filename)
    else:
        img.save(temp_filename)
    with open(temp_filename, "rb") as f:
        data = f.read()
        encoded_string = base64.b64encode(data)
        remove(temp_filename)
        return encoded_string.decode('utf-8')
    
