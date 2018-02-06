# Cats with hats
theCats = {}
loops = 0

#create 100 hatless cats in theCats dictionary
for i in range(1, 1001):
    theCats["Cat " + str(i)] = False

for i in range(1, 1001):
    loops += 1
    count = 0
    for cat, hats in theCats.items():
        count += 1
        if count % loops == 0:
            if theCats[cat]:
                theCats[cat] = False
            else:
                theCats[cat] = True

# print results
for cat, hats in theCats.items():
    if theCats[cat]:
        print(f"{cat} has a hat!")
    else:
        print(f"{cat} is hatless!")
