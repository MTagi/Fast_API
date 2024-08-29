import random


def play(switch):
    # Dat chiec o to dang sau ngau nhien 1 trong 3 canh cua
    doors = ['Xe', 'De', 'De']
    random.shuffle(doors)

    # Nguoi choi chon canh cua lan dau tien
    choose = random.choice([0, 1, 2])
    print('Nguoi choi chon canh cua {}.'.format(choose))

    # Nguoi dan chuong trinh mo 1 trong 2 canh cua chua duoc chon chua De
    show = random.choice([x for x in [0, 1, 2] if x != choose and doors[x] == 'De'])
    print('Nguoi dan chuong trinh mo canh cua thu {} chua De.'.format(show))

    if switch:
        # Nguoi choi chon canh cua khac
        choose = [x for x in [0, 1, 2] if x not in [choose, show]][0]
        print('Nguoi choi se thay doi quyet dinh va chon canh cua {}.'.format(choose))
    else:
        # Nguoi choi khong thay doi quyet dinh
        print('Nguoi choi van giu nguyen canh cua {}.'.format(choose))

    # Nguoi dan chuong trinh mo canh cua duoc chon va cong bo ket qua
    print('Canh cua {} co {}.'.format(choose, doors[choose]))
    win = doors[choose] == 'Xe'
    print('Nguoi choi {}'.format('CHIEN THANG!' if win else 'THUA CUOC!'))
    print()
    return win


if __name__ == '__main__':
    games = 1001 # So lan choi game
    wins_with_switch = 0 # So lan thang neu thay doi lua chon
    wins_without_switch = 0 # So lan thang neu khong thay doi lua chon


    # Truong hop 1: Nguoi choi khong bao gio thay doi lua chon
    print('Truong hop 1: Nguoi choi khong thay doi lua chon')
    print()
    wins = 0
    for i in range(games):
        print("Lan choi chu {}".format(i))
        if play(False):
            wins_without_switch += 1
    print()

    # Truong hop 2: Nguoi choi luon thay doi lua chon
    print('Truong hop 2: Nguoi choi luon thay doi lua chon')
    print()
    wins = 0
    for i in range(games):
        print("Lan choi chu {}".format(i))
        if play(True):
            wins_with_switch += 1
    print()

    print("Truong hop 1: Nguoi choi KHONG thay doi lua chon", end = "\n\n")
    print("So lan trung giai: {}".format(wins_without_switch))
    print('Ti le chien thang: {:.2f}'.format(wins_without_switch / games))
    print()
    print("Truong hop 2: Nguoi choi CO thay doi lua chon", end = "\n\n")
    print("So lan trung giai: {}".format(wins_with_switch))
    print('Ti le chien thang: {:.2f}'.format(wins_with_switch / games))