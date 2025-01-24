import json


def fayllar(joy):
    try:
        with open(joy, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Fayl topilmad")
        return []
    except json.JSONDecodeError:
        print("JSONda xatolik")
        return []

# Erkelani sonini husoblemz:
def man(data):
    count = 0
    for person in data:
        if 'gender' in person:
            if person['gender'] == 'Male':
                count += 1
    return count

# Ayollar sonini hisoblemz
def woman(data):
    count = 0
    for person in data:
        if 'gender' in person:
            if person['gender'] == 'Female':
                count += 1
    return count

# Hindistonlilani chiqoramiza
def india(data):
    indian = []
    for person in data:
        if 'country' in person:
            if person['country'] == 'India':
                indian.append(person)
    return indian

# 20 yoshdan kicila
def kiciklar(data):
    kicik = []
    for person in data:
        if 'age' in person:
            if person['age'] < 20:
                kicik.append(person)
    return kicik

# Muhandislarri topamz
def engi(data):
    engineers = []
    for person in data:
        if 'job' in person:
            if person['job'] == 'Engineer':
                engineers.append(person)
    return engineers

joy = "people.json"
odamlar = fayllar(joy)

if odamlar:
    print(f"Erkelalar soni: {man(odamlar)}")
    print(f"Ayollar soni: {woman(odamlar)}")

    print("Hindistonliklar:")
    for user in india(odamlar):
        print(user)

    print("20 yoshdan kichikla:")
    for user in kiciklar(odamlar):
        print(user)

    print("Muhandisla:")
    for engineer in engi(odamlar):
        print(engineer)
