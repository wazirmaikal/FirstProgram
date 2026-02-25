import random
import time
from datetime import date
HISTORY_FILE = "match_history.txt"

PLAYER_ATTACKS = {
    "1": {"name": "Archer Attack", "damage": 15, "accuracy": 0.8},
    "2": {"name": "Giant Smash", "damage": 25, "accuracy": 0.6},
    "3": {"name": "Wizard Spell", "damage": 20, "accuracy": 0.7},
} 

ENEMY_ATTACKS = [
    {"name": "Enemy Archer", "damage": 10, "accuracy": 0.8},
    {"name": "Enemy Giant", "damage": 20, "accuracy": 0.6},
    {"name": "Enemy Wizard", "damage": 15, "accuracy": 0.7},
]

3
def saveMatchHistory(player1, player2, result):
    while(True):
        try:
            with open(HISTORY_FILE, "a") as f:
                f.write(f"{player1} vs {player2} Winner: {result} play on {date.today()}\n")
                break;        
        except:
            print("File not found")
        
def search():
    while(True):
        try:
            with open(HISTORY_FILE, "r") as f:  
                while(True):
                    found=False
                    clue=input("Enter the name of player to or date to search  his recoed or enter zero to go back :")
                    if(clue=="0"):
                        return
                    f.seek(0)           #make pointer up
                    data=f.readline()
                    while data:
                        words=data.strip().casefold().split()
                        if(clue.casefold() in words):
                            found=True
                            print(data.strip())
                        data=f.readline()
                    if(not found):
                        print("❌ Record not found")
                    print("")
        except:
            print("File not found")

def showStats():
    try:
        with open(HISTORY_FILE, "r") as f:
            data=f.read()
            print(data)
            while(True):
                n=input("Ener 0 to go back : ")
                if(n=="0"):
                    return
    except:
        print("File not found")

def showRules():
    print("\n" + "=" * 40)
    print("HOW TO PLAY")
    print("=" * 40)
    print("1. Choose your attack each turn")
    print("2. Different attacks have different damage and accuracy")
    print("3. 20% chance for critical hits")
    print("4. First to reach 0 HP loses")
    print("=" * 40)
    input("\nPress Enter to continue...")


def getDifficultyLevel():
    print("\n⚔️ Select Difficulty :")
    print("1. Easy 🟢 (80 HP)")
    print("2. Normal 🟡 (100 HP)")
    print("3. Hard 🔴 (120 HP)")

    choice = input("Enter difficulty: ")
    
    if choice == "1":
        return 80
    elif choice == "3":
        return 120
    else:
        print("You give wrong input set as default 100")
        return 100
    
def showAttack():
    print("\nChoose your attack:")
    for key, attack in PLAYER_ATTACKS.items():
        print(f"{key}. {attack['name']} - Damage: {attack['damage']}")
    print("")


def displayHealthBar(name, health, max_health=100):
    print(f"{name}:{health}/{max_health} HP  ❤️")


def isCriticalHit():
    return random.random() <= 0.20  #return true if your luck


def calculateDamage(base_damage):
    if isCriticalHit():
        damage = int(base_damage * 1.5)
        print("🔥 🔥 🔥  CRITICAL HIT!  🔥 🔥 🔥")
        return damage
    return base_damage

def isHit(accuracy):
    if random.random() <= accuracy:
        return True
    else:
        return False


def playerAttack(attackerName, defenderHealth): #retuen health after damage
    print(f"\n{attackerName}'s Turn")
    print(f"Opponent Health: {defenderHealth}")

    showAttack()
    choice = input("Enter b to end game or  attack number: ")
    if choice=="b":
        return "b"

    if choice not in PLAYER_ATTACKS:
        print("Invalid choice! You missed your turn.  😮 😮 😮 😫")
        return defenderHealth

    attack = PLAYER_ATTACKS[choice]
    time.sleep(1) 

    if isHit(attack["accuracy"]):           #check for hit return true
        damage = calculateDamage(attack["damage"])          # for critical hit 
        defenderHealth -= damage                        #base damage is original acctack from dictionary
        print(f"{attackerName} used {attack['name']}! Hit for {damage} damage!  🔥 🔥 🔥 🔥")
    else:
        print(f"{attackerName} used {attack['name']}! It missed! 😮 😮 😮 😫")

    return defenderHealth


def computerAttack(player_health):# return health
    print("\nComputer's Turn")
    time.sleep(1)

    attack = random.choice(ENEMY_ATTACKS)

    if isHit(attack["accuracy"]):
        damage = calculateDamage(attack["damage"])
        player_health -= damage
        print(f"Computer used {attack['name']}! Hit for {damage} damage! 🔥 🔥 🔥 🔥")
    else:
        print(f"Computer used {attack['name']}! It missed! 😮 😮 😮 😫")

    return player_health

# areena
def playGame(mode):
    while True:             #for name
        player1_name = input("\nEnter Player 1 name: ")
        if player1_name.isalpha():
            break
        print("Invalid input! Only letters are allowed.")
    
 

    if mode == "computer":
        player2_name = "Computer"
        playerHealth2 = getDifficultyLevel()
        max_health2 = playerHealth2
    else:
        while True:
            player2_name = input("\nEnter Player 2 name: ")
            if player2_name.isalpha():
                break
            print("Invalid input! Only letters are allowed.")
        
 
        playerHealth2 = 100
        max_health2 = 100

    playerHealth1 = 100
    max_health1 = 100


    print("\nBattle Start! ⚔️  ⚔️  ⚔️  ⚔️  ⚔️  ⚔️  ⚔️  ⚔️ ")
   
    time.sleep(1)

    round_num = 1

    while playerHealth1 > 0 and playerHealth2 > 0:              #main game loop
        print(f"\n{'=' * 40}")
        print(f"ROUND {round_num}")
        print(f"{'=' * 40}")
        displayHealthBar(player1_name, playerHealth1, max_health1)
        displayHealthBar(player2_name, playerHealth2, max_health2)
        
        playerHealth2 = playerAttack(player1_name, playerHealth2)          #health update
        if playerHealth2=="b":
            print("Player1 END THE BALLTE  ⚔️ ⚔️ ⚔️") 
            return

        if playerHealth2 <= 0:
            print(f"\n {player1_name} wins! 🎉 🎉 🎉")
            saveMatchHistory(player1_name, player2_name, player1_name)  #save record
            break

        if mode == "computer":
            playerHealth1 = computerAttack(playerHealth1)
            if playerHealth1 <= 0:
                print(f"\n {player2_name} wins! 🎉 🎉 🎉")
                saveMatchHistory(player1_name, player2_name, player2_name)   #save record
                break
        else:
            playerHealth1 = playerAttack(player2_name, playerHealth1)
            if playerHealth1=="b":
                print("Player2 END THE BALLTE  ⚔️ ⚔️ ⚔️") 
                return
            if playerHealth1 <= 0:
                print(f"\n {player2_name} wins! 🎉 🎉 🎉") 
                saveMatchHistory(player1_name, player2_name, player2_name)
                break

        round_num += 1
        time.sleep(0.5)

    print("⚔️  ⚔️  ⚔️  ⚔️  Game Over  ⚔️  ⚔️  ⚔️  ⚔️  ")
    time.sleep(1)


def main():
    print("=" * 40)
    print("⚔️ ⚔️ ⚔️ ⚔️  WELCOME TO BATTLE GAME  ⚔️  ⚔️  ⚔️  ⚔️ ")
    print("=" * 40)

    while True:
        print("\nMain Menu")
        print("1. Play vs Computer 🤖")
        print("2. Play vs Friend 🧑‍🤝‍🧑")
        print("3. View Statistics 📊")
        print("4. How to Play 📜")
        print("5. Search 🔍")
        print("6. Exit ❌")

        choice = input("\nEnter your choice ⚔️ : ")

        if choice == "1":
            playGame("computer")
        elif choice == "2":
            playGame("friend")
        elif choice == "3":
            showStats()
        elif choice == "4":
            showRules()
        elif choice=="5":
            search()
        elif choice == "6":
            print("\nThanks for playing  👋 👋 👋!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


main()
