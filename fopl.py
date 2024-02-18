global facts
global is_changed

is_changed = True
facts = [["can_fly", "sparrow"], ["has_feathers", "sparrow"], ["animal", "sparrow"]]

def assert_fact(fact):
    global facts
    global is_changed
    if fact not in facts:
        facts.append(fact)
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "animal":
            assert_fact(["living_organism", A1[1]])
        if A1[0] == "living_organism" and ["can_fly", A1[1]] in facts:
            assert_fact(["bird", A1[1]])

print(facts)

is_changed = True
facts = [["mammal", "lion"], ["has_fur", "lion"], ["animal", "lion"]]

def assert_fact(fact):
    global facts
    global is_changed
    if fact not in facts:
        facts.append(fact)
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "animal":
            assert_fact(["living_organism", A1[1]])
        if A1[0] == "living_organism" and ["mammal", A1[1]] in facts:
            assert_fact(["warm_blooded", A1[1]])

print(facts)