import os
from PIL import Image
from pathlib import Path
from flask import flash

# Get the file size and convert it to KB
def image_size(file):
    size_bytes = os.path.getsize(file)
    size_kb = size_bytes / 1024
    return int(size_kb)

# Change the image path
def change_path(file):
    relative_path = file[0] 
    normalized_path = relative_path.replace('\\', '/')   
    full_path = Path('app/static') / normalized_path
    return full_path

# Change the name of the compressed image
def change_file_name(original_path):
    name, extension = os.path.splitext(original_path)
    file_name = os.path.basename(name)
    new_name = f"{os.path.dirname(original_path)}\\OneCompress_{file_name}{extension}"
    return new_name

# Display image
def show_img(path):
    img = Image.open(path)
    img.show()

# Resize the image and get its size
def resize_img(file_path):
    print(file_path)
    with Image.open(file_path) as img:
        img.thumbnail((2200, 1238))
        if img.mode != 'RGB' and img.mode != 'CMYK':
            img = img.convert('RGB')
        newPath = change_file_name(file_path)
        img.save(newPath, format="JPEG", quality=100)
        original_weight = image_size(newPath)
    return original_weight, newPath       

# Compress 2D images
def CompressImg2d(get_original_weight, newPath, quality):
    print(f"Compress {get_original_weight} {newPath} {quality}")
    with Image.open(newPath) as img:
        img.save(newPath, format="JPEG", quality=quality)
        compress_img_weight = image_size(newPath)
        print(f"Compressed weight: {compress_img_weight}")
    return compress_img_weight

# Loop to compress images
def loop_compress(newPath, weight, target_weight, reduction):
    quality = 90
    while weight > target_weight and quality >= 0:
        print(f"Function tryCompress initial weight {weight}")
        weight = CompressImg2d(weight, newPath, quality)
        quality -= reduction
        print(f"Weight {weight} quality: {quality}")
    
    return weight
