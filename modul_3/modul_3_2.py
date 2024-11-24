def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка на корректность адресов электронной почты
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    # Проверка на валидность адресов
    if not is_valid_email(recipient) or not is_valid_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на совпадение адресов отправителя и получателя
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return

# Примеры использования функции
send_email("Привет!", "student@example.com")  # Письмо успешно отправлено с адреса university.help@gmail.com на адрес student@example.com.
send_email("Привет!", "invalid_email")        # Невозможно отправить письмо с адреса university.help@gmail.com на адрес invalid_email
send_email("Привет!", "student@example.com", "student@example.com")  # Нельзя отправить письмо самому себе!
send_email("Привет!", "student@example.com", "invalid_email")