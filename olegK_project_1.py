import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QBasicTimer


class variant:  # создания варианта с примерами
    def __init__(self, count, vib, addi, sub,
                 mul, div, number, colvo,
                 signal, namef, per):
        self.count = count
        self.vib = vib
        self.addi = addi
        self.sub = sub
        self.mul = mul
        self.div = div
        self.number = number
        self.colvo = colvo
        self.signal = signal
        self.namef = namef
        self.pere = per

    def make(self):
        if self.vib is False:  # проверка на кол-во файлов
            file = open(self.namef, 'w')
            a = 1
        else:
            a = 0
        for i in range(self.count):
            if a == 0 and i == 0:
                self.namef = (self.namef[:-4:] + '_{}' +
                              self.namef[-4::]).format(i + 1)
                file = open(self.namef, 'w')
            elif a == 0:
                self.namef = (self.namef[:-6:] + '_{}' +
                              self.namef[-4::]).format(i + 1)
                file = open(self.namef, 'w')
            file.write('\n')
            file.write('Вариант {}'.format(i + 1))
            file.write('\n')
            file.write('\n')
            for j in range(self.colvo):
                sign = random.choice(self.signal)
                if self.addi is True and sign == 1:  # примеры с +
                    while 0 == 0:
                        fir = random.randrange(1, self.number)
                        sec = random.randrange(1, self.number)
                        thir = random.randrange(1, self.number)
                        four = random.randrange(1, self.number)
                        if self.pere == 2:  # выставление нужного кол-ва пременных
                            summ = fir + sec
                        if self.pere == 3:
                            summ = fir + sec + thir
                        if self.pere == 4:
                            summ = fir + sec + thir + four
                        if summ <= self.number:
                            break
                    if self.pere == 2:
                        file.write('{0}) {1} + {2} =  \n'.format(j + 1,
                                                                 fir, sec, summ))
                    elif self.pere == 3:
                        file.write('{0}) {1} + {2} + {3} =  \n'.format(j + 1,
                                                                       fir, sec,
                                                                       thir, summ))
                    elif self.pere == 4:
                        file.write('{0}) {1} + {2} + {3} + {4} =  \n'.format(j + 1,
                                                                             fir, sec, thir,
                                                                             four, summ))
                if self.sub is True and sign == 2:  # примеры с -
                    while 0 == 0:
                        fir = random.randrange(1, self.number)
                        sec = random.randrange(1, self.number)
                        thir = random.randrange(1, self.number)
                        four = random.randrange(1, self.number)
                        if self.pere == 2:
                            summ = fir - sec
                        if self.pere == 3:
                            summ = fir - sec - thir
                        if self.pere == 4:
                            summ = fir - sec - thir - four
                        if summ >= 0:
                            break
                    if self.pere == 2:
                        file.write('{0}) {1} - {2} =  \n'.format(j + 1,
                                                                 fir, sec, summ))
                    elif self.pere == 3:
                        file.write('{0}) {1} - {2} - {3} =  \n'.format(j + 1,
                                                                       fir, sec,
                                                                       thir, summ))
                    elif self.pere == 4:
                        file.write('{0}) {1} - {2} - {3} - {4} =  \n'.format(j + 1,
                                                                             fir, sec, thir,
                                                                             four, summ))
                if self.mul is True and sign == 3:  # примеры с *
                    while 0 == 0:
                        fir = random.randrange(1, self.number)
                        sec = random.randrange(1, self.number)
                        thir = random.randrange(1, self.number)
                        four = random.randrange(1, self.number)
                        if self.pere == 2:
                            summ = fir * sec
                        if self.pere == 3:
                            summ = fir * sec * thir
                        if self.pere == 4:
                            summ = fir * sec * thir * four
                        if summ <= self.number:
                            break
                    if self.pere == 2:
                        file.write('{0}) {1} * {2} =  \n'.format(j + 1,
                                                                 fir, sec, summ))
                    elif self.pere == 3:
                        file.write('{0}) {1} * {2} * {3} =  \n'.format(j + 1,
                                                                       fir, sec,
                                                                       thir, summ))
                    elif self.pere == 4:
                        file.write('{0}) {1} * {2} * {3} * {4} =  \n'.format(j + 1,
                                                                             fir, sec, thir,
                                                                             four, summ))
                if self.div is True and sign == 4:  # примеры с /
                    while 0 == 0:
                        fir = random.randrange(1, self.number)
                        sec = random.randrange(1, self.number)
                        summ = fir % sec
                        if summ == 0:
                            break
                    file.write('{0}) {1} / {2} =  \n'.format(j + 1, fir, sec, summ))
            if a == 0:
                file.close()
        file.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()  # определение кнопок и их действий
        uic.loadUi('projectdis.ui', self)
        self.display_1.setText('Кол-во заданий')
        self.slider_display_1.valueChanged[int].connect(self.col_vo)
        self.display_2.setText('Максимальное значение')
        self.slider_display_2.valueChanged[int].connect(self.max_zn)
        self.display_3.setText('Кол-во вариантов')
        self.slider_display_3.valueChanged[int].connect(self.variant)
        self.addition1.clicked.connect(self.addition)
        self.subtraction1.clicked.connect(self.subtraction)
        self.multiplication1.clicked.connect(self.multiplication)
        self.division1.clicked.connect(self.division)
        self.start.clicked.connect(self.run)
        self.start.clicked.connect(self.doaction)
        self.timer = QBasicTimer()
        self.step = 0
        self.actionNew.triggered.connect(self.new_wi)
        self.change_files.buttonClicked.connect(self.files)
        self.change_number.buttonClicked.connect(self.per_coun)
        self.number = 0
        self.colvo = 0
        self.var = 1
        self.variant1 = False
        self.sign1 = []
        self.addi = False
        self.sub = False
        self.mul = False
        self.div = False
        self.flag = 0
        self.per = 2

    def new_wi(self):  # функция перезапуска прграммы
        if self.flag != 0:
            self.display_1.setText('Кол-во заданий')
            self.display_2.setText('Максимальное значение')
            self.display_3.setText('Кол-во вариантов')
            self.start.setText('Сформировать файл')
            self.slider_display_1.setSliderPosition(0)
            self.slider_display_2.setSliderPosition(0)
            self.slider_display_3.setSliderPosition(0)
            self.FileName.setText('')
            self.addition1.setChecked(False)
            self.subtraction1.setChecked(False)
            self.multiplication1.setChecked(False)
            self.division1.setChecked(False)
            self.number = 0
            self.colvo = 0
            self.step = 0
            self.pbar.setValue(0)
            self.var = 1
            self.variant1 = False
            self.sign1 = []
            self.addi = False
            self.sub = False
            self.mul = False
            self.div = False
            self.per = 2
        else:
            pass

    def addition(self):  # определение знака в примере +
        if self.addi is True:
            self.addi = False
            self.sign1.remove(1)
        elif self.addi is False:
            self.addi = True
            self.sign1.append(1)

    def timerEvent(self, e):  # таймер

        if self.step >= 100:
            self.timer.stop()
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doaction(self):  # действие загрузочной полосы

        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(6, self)

    def subtraction(self):  # определение знака в примере -
        if self.sub is True:
            self.sub = False
            self.sign1.remove(2)
        elif self.sub is False:
            self.sub = True
            self.sign1.append(2)

    def multiplication(self):  # определение знака в примере *
        if self.mul is True:
            self.mul = False
            self.sign1.remove(3)
        elif self.mul is False:
            self.mul = True
            self.sign1.append(3)

    def division(self):  # определение знака в примере /
        if self.div is True:
            self.div = False
            self.sign1.remove(4)
        elif self.div is False:
            self.div = True
            self.sign1.append(4)

    def col_vo(self, value):  # определение кол-во примеров
        self.colvo = value
        self.display_1.setText(str(value))

    def max_zn(self, value):  # определение максимального значения
        self.number = value
        self.display_2.setText(str(value))

    def variant(self, value):  # определение кол-во вариантов
        self.var = value
        self.display_3.setText(str(value))

    def files(self):  # определение кол-ва файлов для записи
        if self.change_files.checkedButton().text() != 'Один':
            self.variant1 = True
        else:
            self.variant1 = False

    def per_coun(self):  # определение кол-ва переменных дщля примера
        if self.change_number.checkedButton().text() == '2':
            self.per = 2
        elif self.change_number.checkedButton().text() == '3':
            self.per = 3
        elif self.change_number.checkedButton().text() == '4':
            self.per = 4

    def run(self):  # запуск программы
        self.flag += 1
        name = self.FileName.text()
        if name == '':  # создание/открытие файла
            namef = "task.txt"
        else:
            namef = self.FileName.text() + '.txt'
        variant2 = variant(self.var, self.variant1, self.addi,
                           self.sub, self.mul, self.div,
                           self.number, self.colvo,
                           self.sign1, namef, self.per)
        variant2.make()
        self.start.setText('Готово')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
