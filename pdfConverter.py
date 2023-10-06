from pdf2image import convert_from_path


images = convert_from_path('resource/BAB 1 PK & PM- PERSIAPAN.pdf')
 
for i in range(len(images)):
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    imageContainer = []