import numpy as np
from typing import Union


def bin2dec(bin: np.ndarray) -> Union[np.int_, np.ndarray]:
    return bin.dot(1 << np.arange(bin.shape[-1] - 1, -1, -1))


def find_rating(arr: np.ndarray, type: str) -> np.int_:
    rating = np.copy(arr)
    for i in range(0, rating.shape[-1]):
        if type == "oxy":
            common_bin = rating.sum(axis=0) // round(len(rating) / 2)
        elif type == "co2":
            common_bin = 1 - (rating.sum(axis=0) // round(len(rating) / 2))
        rating = rating[rating[:,i] == common_bin[i]]
        if len(rating) == 1:
            return bin2dec(rating[0])


def main():
    # load input
    input = np.genfromtxt("input", dtype=int, delimiter=1)

    # begin part 1
    summation = input.sum(axis=0)

    gamma_bin = summation // int(len(input) / 2)
    epsilon_bin = 1 - gamma_bin

    gamma = bin2dec(gamma_bin)
    epsilon = bin2dec(epsilon_bin)

    print(f"Power consumption: {gamma * epsilon}")
    # end part 1

    # begin part 2
    oxy_gen = find_rating(input, "oxy")
    co2_scrub = find_rating(input, "co2")

    print(f"Life support rating: {oxy_gen * co2_scrub}")


if __name__ == "__main__":
    main()
