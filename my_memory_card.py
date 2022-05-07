#создай приложение для запоминания информации]
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
q = Question("Государственный язык Бразилии?", "Португальский", "Английский", "Итальянский", 'Украинский')
questions_list.append(q)
q1 = Question('В какой европейской стране находится Биг-Бен?', 'Англия', 'Австрия', 'Германия', 'Дания')
questions_list.append(q1)
q2 = Question('Государственный язык Индии?', 'Хинди', 'Английский', 'Испанский', 'Немецкий')
questions_list.append(q2)
q3 = Question('Как называется место, где река впадает в другую реку, море или озеро?', 'устье', 'исток', 'русло', 'половодье')

def show_question():
    ansGroupBox.hide()
    RadioGroupBox.show()
    answer.setText('Ответить')

    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    answer.setText('Следующий вопрос')
    ansGroupBox.show()
    RadioGroupBox.hide()

def start_test():
    if answer.text() == 'Ответить':
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    ans_2.setText(q.right_answer)
    show_question()

def show_correct(res):
    ans_1.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика', "\n Всего вопросов " + str(main_win.total), "\n Правильных ответов " + str(main_win.score))
        print('Рейтинг:' , main_win.score/main_win.total*100 , '%')
    else:
        show_correct('Неправильно')
        show_correct('Неверно')
        print('Рейтинг:' , main_win.score/main_win.total*100 , '%')
        

def next_question():
    cur_question = randint(0, len(questions_list)-1)

    main_win.total += 1
    print('Статистика', "\n Всего вопросов " + str(main_win.total), "\n Правильных ответов " + str(main_win.score))
    q = questions_list[cur_question]
    ask(q)
    

def click_OK():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()
      
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,300)

question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

ansGroupBox = QGroupBox('Результат теста')
ans_1 = QLabel('Правильно/Неправильно')
ans_2 = QLabel('Правильный ответ')
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(ans_1)
layout_ans4.addWidget(ans_2)
ansGroupBox.setLayout(layout_ans4)

v_line = QVBoxLayout()
RadioGroupBox.setLayout(v_line)
answer = QPushButton('Ответить')

vl = QVBoxLayout()
vl.addWidget(question)
vl.addWidget(RadioGroupBox)
vl.addWidget(ansGroupBox)
ansGroupBox.hide()
vl.addWidget(answer)
main_win.setLayout(vl)

main_win.score = 0
main_win.total = 0
answer.clicked.connect(click_OK)
next_question()

main_win.show()
app.exec_()