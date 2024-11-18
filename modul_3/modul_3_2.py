def send_email(message, recipient, sender = 'university.help@mail.com'):
    if '@' not in recipient or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')) or recipient.endswith(('.com', '.ru', '.net')):
        print('Невозможно отправить письмо с адреса {} на адрес {}'.format(sender, recipient))
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    else:
        print('Письмо отправлено успешно: nОтправитель: {}nПолучатель: {}nСообщение: {}'.format(sender, recipient, message))

