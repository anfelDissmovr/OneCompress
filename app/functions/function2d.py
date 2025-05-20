import os
from PIL import Image
from pathlib import Path


def image_size(file):
    size_bytes = os.path.getsize(file)
    return int(size_bytes / 1024)


def change_path(file):
    relative_path = file[0].replace('\\', '/')
    return Path('app/static') / relative_path


def change_file_name(original_path):
    file_name = os.path.basename(original_path).replace('\\', '/')
    compressed_dir = Path("app/static/upload/2d/compressed")
    compressed_dir.mkdir(parents=True, exist_ok=True)
    return str(compressed_dir / file_name)


def show_img(path):
    img = Image.open(path)
    img.show()


def resize_img(file_path,):
    with Image.open(file_path) as img:
        img.thumbnail((2200, 1238))
        if img.mode not in ('RGB', 'CMYK'):
            img = img.convert('RGB')
        newPath = change_file_name(file_path)
        img.save(newPath, format="JPEG", quality=100)
        return image_size(newPath), newPath


def CompressImg2d(get_original_weight, newPath, quality):
    with Image.open(newPath) as img:
        img.save(newPath, format="JPEG", quality=quality)
        return image_size(newPath)


def loop_compress(newPath, weight, target_weight, reduction):
    quality = 90
    while weight > target_weight and quality >= 0:
        weight = CompressImg2d(weight, newPath, quality)
        quality -= reduction
    return weight