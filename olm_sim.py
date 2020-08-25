from combat_calc import *
#Olm procedure
#	Everyone ovl'd once going in
#	specs on melee hand (3 dwh, 4 bgs)
#	Kill mage hand
#	Kill melee hand
#	25 sec intermission
#	3 warhammer, 4 bgs specs
#	Kill mage hand
#	Kill melee hand
#	25 sec intermission
#	3 warhammer, 4 bgs specs
#	Get melee low
#	Get mage low
#	Kill both at same time
#	Range Olm

def sangHit():
	pass

def inqHammer(NPC):
	att_effective_level = getEffectiveLevel(120, "Accurate", "Melee", "Piety")
	def_effective_level = getEffectiveLevel(NPC.defence)
	attack_roll = calcAttackRoll(att_effective_level, 192, "Inquisitor")
	defence_roll = calcDefenceRoll(def_effective_level, 50)
	accuracy = calcHitChance(attack_roll, defence_roll)
	effective_strength = getEffectiveStrength("Melee", 118, "Accurate", "Piety")
	print(effective_strength)
	max_hit = calcMaxHit(effective_strength, 148, "Inquisitor", "Dragon warhammer")
	return accuracy, max_hit

#(self, hp, defence, mage, stab_def, slash_def, crush_def, mage_def, range_def):

def main():
	olm_mage_hand = NPC(2400, 185, 92, 200, 200, 200, 50, 200)
	olm_melee_hand = NPC(2400, 185, 185, 50, 50, 50, 200, 200)
	olm_head = NPC(3200, 159, 300, 200, 200, 200, 200, 50)

	number_of_players = 7

	print(inqHammer(olm_melee_hand))

	#def calcAttackRoll(effective_level, equipment_bonus, special_attack = "", mage_level = 0)
	#def calcDefenceRoll(effective_level, equipment_bonus):
	#def calcHitChance(max_attack_roll, max_defence_roll, brimstone = False):
	#calcMaxHit(effective_strength, equipment_strength, set_bonus = "", special_attack = "", mage_level = 0)
	#getEffectiveStrength(combat, visible_level, style, prayer = "none", set_bonus = "none"):
	#getEffectiveLevel(visible_level, style = "Controlled", combat = "", prayer = "", set_bonus = "")




if __name__ == '__main__':
	main()