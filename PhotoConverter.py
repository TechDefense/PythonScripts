#requirements: pip install Pillow


import os
from PIL import Image

# Get current directory to search for photo files
directory = os.getcwd()

# Photo file formats Dictionary
supported_formats = {
    "1": "JPEG",
    "2": "PNG",
    "3": "BMP",
    "4": "GIF",
    "5": "TIFF",
    "6": "HEIC"
}

# Print the menu of supported photo file formats
print("Supported photo file formats:")
for num, format in supported_formats.items():
    print(f"{num}. {format}")

# Ask the user to select the photo file format to convert from
from_format = input("Enter the number or name of the photo file format to convert from: ").strip()

# Determine the file extension of the selected format
if from_format.isdigit() and from_format in supported_formats:
    from_format = supported_formats[from_format]
elif from_format not in supported_formats.values():
    print("Invalid photo file format selected.")
    exit()

# Ask the user to select the photo file format to convert to
to_format = input("Enter the number or name of the photo file format to convert to: ").strip()

# Choose the file extension to convert to
if to_format.isdigit() and to_format in supported_formats:
    to_format = supported_formats[to_format]
elif to_format not in supported_formats.values():
    print("Invalid photo file format selected.")
    exit()

# Loop through all directories and subdirectories to find photo files of the selected format
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(f".{from_format.lower()}") or (from_format == "JPEG" and file.endswith(".jpg")):
            # Create the path to the photo file
            photo_path = os.path.join(root, file)

            # Create the path to the output file
            output_path = os.path.splitext(photo_path)[0] + f".{to_format.lower()}"

            # Check if the output file already exists
            if os.path.exists(output_path):
                print(f"Skipping conversion for {photo_path}. Output file {output_path} already exists.")
                continue

            # Open the photo file and convert it to the selected format
            image = Image.open(photo_path)
            image.save(output_path, format=to_format)

            # Print the conversion result
            print(f"Converted {photo_path} to {output_path}")
