def send_email(message, recipient, sender='university.help@gmail.com'):
    sobaka = '@'
    konec = ('.com', '.net', '.ru')
    flag = False
    if sobaka in recipient:
        for i in konec:
            if i in recipient:
                flag = True
    sobaka2 = '@'
    konec2 = ('.com', '.net', '.ru')
    flag2 = False
    if sobaka2 in sender:
        for i in konec2:
            if i in sender:
                flag2 = True
    if flag is False or flag2 is False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
