with open("day07.in") as f:
    inp = f.read().strip().split("\n")

# PROBLEM 1 (Rank 662)

scored_hands = []
labels = list("23456789TJQKA")
for row in inp:
    cards, bid = row.split()

    hands = [cards.count(label) for label in labels]
    hands = sorted(hands, reverse=True)

    scored_hands.append((hands, [labels.index(c) for c in cards], int(bid)))

scored_hands = sorted(scored_hands)
score = sum(scored_hands[i][2] * (i + 1) for i in range(len(inp)))

print(score)

# PROBLEM 2 (Rank 274)

scored_hands = []
labels = list("J23456789TQKA")
for row in inp:
    cards, bid = row.split()

    hands = [cards.count(label) for label in labels if label != "J"]
    hands = sorted(hands, reverse=True)
    hands[0] += cards.count("J")

    scored_hands.append((hands, [labels.index(c) for c in cards], int(bid)))

scored_hands = sorted(scored_hands)
score = sum(scored_hands[i][2] * (i + 1) for i in range(len(inp)))

print(score)
