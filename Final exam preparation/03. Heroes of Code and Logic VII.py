heroes_number = int(input())

hit_points_by_hero = {}
mana_points_by_hero = {}

for _ in range(heroes_number):
    hero_arguments = input().split()
    hero = hero_arguments[0]
    hit_points = int(hero_arguments[1])
    mana_points = int(hero_arguments[2])

    hit_points_by_hero[hero] = hit_points
    mana_points_by_hero[hero] = mana_points

while True:
    line = input()
    if line == 'End':
        break
    command_args = line.split(' - ')
    command = command_args[0]
    hero = command_args[1]

    if command == 'CastSpell':
        mana_for_spell = int(command_args[2])
        spell_name = command_args[3]

        if mana_for_spell > mana_points_by_hero[hero]:
            print(f'{hero} does not have enough MP to cast {spell_name}!')
        else:
            mana_points_by_hero[hero] -= mana_for_spell
            print(f'{hero} has successfully cast {spell_name} and now has {mana_points_by_hero[hero]} MP!')
    elif command == 'TakeDamage':
        damage = int(command_args[2])
        attacker = command_args[3]

        hit_points_by_hero[hero] -= damage
        if hit_points_by_hero[hero] <= 0:
            print(f'{hero} has been killed by {attacker}!')
            mana_points_by_hero.pop(hero)
            hit_points_by_hero.pop(hero)
        else:
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {hit_points_by_hero[hero]} HP left!')
    elif command == 'Recharge':
        mana_amount = int(command_args[2])
        mana_before_recharge = mana_points_by_hero[hero]
        mana_points_by_hero[hero] = min(mana_points_by_hero[hero] + mana_amount, 200)
        print(f'{hero} recharged for {mana_points_by_hero[hero] - mana_before_recharge} MP!')
    else:
        heal_amount = int(command_args[2])
        hit_points_before_heal = hit_points_by_hero[hero]
        hit_points_by_hero[hero] = min(hit_points_by_hero[hero] + heal_amount, 100)
        print(f"{hero} healed for {hit_points_by_hero[hero] - hit_points_before_heal} HP!")

for hero in mana_points_by_hero.keys():
    hit_points = hit_points_by_hero[hero]
    mana_points = mana_points_by_hero[hero]
    print(f'{hero}\n  HP: {hit_points}\n  MP: {mana_points}')
