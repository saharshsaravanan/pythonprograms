import string
import time
import time


class PassiveUpgrade:
    def __init__(self):
        self.level = 1  # Starts at level 1
        self.multiplier = 1  # No boost at first
        self.base_cost = 1000  # Initial price

    def purchase_upgrade(self, coins):
        """Buy x2 passive income upgrade with 5× cost scaling"""
        if coins >= self.base_cost:
            coins -= self.base_cost  # Deduct cost
            self.multiplier *= 2  # Double passive income
            self.base_cost *= 5  # Cost multiplies by 5 for the next upgrade

            print(
                f"Upgrade Purchased! Passive Income now x{self.multiplier}. Next upgrade costs {self.base_cost} coins.")
        else:
            print("Not enough coins to buy this upgrade.")

        return coins


#


class Upgrade:
    def __init__(self, name, level_required, click_bonus):
        self.name = name
        self.level_required = level_required
        self.click_bonus = click_bonus

class Skill:
    def __init__(self, name, description, hotkey, base_cooldown, duration):
        self.name = name
        self.description = description
        self.hotkey = hotkey
        self.base_cooldown = base_cooldown
        self.duration = duration
        self.on_cooldown = False

    def activate(self):
        if not self.on_cooldown:
            print(f"{self.name} activated! Auto-clicking for {self.duration} seconds.")
            self.on_cooldown = True
            time.sleep(self.duration)  # Simulate skill duration
            print(f"{self.name} ended. Cooldown started.")
            time.sleep(self.base_cooldown)  # Simulate cooldown
            self.on_cooldown = False
            print(f"{self.name} is ready to use again.")

class ClickerHero:
    def __init__(self):
        self.level = 1
        self.click_damage = 1
        self.upgrades = [
            Upgrade("Big Clicks", 10, 1.0),
            Upgrade("Huge Clicks", 25, 1.0),
            Upgrade("Massive Clicks", 50, 1.0),
            Upgrade("Titanic Clicks", 100, 1.5),
            Upgrade("Colossal Clicks", 200, 2.0),
            Upgrade("Monumental Clicks", 400, 2.5),
        ]
        self.clickstorm = Skill("Clickstorm", "Auto-clicks rapidly for 30 seconds.", "1", 600, 30)

    def check_upgrades(self):
        for upgrade in self.upgrades:
            if self.level >= upgrade.level_required:
                self.click_damage *= (1 + upgrade.click_bonus)
                print(f"{upgrade.name} unlocked! Click damage is now {self.click_damage}.")

    def click(self):
        print(f"Clicked! Dealt {self.click_damage} damage.")
        self.level += 1  # Leveling up for testing purposes
        self.check_upgrades()

    def activate_skill(self):
        self.clickstorm.activate()

# Example Usage
player = ClickerHero()
player.click()  # Clicking will now level up and unlock upgrades automatically
player.activate_skill()


def generate_notation(count):
    letters = list(string.ascii_uppercase)
    a1, a2 = 0, 0

    while len(letters) < count:
        index = len(letters)
        if index < 26:
            new_notation = letters[a1]
        elif index < 26 ** 2:
            new_notation = letters[a1] + letters[a2]
        else:
            indexes = [(index // (26 ** i)) % 26 for i in range(3)]
            new_notation = ''.join(letters[i] for i in reversed(indexes))

        letters.append(new_notation)
        a2 += 1

        if a2 >= len(letters):
            a1 += 1
            a2 = 0

    return letters[-1]
def keep_first_three_digits(num):
    return int(str(num)[:3])


def notation_to_number(notation):
    """ Convert notation suffix into a ranking number. """
    letters = list(string.ascii_uppercase)
    suffix = ''.join(filter(str.isalpha, notation))  # Extract only letters
    base_value = 0

    for i, char in enumerate(reversed(suffix)):  # Process from last letter
        base_value += (letters.index(char) + 1) * (26 ** i)

    return base_value


def subtract_notation(notation1, notation2):
    """ Subtract notation values, keeping correct format. """
    num1 = int(''.join(filter(str.isdigit, notation1)))  # Extract numbers
    num2 = int(''.join(filter(str.isdigit, notation2)))

    notation_rank1 = notation_to_number(notation1)
    notation_rank2 = notation_to_number(notation2)

    # Perform subtraction
    new_number = num1 - num2
    new_notation_rank = max(notation_rank1 - notation_rank2, 0)  # Avoid negative notation ranks

    # Convert back to notation
    letters = list(string.ascii_uppercase)
    new_suffix = ""

    while new_notation_rank > 0:
        new_notation_rank, remainder = divmod(new_notation_rank - 1, 26)
        new_suffix = letters[remainder] + new_suffix

    return f"{new_number}{new_suffix}"


import mysql.connector


def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")


    # Connect to MySQL Database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="game"
    )
    cursor = conn.cursor()

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()
    print("checking password")
    time.sleep(2.34+len(password)/999)
    if existing_user:
        print("Username already exists. Try another one.")
        return False
    print("user does not exist:registered")

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()  # Save changes

    print(f"User '{username}' registered successfully!")

    # Close connection
    cursor.close()
    conn.close()
    return True  # Registration successful


# Run registration function



def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Connect to MySQL Database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="game"
    )
    cursor = conn.cursor()

    # Validate credentials
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    print("checking password",end=" ")

    time.sleep(3.091+len(password)*1.6324)

    if user:
        print(f"Welcome, {username}! Login successful.")
        return True
    else:
        print("Invalid login. Please try again.❌❌❌❌❌❌❌❌❌❌❌❌")
        return False

    cursor.close()
    conn.close()
    import mathdef convert_alpha_exp(s):
    if not s.startswith("1e"):
        return s  # Not scientific notation mode

    num_part = s[2:]
    digits = ""
    alpha = ""

    # Split numeric and alphabetic parts
    for ch in num_part:
        if ch.isdigit():
            digits += ch
        else:
            alpha += ch





    def transcendence_power(lifetime_ancient_souls):
        """Calculates Transcendence Power (TP) based on Lifetime Ancient Souls."""
        tp = 2 ** (0.0003 * lifetime_ancient_souls) - sqrt(lifetime_ancient_souls)
        return max(tp-2, 0)  # Ensures TP is at least 0 to not get negetive souls


from math import prod, sqrt, ceil, floor

class ClickerGame:
    def __init__(self,name):
        self.name = name
        self.zone = 1
        self.enemies_per_zone = 10
        self.enemies_defeated = 0
        self.gold = 0
        self.boss_zone_interval = 5
        self.lynel_interval = 23
        self.total_bosses_defeated = 0
        self.crit_unlocked = True
        self.crit_chance = 0.00001
        self.crit_multiplier = 021.999999
    def calculate_gold_reward(self, is_boss, is_lynel):
            if self.zone == 1:
                gold = 1
            elif self.zone <= 140:
                gold = 1.6 ** self.zone
            else:
                gold = 4.717e28 * (1.15 ** (self.zone - 140))

            if is_lynel:
                gold *= 15
            elif is_boss:
                gold *= 10
            return gold

        def calculate_hp(self, is_boss, is_lynel):
            if self.zone <= 140:
                hp = ceil(10 * (self.zone - 1 + 1.55 ** (self.zone - 1)) * (10 if is_boss else 1))
            elif self.zone <= 500:
                hp = ceil(10 * (139 + 1.55 ** 139 * 1.145 ** (self.zone - 140)) * (10 if is_boss else 1))
            else:
                hp = ceil(10 * (139 + 1.55 ** 139 * 1.145 ** 360 * prod(
                    [(1.145 + 0.001 * floor((i - 1) / 500)) for i in range(501, self.zone + 1)])) * (
                                   10 if is_boss else 1))

            if is_lynel:
                hp *= 2

            return hp

        def defeat_enemy(self):
            is_boss = self.zone % self.boss_zone_interval == 0
            is_lynel = is_boss and self.total_bosses_defeated % self.lynel_interval == 0

            gold_reward = self.calculate_gold_reward(is_boss, is_lynel)
            hp = self.calculate_hp(is_boss, is_lynel)
            self.gold += gold_reward
            self.enemies_defeated += 1

            enemy_type = "Lynel Boss" if is_lynel else "Boss" if is_boss else "Enemy"
            print(f"{enemy_type} defeated! Gold earned: {gold_reward}, HP was: {hp}, Total Gold: {self.gold}")

            if is_boss:
                self.total_bosses_defeated += 1

            if self.enemies_defeated >= self.enemies_per_zone:
                self.advance_zone()
            else:
                print()




        def advance_zone(self):
            self.zone += 1
            self.enemies_defeated = 0

            if self.zone % 500 == 0:
                self.enemies_per_zone += 1

            print(f"Zone {self.zone} reached! Enemies to defeat: {self.enemies_per_zone}")

        import math


    def upgrade_crit_chance(self):
            self.crit_chance += 0.02
            return min(0.45,self.crit_chance)
    def upgrade_crit_damage(self):
        self.crit_multiplier *= 1.001
        return max(20, self.crit_multiplier)
    class Player:
        def __init__(self):
            self.gold = 0
            self.hero_souls = 0.0
            self.gold_multiplier = 1.0
            self.dps_multiplier = 1.0
            self.hero_soulsifasend = 0.0

        def earn_gold(self, base_income):
            soul_effect = 1 + (self.hero_souls * 0.1 )  # Minor scaling without breaking balance
            self.gold += base_income * self.gold_multiplier * soul_effect

        def ascension_boost(self):
            self.hero_souls += self.self.hero_soulsifasend  # Example scaling based on playtime
            self.dps_multiplier = 1.1*self.hero_souls  # Ensuring meaningful boost

    player = Player()




