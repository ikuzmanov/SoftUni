def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    left_half = ticket[:10]
    right_half = ticket[10:]
    winning_characters = ['@', '#', '$', '^']
    for winning_character in winning_characters:
        for repetition in range(10, 0, -1):
            character_repetition = winning_character * repetition
            if character_repetition in left_half and character_repetition in right_half:
                if repetition == 10:
                    return f'ticket "{ticket}" - {len(character_repetition)}{winning_character} Jackpot!'
                elif 6 <= repetition <= 9:
                    return f'ticket "{ticket}" - {len(character_repetition)}{winning_character}'

    return f'ticket "{ticket}" - no match'


tickets = [s.strip() for s in input().split(", ")]

ticket_state = []

for ticket in tickets:
    ticket_state.append(is_winning(ticket))

[print(s) for s in ticket_state]