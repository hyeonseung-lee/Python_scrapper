
name = str(input("Who do you want to be blamed? : "))
times = int(input("How much times? : "))
name += " "

for time in range(times):
    print(" ")
    for i in range(8):
        fuck = ""
        fuck += " "*len(name)*5
        fuck += name
        fuck += " "*len(name)*5
        print(fuck)

    for j in range(5):
        fuck = ""
        fuck = name*11
        print(fuck)