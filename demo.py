def ability_modifier_table(score: int) -> int:
    if not 1 <= score <= 30:
        raise ValueError("Ability score must be between 1 and 30.")
    return (score - 10) // 2



print(ability_modifier_table(1))
print(ability_modifier_table(16))