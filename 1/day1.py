file = open("./input.txt", "r")
input = file.read().split("\n\n")
summed_totals = [sum([int(y) for y in x.split("\n")]) for x in input]


# Part 1
def part1():
    print("Part 1:", max(summed_totals))


def part2():
    summed_totals.sort(reverse=True)
    top_3_summed_totals = sum(summed_totals[:3])

    # Sum the top 3 summed_totals
    print("Part 2:", top_3_summed_totals)


part1()
part2()
