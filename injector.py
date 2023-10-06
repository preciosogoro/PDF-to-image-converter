# f = open("ordellarchive python/file.html", "a")
# f.write("Hello world")
# f.clo se()
templatesoal = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css soal/templatesoal.css">
</head>
<body> 
    <header>
        <div class="content">
            <div class="Logo">
                <a href="#">ordell</a>
            </div>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Akademis</a></li>
            </ul>
        </div>
    </header>
    
    <main id="container">
        <div class="placeholder">
            <div class="imagePlaceholder">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
                <img src="../resources/image/image soal/SOAL BTA PK & PM BAB 1/" alt="Soal BTA PK & PM bab 1">
            </div>
        </div>
    </main>
   
</body>
</html>'''

def inject(path, filename):
    f = open(path + filename, "a")
    print(f)
    f.write(templatesoal)
    f.close()
    
inject("ordellarchive python/HTML/", "test.html")

