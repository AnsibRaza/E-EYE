import random, os
path = r"C:\Users\Dell\Documents\LiClipse Workspace\Profi\E-EYE\E-EYE\Definitions\savepic"
random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
print(random_filename)