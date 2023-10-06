from pdf2image import convert_from_path


images = convert_from_path('example.pdf')
 
for i in range(len(images)):
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    imageContainer = []

for object in imageContainer:
    try:
        print(object)
        print(type(object))
    except:
        print("an Error has occured")

