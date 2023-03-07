import random

print("1 ile 100 arasında bir sayı tuttum. Tahmin edebilecek misin?")

scores = {}

while True:
    player_name = input("Lütfen adınızı girin: ")
    random_number = random.randint(1, 100)
    guesses = 0
    max_guesses = 10

    while guesses < max_guesses:
        guess = int(input("Tahmininizi girin: "))
        guesses += 1

        if guess < random_number:
            print("Daha büyük bir sayı girin.")
        elif guess > random_number:
            print("Daha küçük bir sayı girin.")
        else:
            print("Tebrikler! Doğru tahmin ettiniz!")
            print("Tahmin sayınız:", guesses)

            score = (max_guesses - guesses + 1) * 10

            if player_name in scores:
                if score > scores[player_name]:
                    scores[player_name] = score
            else:
                scores[player_name] = score

            break

    if guesses == max_guesses:
        print("Tahmin hakkınız bitti. Doğru sayı:", random_number)

    play_again = input("Tekrar oynamak ister misiniz? (E/H): ")
    if play_again.lower() == "h":
        break

print("\nSkor Tablosu:")
for player, score in scores.items():
    print(player, "-", score, "puan")
