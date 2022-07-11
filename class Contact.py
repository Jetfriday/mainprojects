class Contact:
    def __init__(phonebook, name, phone, address, birthday):
        phonebook.name = name
        phonebook.phone = phone
        phonebook.address = address
        phonebook.birthday = birthday

        print(f"Создан новый контакт {name}")
    
    def  show(phonebook):
        print(f"{phonebook.name} - адресс: {phonebook.address}, телефон: {phonebook.phone}, день рождения: {phonebook.birthday}")

    def __str__(phonebook):
        return "Контакт: " + phonebook.name + ", " + phonebook.phone

mike = Contact("Михаил Булгаков","2-03-27","Россия, Москва, Большая Пироговская, дом 35б, кв. 6","15.05.1891")
vlad = Contact("Владимир Маяковский","73-88","Россия, Москва, Лубянский проезд, д. 3, кв. 12","19.07.1893")

print(vlad)