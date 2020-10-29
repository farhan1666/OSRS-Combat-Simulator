from combat_calc import *
from statistics import mean, mode, median

def inqHammer(NPC):
	att_effective_level = getEffectiveLevel(118, "Accurate", "Melee", "Piety")
	def_effective_level = getEffectiveLevel(NPC.defence)
	attack_roll = calcAttackRoll(att_effective_level, 192, "Inquisitor")
	defence_roll = calcDefenceRoll(def_effective_level, NPC.crush_def)
	accuracy = calcHitChance(attack_roll, defence_roll)
	effective_strength = getEffectiveStrength("Melee", 118, "Accurate", "Piety")
	max_hit = calcMaxHit(effective_strength, 148, "Inquisitor", "Dragon warhammer")
	return accuracy, max_hit

def Hammer(NPC):
	att_effective_level = getEffectiveLevel(118, "Accurate", "Melee", "Piety")
	def_effective_level = getEffectiveLevel(NPC.defence)
	attack_roll = calcAttackRoll(att_effective_level, 160)
	defence_roll = calcDefenceRoll(def_effective_level, NPC.crush_def)
	accuracy = calcHitChance(attack_roll, defence_roll)

	effective_strength = getEffectiveStrength("Melee", 118, "Accurate", "Piety")
	max_hit = calcMaxHit(effective_strength, 150, "", "Dragon warhammer")
	return accuracy, max_hit



def inqBGS(NPC):
	att_effective_level = getEffectiveLevel(118, "Aggressive", "Melee", "Piety")
	def_effective_level = getEffectiveLevel(NPC.defence)
	attack_roll = calcAttackRoll(att_effective_level, 149, "Inquisitor", "Bandos godsword")
	defence_roll = calcDefenceRoll(def_effective_level, NPC.slash_def)
	accuracy = calcHitChance(attack_roll, defence_roll)
	effective_strength = getEffectiveStrength("Melee", 118, "Aggressive", "Piety")
	max_hit = calcMaxHit(effective_strength, 183, "Inquisitor", "Bandos godsword")
	return accuracy, max_hit


def main():
	# (self, hp, defence, mage, stab_def, slash_def, crush_def, mage_def, range_def):
	tekton_hp_inq = []

	for i in range(100000):
		tekton = NPC(300, 205, 205, 155, 165, 105, 0, 0)
		accuracy, max_hit = inqHammer(tekton)

		venghit1 = simHit(1, 51)
		venghit2 = simHit(1, 51)

		tekton.lower_hp(int((venghit1+1)*.75))
		tekton.lower_hp(int((venghit2+1)*.75))

		damage1 = simHit(accuracy, max_hit)

		if damage1 > 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.3))
		if damage1 == 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.05))

		accuracy, max_hit = inqHammer(tekton)
		damage2 = simHit(accuracy, max_hit)

		if damage2 > 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.3))
		if damage2 == 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.05))

		tekton.lower_hp(damage1)
		tekton.lower_hp(damage2)
		att_effective_level = getEffectiveLevel(118, "Aggressive", "Melee", "Piety")
		def_effective_level = getEffectiveLevel(tekton.defence)
		attack_roll = calcAttackRoll(att_effective_level, 99, "Inquisitor")
		defence_roll = calcDefenceRoll(def_effective_level, tekton.crush_def)
		accuracy = calcHitChance(attack_roll, defence_roll)
		effective_strength = getEffectiveStrength("Melee", 118, "Aggressive", "Piety")
		max_hit = calcMaxHit(effective_strength, 130, "inquisitor", "")

		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton_hp_inq.append(tekton.hp)


	tekton_hp_bandos = []
	for i in range(100000):
		tekton = NPC(300, 205, 205, 155, 165, 105, 0, 0)

		venghit1 = simHit(1, 51)
		venghit2 = simHit(1, 51)

		tekton.lower_hp(int((venghit1+1)*.75))
		tekton.lower_hp(int((venghit2+1)*.75))

		accuracy, max_hit = Hammer(tekton)

		damage1 = simHit(accuracy, max_hit)


		if damage1 > 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.3))
		if damage1 == 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.05))
		accuracy, max_hit = Hammer(tekton)
		damage2 = simHit(accuracy, max_hit)
		if damage2 > 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.3))
		if damage2 == 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.05))

		tekton.lower_hp(damage1)
		tekton.lower_hp(damage2)
		att_effective_level = getEffectiveLevel(118, "Aggressive", "Melee", "Piety")
		def_effective_level = getEffectiveLevel(tekton.defence)
		attack_roll = calcAttackRoll(att_effective_level, 147, "")
		defence_roll = calcDefenceRoll(def_effective_level, tekton.slash_def)
		accuracy = calcHitChance(attack_roll, defence_roll)
		effective_strength = getEffectiveStrength("Melee", 118, "Aggressive", "Piety")
		max_hit = calcMaxHit(effective_strength, 132, "", "")
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton.lower_hp(simScytheHit(accuracy, max_hit))
		tekton_hp_bandos.append(tekton.hp)



	print("inq: ", str(tekton_hp_inq.count(0)))

	print("Bandos: ", str(tekton_hp_bandos.count(0)))

	print("inq rate: 1/", str(100000/tekton_hp_inq.count(0)))
	print("Bandos rate: 1/", str(100000/tekton_hp_bandos.count(0)))





if __name__ == '__main__':
	main()