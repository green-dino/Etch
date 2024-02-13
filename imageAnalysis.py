from PIL import Image
from prettytable import PrettyTable
from PIL.ExifTags import TAGS

class ImageProcessor:
    @staticmethod
    def process_image(image_path):
        try:
            with Image.open(image_path) as pil_image:
                exif_data = pil_image._getexif()
                image_time_stamp, camera_make, camera_model = "NA", "NA", "NA"
                
                if exif_data:
                    for tag, value in exif_data.items():
                        tag_name = TAGS.get(tag, tag)
                        if tag_name == 'DateTimeOriginal':
                            image_time_stamp = value.strip()
                        elif tag_name == "Make":
                            camera_make = value.strip()
                        elif tag_name == 'Model':
                            camera_model = value.strip()
                
                im_format = pil_image.format
                im_type = pil_image.mode
                im_width = pil_image.width
                im_height = pil_image.height
                
                return im_format, im_type, im_width, im_height, image_time_stamp, camera_make, camera_model
        except Exception as err:
            print("Exception: ", str(err))
            return None, None, None, None, None, None, None

class ImageSearcher:
    def __init__(self, directory):
        self.directory = directory

    def is_image(self, file_path):
        try:
            Image.open(file_path)
            return True
        except:
            return False

    def get_file_size(self, file_path):
        size_bytes = os.path.getsize(file_path)
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.2f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.2f} MB"

    def search_images(self):
        if not os.path.exists(self.directory):
            print("Error: Directory does not exist.")
            return

        if not os.path.isdir(self.directory):
            print("Error: Path provided is not a directory.")
            return

        table = PrettyTable(["Image?", "File", "FileSize", "Ext", "Format", "Width", "Height", "Type", "Timestamp", "Make", "Model"])

        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if self.is_image(file_path):
                img_format, img_type, img_width, img_height, image_time_stamp, camera_make, camera_model = ImageProcessor.process_image(file_path)
                if img_format:
                    file_size = self.get_file_size(file_path)
                    ext = os.path.splitext(filename)[1]
                    table.add_row(["Yes", filename, file_size, ext, img_format, img_width, img_height, img_type, image_time_stamp, camera_make, camera_model])

        if table._rows:
            print("Images found in directory:")
            print(table)
        else:
            print("No images found in directory.")

def main():
    directory = input("Enter directory path to search: ")
    searcher = ImageSearcher(directory)
    searcher.search_images()

if __name__ == "__main__":
    main()