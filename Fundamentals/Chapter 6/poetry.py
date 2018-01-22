# wax_poetic
import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert",
         "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes",
         "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant",
              "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in",
                "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously",
           "sensuously"]


def makePoem():
    # select 3 adjectives
    a1 = random.choice(adjectives)
    a2 = random.choice(adjectives)
    a3 = random.choice(adjectives)
    while a1 == a2 or a1 == a3:
        a1 = random.choice(adjectives)
    while a2 == a3:
        a2 = random.choice(adjectives)

    # select 3 nouns
    n1 = random.choice(nouns)
    n2 = random.choice(nouns)
    n3 = random.choice(nouns)
    while n1 == n2 or n1 == n3:
        n1 = random.choice(adjectives)
    while n2 == n3:
        n2 = random.choice(nouns)

    # select 3 verbs
    v1 = random.choice(verbs)
    v2 = random.choice(verbs)
    v3 = random.choice(verbs)
    while v1 == v2 or v1 == v3:
        v1 = random.choice(adjectives)
    while v2 == v3:
        v2 = random.choice(adjectives)

    # select 2 prepositions
    p1 = random.choice(prepositions)
    p2 = random.choice(prepositions)
    while p1 == p2:
        p1 = random.choice(nouns)

    # select 1 adverb
    a1 = random.choice(adverbs)

    # detects if first word starts with a vowel
    context_a = "A"
    if "aeiou".find(a1[0]) != -1:
        context_a = "An"

    print(f"{context_a} {a1} {n1}")
    print()
    print(f"{context_a} {a1} {n1} {v1} {p1} the {a2} {n2}")
    print(f"{a1}, the {n1} {v2}")
    print(f"the {n2} {v3} {p2} a {a3} {n3}")


makePoem()
