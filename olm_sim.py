from combat_calc import *
from statistics import mean, mode, median


# Olm procedure
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
    defence_roll = calcDefenceRoll(def_effective_level, NPC.crush_def)
    accuracy = calcHitChance(attack_roll, defence_roll)
    effective_strength = getEffectiveStrength("Melee", 120, "Accurate", "Piety")
    max_hit = calcMaxHit(effective_strength, 148, "Inquisitor", "Dragon warhammer")
    return accuracy, max_hit


def inqBGS(NPC):
    att_effective_level = getEffectiveLevel(120, "Aggressive", "Melee", "Piety")
    def_effective_level = getEffectiveLevel(NPC.defence)
    attack_roll = calcAttackRoll(att_effective_level, 149, "Inquisitor", "Bandos godsword")
    defence_roll = calcDefenceRoll(def_effective_level, 50)
    accuracy = calcHitChance(attack_roll, defence_roll)
    effective_strength = getEffectiveStrength("Melee", 120, "Aggressive", "Piety")
    max_hit = calcMaxHit(effective_strength, 183, "Inquisitor", "Bandos godsword")
    return accuracy, max_hit


# (self, hp, defence, mage, stab_def, slash_def, crush_def, mage_def, range_def):

def main():
    olm_mage_hand = NPC(2400, 185, 92, 200, 200, 200, 50, 200)
    olm_head = NPC(3200, 159, 300, 200, 200, 200, 200, 50)
    olm_melee_hand = NPC(2400, 185, 185, 50, 50, 50, 200, 200)
    defences = []

    for i in range(40000):
        olm_melee_hand = NPC(2400, 185, 185, 50, 50, 50, 200, 200)
        accuracy, max_hit = inqHammer(olm_melee_hand)

        damage1 = simHit(accuracy, max_hit)
        damage2 = simHit(accuracy, max_hit)
        #damage3 = simHit(accuracy, max_hit)

        if damage1 > 0:
            olm_melee_hand.lower_def(multiplyDown(olm_melee_hand.defence, 0.3))
        if damage2 > 0:
            olm_melee_hand.lower_def(multiplyDown(olm_melee_hand.defence, 0.3))
        #if damage3 > 0:
        #    olm_melee_hand.lower_def(multiplyDown(olm_melee_hand.defence, 0.3))

        accuracy, max_hit = inqBGS(olm_melee_hand)

        damage3 = simHit(accuracy, max_hit)
        damage4 = simHit(accuracy, max_hit)
        damage5 = simHit(accuracy, max_hit)
        damage6 = simHit(accuracy, max_hit)
        damage7 = simHit(accuracy, max_hit)

        olm_melee_hand.lower_def(damage3)
        olm_melee_hand.lower_def(damage4)
        olm_melee_hand.lower_def(damage5)
        olm_melee_hand.lower_def(damage6)
        olm_melee_hand.lower_def(damage7)

        defences.append(olm_melee_hand.defence)

    print("Mode:", mode(defences))
    print("Median:", median(defences))
    print("Mean", mean(defences))
    zero_def_rate = round((defences.count(0) / len(defences) * 100), 2)
    print("Amount of times at 0 defence: " + str(defences.count(0)))

    print("That's " + str(zero_def_rate) + "% of the time, or 1/" + str(round((defences.count(0) /  len(defences)) ** -1, 2)))



# print(olm_melee_hand.defence)
# def calcAttackRoll(effective_level, equipment_bonus, special_attack = "", mage_level = 0)
# def calcDefenceRoll(effective_level, equipment_bonus):
# def calcHitChance(max_attack_roll, max_defence_roll, brimstone = False):
# calcMaxHit(effective_strength, equipment_strength, set_bonus = "", special_attack = "", mage_level = 0)
# getEffectiveStrength(combat, visible_level, style, prayer = "none", set_bonus = "none"):
# getEffectiveLevel(visible_level, style = "Controlled", combat = "", prayer = "", set_bonus = "")


if __name__ == '__main__':
    main()
