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
	defences = []

	for i in range(40000):
		tekton = NPC(1200, 217, 217, 155, 165, 105, 0, 0)
		accuracy, max_hit = inqHammer(tekton)

		damage1 = simHit(accuracy, max_hit)
		damage2 = simHit(accuracy, max_hit)

		if damage1 > 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.3))
		if damage2 > 0:
			tekton.lower_def(multiplyDown(tekton.defence, 0.3))

		accuracy, max_hit = inqBGS(tekton)

		damage3 = simHit(accuracy, max_hit)
		damage4 = simHit(accuracy, max_hit)
		damage5 = simHit(accuracy, max_hit)
		damage6 = simHit(accuracy, max_hit)
		damage7 = simHit(accuracy, max_hit)

		tekton.lower_def(damage3)
		tekton.lower_def(damage4)
		tekton.lower_def(damage5)
		tekton.lower_def(damage6)
		tekton.lower_def(damage7)

		defences.append(tekton.defence)

	print("Mode:", mode(defences))
	print("Median:", median(defences))
	print("Mean", mean(defences))
	zero_def_rate = round((defences.count(0) / len(defences) * 100), 2)
	print("Amount of times at 0 defence: "+str(defences.count(0)))

	print("That's "+str(zero_def_rate)+"% of the time, or 1/"+str(round((defences.count(0) /  len(defences)) ** -1, 2)))



if __name__ == '__main__':
	main()
