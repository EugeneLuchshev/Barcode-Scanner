import sys
barcode = ' '
print('отсканируй штрихкод')
while barcode: #создаем бесконечный цикл
    barcode = str(input()) #переменная, куда будут вводиться отсканированные штрихкоды
    print("отсканирован:", barcode)
    try:
        with open('text.txt', 'a') as file: # записываем отсканированные значения в тхт файл
            file.write('штрихкод:')
            file.write(barcode)
            file.write('\n') #отступ между 'штрихкод: ' и отсканированным значением
    except:
        print('штрихкод сохранен')


