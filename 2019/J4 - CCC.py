def main(Seq):
    # Input
    Lst = [
        ["1", "2"],
        ["3", "4"]
    ]

    # Data Processing
    for i in range(len(Seq)):
        if Seq[i] == "H":
            Lst.reverse()
        elif Seq[i] == "V":
            for h in Lst:
                h.reverse()
    # Output
    for j in Lst:
        Na = " ".join(j)
        print(Na)


def InputF():
    Seq = input()
    count = 0
    for a in range(len(Seq)):
        if Seq[a] == "H":
            count += 1
        if Seq[a] == "V":
            count += 1
    if count != len(Seq):
        print("Make sure Your input is Either H or V")
        InputF()
    else:
        main(Seq)


if __name__ == "__main__":
    InputF()



