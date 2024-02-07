def main():
    month = months()
    checking(month)


def months():
    birthdates = []

    with open('astronauts.csv', 'r') as file:
        for line in file:
            fields = line.strip().split(',')
            birthdates.append(fields[4])

    monthlist = []

    for birthdate in birthdates:
        date = birthdate.strip().split('/')
        month = date[0]
        monthlist.append(month)
    return monthlist


def checking(monthlist):
    repeat = 1
    appearances = []

    for y in range(12):
        number = monthlist.count(str(repeat))
        appearances.append(number)
        repeat += 1
    x = 1
    for a in range(3):
        index = appearances.index(max(appearances))
        print(
            f'A(z) {x}. leggyakoribb születési hónap a(z) '
            f'{index}. {(max(appearances) / (len(monthlist) - 1) * 100):.1f}%-al')
        appearances[index] = 0
        x += 1


main()
