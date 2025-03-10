#golovnui modul
from dataclasses import replace

from PyQt5.QtWidgets import QApplication
from time import sleep
app = QApplication([])
from main_window import *
import json
box = 0
en_word = 0
cur_word = 0
curent_user= {
              "uspishnist": [
                  0,
                  0,
                  0]}
class User:
    def __init__(self,nickname,password,uspishnist,posada="user"):
        self.posada=posada
        self.nickname=nickname
        self.password=password
        self.uspishnist=uspishnist
        spusok_users.append(self)

    def to_dict(self):  # Метод для преобразования в словарь
        return self.__dict__


def change():
    global box, cur_word, en_word,ans_time,right_ans
    if box == 1:
        box = 2
        radio_gb.show()
        ans_gb.hide()
        shuffle(english_words_list)
        en_word = choice(english_words_list)
        lb_question.setText(en_word)
        n = randint(1, 4)
        if n == 1:
            rbtn1.setText(english_ukrainian_dict[en_word])
            rbtn2.setText(choice(ukr_words_list))
            rbtn3.setText(choice(ukr_words_list))
            rbtn4.setText(choice(ukr_words_list))
        if n == 2:
            rbtn1.setText(choice(ukr_words_list))
            rbtn2.setText(english_ukrainian_dict[en_word])
            rbtn3.setText(choice(ukr_words_list))
            rbtn4.setText(choice(ukr_words_list))
        if n == 3:
            rbtn1.setText(choice(ukr_words_list))
            rbtn2.setText(choice(ukr_words_list))
            rbtn3.setText(english_ukrainian_dict[en_word])
            rbtn4.setText(choice(ukr_words_list))
        if n == 4:
            rbtn1.setText(choice(ukr_words_list))
            rbtn2.setText(choice(ukr_words_list))
            rbtn3.setText(choice(ukr_words_list))
            rbtn4.setText(english_ukrainian_dict[en_word])
        radio_group.setExclusive(False)
        rbtn1.setChecked(False)
        rbtn2.setChecked(False)
        rbtn3.setChecked(False)
        rbtn4.setChecked(False)
        radio_group.setExclusive(True)
        btn_ok.setText("Відповісти")
    elif box==2:
        global curent_user
        curent_user["uspishnist"][0]+=1
        if rbtn1.isChecked():
            cur_word = rbtn1.text()
        elif rbtn2.isChecked():
            cur_word = rbtn2.text()
        elif rbtn3.isChecked():
            cur_word = rbtn3.text()
        elif rbtn4.isChecked():
            cur_word = rbtn4.text()
        else:
            cur_word = ""
        box = 1
        ans_gb.show()
        radio_gb.hide()
        if cur_word == english_ukrainian_dict[en_word]:
            lb_result.setText("Правильно")
            curent_user["uspishnist"][1]+=1
        else:
            lb_result.setText("Неправильно")
        lb_correct.setText(english_ukrainian_dict[en_word])
        btn_ok.setText("Наступне запитання")
    elif box==0:
        for user in spusok_users:
            if line_e_password.text()==user["password"] and line_e_nickname.text()==user["nickname"]:
                globals()["curent_user"]=user
                box=1
                line_e_gb.hide()
                lb_question.setText("nagmu shchob rozpochatu")
                btn_ok.setText("Pochatu")
                statustuka_posada.setText(curent_user["posada"])
                if curent_user["posada"]== "admin":
                    znaitu_st_le.show()
                    znaitu_st_btn.show()
                    pominatu_pos_user_btn.show()
                    pominatu_pos_admin_btn.show()

                break
        if box==0:
            lb_question.setText("User ne znaidenui")








def wait():
    window_card.hide()
    sleep(box_min.value() * 60)
    window_card.show()


def show_menu():
    global curent_user
    statustuka_l.setText("Статистика")
    try:
        if curent_user["uspishnist"][0] == 0 and curent_user["uspishnist"][0] == 0:
            raz_vidpovilu_l.setText(f"Разів відповіли:0")
            virnux_vidpovidei_l.setText(f"Вірних відповідей:0")
            uspishnist_l.setText(f"Успішність:0%")
        else:
            raz_vidpovilu_l.setText(f"Разів відповіли:{curent_user["uspishnist"][0]}")
            virnux_vidpovidei_l.setText(f"Вірних відповідей:{curent_user["uspishnist"][1]}")
            uspishnist_l.setText(f"Успішність:{curent_user["uspishnist"][1] / curent_user["uspishnist"][0] * 100}%")
    except:
        raz_vidpovilu_l.setText(f"Разів відповіли:0")
        virnux_vidpovidei_l.setText(f"Вірних відповідей:0")
        uspishnist_l.setText(f"Успішність:0%")
    menu_w.show()
    window_card.hide()
def nazad():
    menu_w.hide()
    window_card.show()
def gest():
    globals()["box"]=1
    btn_gest.hide()
    line_e_gb.hide()
    lb_question.setText("regum gosta bkluchenui")
    btn_ok.setText("Pochatu")
    statustuka_posada.setText("Gist")
def make_akk():
    if  line_e_password_r.isHidden():
        line_e_password_r.show()
        lb_question.setText("napushi dani i nagmu sotdat akk")
        dodatu_akk_btn.setText("Sozdatu akk")
        globals()["box"] = -1
    elif not line_e_password_r.isHidden():
        a=0
        globals()["box"]=-1
        for user in spusok_users:
            if user["nickname"]==line_e_nickname.text():
                lb_question.setText("nickname uge zanyatui")
                break
            else:
                a+=1
        if line_e_password.text()==line_e_password_r.text() and a==len(spusok_users):
            user1={              "posada":"user",
                                 "nickname":line_e_nickname.text(),
                                 "password":line_e_password.text(),
                                 "uspishnist":[0,0,0]}
            spusok_users.append(user1)

            btn_gest.hide()
            line_e_gb.hide()
            lb_question.setText("nagmu schob rozpochatu")
            statustuka_posada.setText("user")
            globals()["box"]=1
            globals()["curent_user"] = user1
def make_user():
    a=0
    global spusok_users,curent_user
    for user in spusok_users:
        a+=1
        if znaitu_st_le.text()==user["nickname"] and not curent_user["nickname"]==znaitu_st_le.text():
            user["posada"]="user"
            statustuka_l.setText("nemogna minatu svou posady")
    if a == len(spusok_users): statustuka_l.setText("nemogna minatu svou posady")
def make_admin():
    a=0
    global spusok_users,curent_user
    for user in spusok_users:
        a+=1
        if znaitu_st_le.text()==user["nickname"]and  not curent_user["nickname"]==znaitu_st_le.text():
            user["posada"]= "admin"
            break
    if a==len(spusok_users):statustuka_l.setText("nemogna minatu svou posady")

btn_ok.clicked.connect(change)
btn_menu.clicked.connect(show_menu)
btn_sleep.clicked.connect(wait)
nazad_btn.clicked.connect(nazad)
btn_gest.clicked.connect(gest)
dodatu_akk_btn.clicked.connect(make_akk)
pominatu_pos_user_btn.clicked.connect(make_user)
pominatu_pos_admin_btn.clicked.connect(make_admin)
app.exec_()
with open("data.json", "w", encoding="utf-8") as file:
    json.dump((english_ukrainian_dict,english_words_list,ukr_words_list,ans_time,right_ans), file, ensure_ascii=False, indent=4)
for user in spusok_users:
    try:
        spusok_users[spusok_users.index(user)]=user.__dict__
    except:
        None
with open("Users.json", "w", encoding="utf-8") as file:
    json.dump(spusok_users, file, ensure_ascii=False, indent=4)