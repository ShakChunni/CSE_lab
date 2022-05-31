# 3


def hoc_builder(height):
    initial_cards = 8
    if height == 0:
        return
    elif height == 1:
        cards = 8
        final_cards = cards
        return final_cards
    elif height > 1:
        cards = initial_cards + ((height-1)*5)
        return cards


print(hoc_builder(3))
