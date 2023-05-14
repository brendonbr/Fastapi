import cv2
import pytesseract
import re


def escrever_texto():
    # Carregar imagem em preto e branco
    img = cv2.imread('opencv/imagem.png', cv2.IMREAD_GRAYSCALE)

    # Aplicar limiarização para binarizar a imagem
    _, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Aplicar detecção de contornos
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterar sobre os contornos e extrair o texto
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cropped_img = img[y:y+h, x:x+w]
        text = pytesseract.image_to_string(cropped_img, lang='por')

    palavras=text.split()
    alternativas=['(A)','(B)','(C)','(D)','(E)']
    alt_correta='\item'
    for i in range(len(palavras)):
        if palavras[i] in alternativas:
            palavras[i] = alt_correta
            novo_text=' '.join(palavras)      
    print(novo_text)


escrever_texto()



