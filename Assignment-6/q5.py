
class Image:
    
    def __init__(self, imageWidth=0, imageHeight=0, colorCode="None"):
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.colorCode = colorCode

    def set_imageWidth(self, width):
        self.imageWidth = width

    def set_imageHeight(self, height):
        self.imageHeight = height

    def set_colorCode(self, color):
        self.colorCode = color

    def get_imageWidth(self):
        return self.imageWidth

    def get_imageHeight(self):
        return self.imageHeight

    def get_colorCode(self):
        return self.colorCode

    def __str__(self):
        return (f"Image Width: {self.imageWidth}, "
                f"Image Height: {self.imageHeight}, "
                f"Color Code: {self.colorCode}")



image1 = Image()


image2 = Image(1920, 1080, "#FFFFFF")


print("Image 1 Details:")
print(image1)

print("\nImage 2 Details:")
print(image2)