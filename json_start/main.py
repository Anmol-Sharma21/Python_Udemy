try:
    file = open("dazta.txt")
except:
    file = open("dazta.txt", "w")
    file.write("something")