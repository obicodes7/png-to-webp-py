from PIL import Image
import os


def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            if "pngtowebp.py" not in full_path:
                output_webp = full_path.replace('.png', '.webp')
                convert_png_to_webp(full_path, output_webp)
                os.remove(full_path)


def convert_png_to_webp(input_path, output_path):
    try:
        image = Image.open(input_path)
        image = image.convert('RGB')  # Convert to RGB if needed
        image.save(output_path, 'webp')
        print(f"Converted {input_path} to {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


directory_path = './'
list_files_recursive(directory_path)
