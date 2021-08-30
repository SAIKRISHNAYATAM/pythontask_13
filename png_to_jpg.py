from PIL import Image

img = Image.open("C:\\Users\\sy21249\\PycharmProjects\\sai\\panda.png")
jpg = img.convert('RGB')
jpg.save('C:\\Users\\sy21249\\PycharmProjects\\sai\\panda1.jpg')