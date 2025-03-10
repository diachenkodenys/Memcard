#golovne vikno
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, \
    QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, \
    QSpinBox, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from random import shuffle,choice,randint
from time import time
import json
window_card=QWidget()
window_card.resize(600,500)
window_card.setWindowTitle("Memory Card")

with open("data.json","r", encoding="utf-8") as file:
   english_ukrainian_dict,english_words_list,ukr_words_list,ans_time,right_ans=json.load(file)
with open("Users.json","r", encoding="utf-8") as file:
    spusok_users=json.load(file)

# створюємо віджети
btn_menu = QPushButton('Меню')
btn_sleep = QPushButton('Відпочити')
btn_ok = QPushButton('vviitu')
box_min = QSpinBox() # к-сть хв для відпочинку
box_min.setValue(5)
lb_question = QLabel('vviidu v akaunt') # текст для запитання
lb_question.setStyleSheet("font-size: 50px;")

# панель із запитаннями
radio_gb = QGroupBox('Варіанти відповіді')
radio_group = QButtonGroup()
radio_gb.hide()
rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')
rbtn1.setStyleSheet("font-size: 50px;")
rbtn2.setStyleSheet("font-size: 50px;")
rbtn3.setStyleSheet("font-size: 50px;")
rbtn4.setStyleSheet("font-size: 50px;")

radio_group.addButton(rbtn1)
radio_group.addButton(rbtn2)
radio_group.addButton(rbtn3)
radio_group.addButton(rbtn4)

# панель із результатом
ans_gb = QGroupBox('Результат тесту')
lb_result = QLabel('') # надпис правильно чи неправ.
lb_correct = QLabel('') # правильний вар. з відповіддю
lb_result.setStyleSheet("font-size: 50px;")
lb_correct.setStyleSheet("font-size: 50px;")

line_e_gb=QGroupBox()
line_e_nickname=QLineEdit()
line_e_password=QLineEdit()
line_e_password_r=QLineEdit()
line_e_password_r.hide()
line_e_nickname.setPlaceholderText("Nickname")
line_e_password.setPlaceholderText("Password")
line_e_password_r.setPlaceholderText("Repeat your password")
dodatu_akk_btn=QPushButton("Sche nema akkaunta?Sozdayte novui")
line_v_gb_line_e=QVBoxLayout()
line_v_gb_line_e.addWidget(line_e_nickname)
#line_v_gb_line_e.addSpacing(-60)
line_v_gb_line_e.addWidget(line_e_password)
line_v_gb_line_e.addWidget(line_e_password_r)
#line_v_gb_line_e.addSpacing(-80)
line_v_gb_line_e.addWidget(dodatu_akk_btn)
line_v_gb_line_e.addSpacing(80)
line_e_gb.setLayout(line_v_gb_line_e)

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
radio_gb.setLayout(layout_ans1)

# розташовуємо результат
layout_result = QVBoxLayout()
layout_result.addWidget(lb_result,alignment=(Qt.AlignTop | Qt.AlignLeft))
layout_result.addWidget(lb_correct,alignment=Qt.AlignCenter, stretch=2)
ans_gb.setLayout(layout_result)
ans_gb.hide()

# створюємо та добавляємо всі інші віджети
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line25=QHBoxLayout
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_min)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_question,alignment=Qt.AlignCenter)
layout_line3.addWidget(radio_gb)
layout_line3.addWidget(ans_gb)
layout_line3.addWidget(line_e_gb)

btn_gest=QPushButton("vvitu yak gist")

layout_line4.addStretch(1)
layout_line4.addWidget(btn_ok,stretch=1)
layout_line4.addWidget(btn_gest,stretch=1)
layout_line4.addStretch(1)




layout_main=QVBoxLayout()
layout_main.addLayout(layout_line1)
layout_main.addLayout(layout_line2,stretch=1)
layout_main.addLayout(layout_line3,stretch=5)
layout_main.addLayout(layout_line4)


line_e_gb.show()
window_card.setLayout(layout_main)



def dodatu_z():
    english_ukrainian_dict[zaputana_le.text()]=virna_vidpovid_le.text()
    ukr_words_list.append(persha_hubna_vidpovid_le.text())
    ukr_words_list.append(druga_hubna_vidpovid_le.text())
    ukr_words_list.append(treta_hubna_vidpovid_le.text())
    english_words_list.append(virna_vidpovid_le.text())
def ochustutu():
    zaputana_le.clear()
    virna_vidpovid_le.clear()
    persha_hubna_vidpovid_le.clear()
    druga_hubna_vidpovid_le.clear()
    treta_hubna_vidpovid_le.clear()
def menu_admin():
    a=0
    global spusok_users
    t=znaitu_st_le.text()
    for user in spusok_users:
        a+=1
        if user["nickname"] == t:
            a-=1
            if user["uspishnist"][0] == 0 and user["uspishnist"][0] == 0:
                raz_vidpovilu_l.setText(f"Разів відповіли:0")
                virnux_vidpovidei_l.setText(f"Вірних відповідей:0")
                uspishnist_l.setText(f"Успішність:0%")
            else:
                raz_vidpovilu_l.setText(f"Разів відповіли:{user["uspishnist"][0]}")
                virnux_vidpovidei_l.setText(f"Вірних відповідей:{user["uspishnist"][1]}")
                uspishnist_l.setText(f"Успішність:{user["uspishnist"][1] / user["uspishnist"][0] * 100}%")
    statustuka_l.setText("Статистика")
    if a==len(spusok_users): statustuka_l.setText("koristyvacha ne znaydeno")

menu_w=QWidget()
menu_w.setWindowTitle("Menu")
menu_w.resize(400,300)
zaputana_l=QLabel("Введіть запитання:")
virna_vidpovid_l=QLabel("Вірна відповідь:")
persha_hubna_vidpovid_l=QLabel("Перша хибна відповідь:")
druga_hubna_vidpovid_l=QLabel("Друга хибна відповідь:")
treta_hubna_vidpovid_l=QLabel("Третя хибна відповідь:")
zaputana_le=QLineEdit()
virna_vidpovid_le=QLineEdit()
persha_hubna_vidpovid_le=QLineEdit()
druga_hubna_vidpovid_le=QLineEdit()
treta_hubna_vidpovid_le=QLineEdit()
dodatu_zaputana_btn=QPushButton("Додати запитання")
ochustutu_btn=QPushButton("Очистити")
statustuka_l=QLabel("Статистика")
statustuka_posada=QLabel("Ne vviishow")
statustuka_l.setStyleSheet("font-size: 30px;")
raz_vidpovilu_l=QLabel("Разів відповіли:0%")
virnux_vidpovidei_l=QLabel("Вірних відповідей:0%")
uspishnist_l=QLabel("Успішність:0%")
nazad_btn=QPushButton("Назад")
layout_h1=QHBoxLayout()
layout_h2=QHBoxLayout()
layout_h3=QHBoxLayout()
layout_h4=QHBoxLayout()
layout_h5=QHBoxLayout()
layout_h6=QHBoxLayout()
layout_h7=QHBoxLayout()
layout_h8=QHBoxLayout()
layout_h9=QHBoxLayout()
layout_h10=QHBoxLayout()
layout_h11=QHBoxLayout()

layout_h1.addWidget(zaputana_l,alignment=Qt.AlignLeft)
layout_h1.addWidget(zaputana_le,alignment=Qt.AlignRight)

layout_h2.addWidget(virna_vidpovid_l,alignment=Qt.AlignLeft)
layout_h2.addWidget(virna_vidpovid_le,alignment=Qt.AlignRight)

layout_h3.addWidget(persha_hubna_vidpovid_l,alignment=Qt.AlignLeft)
layout_h3.addWidget(persha_hubna_vidpovid_le,alignment=Qt.AlignRight)

layout_h4.addWidget(druga_hubna_vidpovid_l,alignment=Qt.AlignLeft)
layout_h4.addWidget(druga_hubna_vidpovid_le,alignment=Qt.AlignRight)

layout_h5.addWidget(treta_hubna_vidpovid_l,alignment=Qt.AlignLeft)
layout_h5.addWidget(treta_hubna_vidpovid_le,alignment=Qt.AlignRight)

layout_h6.addWidget(dodatu_zaputana_btn,stretch=1)
layout_h6.addWidget(ochustutu_btn,stretch=1)

znaitu_st_le=QLineEdit()
znaitu_st_le.setPlaceholderText("Nickname")
znaitu_st_btn=QPushButton("znaitu")
pominatu_pos_user_btn=QPushButton("zrobutu userom")
pominatu_pos_admin_btn=QPushButton("zrobutu adminom")
layout_h7.addWidget(statustuka_l,alignment=Qt.AlignLeft)
layout_h7.addWidget(statustuka_posada)
layout_h7.addWidget(znaitu_st_le)
layout_h7.addWidget(znaitu_st_btn)
znaitu_st_btn.hide()
znaitu_st_le.hide()

layout_h8.addWidget(raz_vidpovilu_l,alignment=Qt.AlignLeft)
layout_h8.addWidget(pominatu_pos_user_btn,alignment=Qt.AlignRight)


layout_h9.addWidget(virnux_vidpovidei_l,alignment=Qt.AlignLeft)
layout_h9.addWidget(pominatu_pos_admin_btn,alignment=Qt.AlignRight)

pominatu_pos_user_btn.hide()
pominatu_pos_admin_btn.hide()

layout_h10.addWidget(uspishnist_l,alignment=Qt.AlignLeft)

layout_h11.addWidget(nazad_btn,stretch=1)

main_v_line=QVBoxLayout()
main_v_line.addLayout(layout_h1)
main_v_line.addLayout(layout_h2)
main_v_line.addLayout(layout_h3)
main_v_line.addLayout(layout_h4)
main_v_line.addLayout(layout_h5)
main_v_line.addLayout(layout_h6)
main_v_line.addSpacing(20)
main_v_line.addLayout(layout_h7)
main_v_line.addSpacing(-10)
main_v_line.addLayout(layout_h8)
main_v_line.addSpacing(-10)
main_v_line.addLayout(layout_h9)
main_v_line.addSpacing(-8)
main_v_line.addLayout(layout_h10)
main_v_line.addLayout(layout_h11)

menu_w.setLayout(main_v_line)
dodatu_zaputana_btn.clicked.connect(dodatu_z)
ochustutu_btn.clicked.connect(ochustutu)
znaitu_st_btn.clicked.connect(menu_admin)

window_card.show()
