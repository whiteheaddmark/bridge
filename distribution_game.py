import random

distributions = [
    [4, 3, 3, 3],
    [4, 4, 3, 2],
    [4, 4, 4, 1],
    [5, 3, 3, 2],
    [5, 4, 2, 2],
    [5, 4, 3, 1],
    [5, 4, 4, 0],
    [5, 5, 2, 1],
    [5, 5, 3, 0],
    [6, 3, 3, 1],
    [6, 3, 2, 2],
    [6, 4, 2, 1],
    [6, 4, 3, 0],
    [6, 5, 1, 1],
    [6, 5, 2, 0],
    [6, 6, 1, 0],
    [7, 6, 0, 0],
    [7, 5, 1, 0],
    [7, 4, 2, 0],
    [7, 4, 1, 1],
    [7, 3, 3, 0],
    [7, 3, 2, 1],
    [7, 2, 2, 2],
]


def main():

    random.seed()

    while distributions:

        distribution = random.choice(distributions)
        distributions.remove(distribution)

        random.shuffle(distribution)

        print(
            "{} {} {}".format(distribution[0], distribution[1], distribution[2]),
            end=" ",
        )

        answer_text = input()
        answer_text = answer_text.strip()
        if answer_text.isdigit():
            answer = int(answer_text)
            if answer != distribution[3]:
                print("X, {0}".format(distribution[3]))
        else:
            break

    print("bye.")


if __name__ == "__main__":
    main()
