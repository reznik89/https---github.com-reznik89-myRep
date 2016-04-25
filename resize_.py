from PIL import Image

def scale_and_resize():
    img = Image.open('hello.jpg')
    width, height = img.size

    img.resize((128,128)).save("128.png")

    img.resize((width//2, height//2)).save("half.jpg")

if __name__ == '__main__':
    scale_and_resize()
