import cv2
import entity.caption as caption;
from datetime import datetime

classificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface_extended.xml")
imagem = cv2.imread(r"images/gato_rebaixado.png")
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = classificador.detectMultiScale(cinza, scaleFactor=1.50, minSize =(30,30))

#reconhecedor = cv2.face.EigenFaceRecognizer_create()
#reconhecedor.read('classificadorEigen.yml')


path = "/Users/evertosilva/Desktop/pythonProject/ps_ia/"
today = datetime.now()
date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
time = str(today.hour) + ':' + str(today.minute) + ':' + str(today.second)

caption = caption.Caption(path, date, time, "Jardim")

if len(faces) > 0:
    print("Gato detectado no jardim.")

    amostra = 1
    numeroMaxAmostras = 5
    largura, altura = 220, 220
    for (x, y, l, a) in faces:
        cv2.imshow("Gatos detectados", imagem)
        cv2.rectangle(imagem, (x, y), (x+largura, y+altura), (0, 0, 225), 2)
        if cv2.waitKey(1):
            imagemGato = cv2.resize(cinza[y: y+altura, x: x+largura], (largura, altura))
            localFoto = "fotos/"+str(amostra)+".jpg"

            cv2.imwrite(localFoto, imagemGato)
            amostra+=1
        if amostra > numeroMaxAmostras:
            break
            print("Fotos capturadas com sucesso!")
            cv2.destroyAllWindows()
#else:
    #print("Não detectamos nenhum gato.")