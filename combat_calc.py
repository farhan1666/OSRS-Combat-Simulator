#Created by @Phoneman_btw
import random
def simHit(accuracy, maxHit):
	accuracy_rand = random.randint(0,10000)
	hit = random.randint(0, maxHit)
	if accuracy * 10000 >= accuracy_rand:
		return hit
	else:
		return 0

def simScytheHit(accuracy, maxHit):
	final_hit = 0
	final_hit += simHit(accuracy, maxHit)
	final_hit += simHit(accuracy, multiplyDown(maxHit, 0.5))
	final_hit += simHit(accuracy, multiplyDown(maxHit, 0.25))
	return final_hit

#This section is for melee and ranged max hit

def multiplyDown(number, multiplier): #Increases the number by multiplier then floors it lmao
	number *= multiplier
	number = int(number)
	return number

def calcMaxHit(effective_strength, equipment_strength, set_bonus = "", special_attack = "", mage_level = 0):
	maxHit = int(0.5 + effective_strength * (equipment_strength+64)/640)
	if special_attack == "Bandos godsword":
		maxHit = multiplyDown(maxHit, 1.10)
	elif special_attack == "Dragon warhammer":
		maxHit = multiplyDown(maxHit, 1.50)
	elif special_attack == "Twisted bow":
		maxHit = multiplyDown(maxHit, (0.5386 + 0.0087 * mage_level - 0.000009 * mage_level**2))
	if set_bonus == "Inquisitor":
		maxHit = multiplyDown(maxHit, 1.025)
	return maxHit

def getEffectiveStrength(combat, visible_level, style, prayer = "none", set_bonus = "none"):
	if prayer == "Piety":
		visible_level *= 1.23
	elif prayer == "Rigour":
		visible_level *= 1.23
	visible_level = int(visible_level)

	if style == "Aggressive":
		visible_level += 3
	elif style == "Controlled":
		visible_level += 1
	elif style == "Accurate":
		if combat == "Ranged":
			visible_level += 3

	visible_level += 8
	if set_bonus == "Regular Void":
		visible_level = multiplyDown(visible_level, 1.1)
	elif set_bonus == "Elite Void":
		if combat == "Ranged":
			visible_level = multiplyDown(visible_level, 1.125)
	return visible_level

#This section is for magic max hit

def calcMageMaxHit(spell = "Sang", visible_mage = 120, anc_pieces = 3, occult = True, torm = True,  harm = False, tome = True):
	magic_boost = anc_pieces * 0.02 + occult * 0.10 + torm * 0.05 + harm * 0.15
	if spell == "Sang":
		maxHit = int(visible_mage / 3) - 1
	elif spell == "Fire Surge":
		maxHit = 24
	maxHit = multiplyDown(maxHit, 1 + magic_boost)
	if spell == "Fire Surge" and tome == True:
		maxHit = multiplyDown(maxHit, 1.5)
	return maxHit

#This section is for calculating accuracy

def calcAttackRoll(effective_level, equipment_bonus, special_attack = "", mage_level = 0): #Take the corresponding stab, slash, crush, ranged or magic attack bonus from the equipment stats interface and let this equal equipment_bonus
	max_roll = effective_level * (equipment_bonus + 64)
	if special_attack == "Bandos Godsword":
		max_roll = multiplyDown(max_roll, 2.00)
	elif special_attack == "Twisted bow":
		max_roll = multiplyDown(max_roll, min((0.399 + 0.0063 * min((350, mage_level)) - 0.000009 * min((350, mage_level))**2), 1.4)) #Bow accuracy capped at 1.4	
	print("Max Attack roll:", max_roll)
	return max_roll

def calcDefenceRoll(effective_level, equipment_bonus):
	max_roll = effective_level * (equipment_bonus + 64)
	print("Max Defence roll:", max_roll)
	return max_roll

def calcHitChance(max_attack_roll, max_defence_roll):
	if max_attack_roll > max_defence_roll:
		hit_chance = 1 - (max_defence_roll + 2) / (2 * (max_attack_roll + 1))
	else:
		hit_chance = max_attack_roll / (2 * (max_defence_roll + 1))
	return hit_chance


def getEffectiveLevel(visible_level, style = "Controlled", combat = "", prayer = "", set_bonus = ""): #Monsters are basically always on controlled for calculations sake
	effective_level = visible_level
	if prayer == "Piety":
		effective_level = multiplyDown(effective_level, 1.2)
	elif prayer == "Rigour":
		effective_level = multiplyDown(effective_level, 1.2)
	elif prayer == "Augury":
		effective_level = multiplyDown(effective_level, 1.25)
	if style =="Accurate":
		effective_level += 3
	elif style == "Controlled":
		effective_level += 1
	elif style == "Long range":
		if combat == "Magic":
			effective_level += 1
	effective_level += 8
	if set_bonus == "Regular Void":
		if combat == "Melee" or "Ranged":
			effective_level = multiplyDown(effective_level, 1.10)
		elif combat == "Magic":
			effective_level = multiplyDown(effective_level, 1.45)
	return effective_level


def main():
	max_hit = calcMageMaxHit("Sang", 99)
	effective_level = getEffectiveLevel(99, "Accurate", "Magic")
	def_effective_level = getEffectiveLevel(250)
	equipment_bonus = 31
	def_equipment_bonus = 50
	attack_roll = calcAttackRoll(effective_level, equipment_bonus)
	defence_roll = calcDefenceRoll(def_effective_level, def_equipment_bonus)
	# accuracy = calcHitChance(attack_roll, defence_roll)
	hits = []
	for i in range(100000):
		hits.append(calcHitChance(attack_roll, defence_roll))
	print(sum(hits) / len(hits))
if __name__ == '__main__':
	main()
