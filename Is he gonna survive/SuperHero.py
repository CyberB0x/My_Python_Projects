# Is he gonna survive?

user_bullets = int(input("Введите кол-во стрел для сражение \n"))
user_dragons = int(input("Кол-во драконов на поле сражение \n"))

def hero(bullets, dragons):
    required_bullets = dragons * 2
    return bullets >= required_bullets

bullets = user_bullets
dragons = user_dragons

if hero(bullets, dragons):
    print(f"Ура Герой выжил кол-во стрел {bullets}, кол-во драконов {dragons}")
else:
    print(f"Жаль что Герой не выжил кол-во стрел {bullets}, кол-во драконов {dragons}.")