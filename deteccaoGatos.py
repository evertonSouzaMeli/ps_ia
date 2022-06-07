import cv2
import entity.caption as caption
import utils.csvUtils as csvUtils
from datetime import datetime

classificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")

imagesList = [r"images/gato_1.png", r"images/gato_2.jpeg", r"images/gato_3.jpeg", r"images/gato_4.png"]

today = datetime.now()
date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
time = str(today.hour) + ':' + str(today.minute) + ':' + str(today.second)
caption = caption.Caption("", date, time, "Jardim")
amostra = 0
i = 0

while i < len(imagesList) or amostra > 5:
    imagem = cv2.imread(imagesList[i])
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    faces = classificador.detectMultiScale(cinza, scaleFactor=1.1)
    if len(faces) > 0:
        print("Gato detectado no jardim.")
        numeroMaxAmostras = 5
        largura, altura = 220, 220

        for (x, y, l, a) in faces:
            imagem = cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 0, 225), 2)
            cv2.imshow("Gatos detectados", imagem)

            if cv2.waitKey(2000):
                amostra += 1
                localPhoto = "./data/gato_" + str(amostra) + ".jpg"
                caption.path = localPhoto
                cv2.imwrite(localPhoto, imagem)
                csvUtils.includeRows(caption)
            if amostra > numeroMaxAmostras:
                print("Fotos capturadas com sucesso!")
                cv2.destroyAllWindows()
                break
    else:
        print("Não detectamos nenhum gato.")
    i += 1
