from collections import defaultdict

def split_bill(items, shares):
    amounts = defaultdict(float)

    item_costs = {}
    for item, cost in items.items():
        item_costs[item] = cost

    for item, people in shares.items():
        if item in item_costs:
            cost_per_person = item_costs[item] / len(people)
            for person in people:
                amounts[person] += cost_per_person

    return amounts

items = {
    'Chargah': 1200,
    'Salad': 100,
    'Limca': 300
}

shares = {
    'Chargah': ['A.Aziz', 'A.Hadi'],
    'Salad': ['A.Aziz', 'A.Hadi', 'Salman'],
    'Limca': ['Salman']
}

amounts_owed = split_bill(items, shares)

for person, amount in amounts_owed.items():
    print(f'{person} owes ${amount:.2f}')
