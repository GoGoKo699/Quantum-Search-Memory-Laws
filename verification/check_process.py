"""Exact finite checks of the paired process and the phase certificate."""

from fractions import Fraction
from itertools import product


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def run():
    dilution_cases = 0
    for eta in map(Fraction, ["0", "1/100", "1/8", "1/4", "1/2"]):
        weight = 1 / (2 * (1 - eta))
        actual = {
            (0, 0): 1 - weight + weight * eta**2,
            (0, 1): weight * eta * (1 - eta),
            (1, 0): weight * eta * (1 - eta),
            (1, 1): weight * (1 - eta)**2,
        }
        expected = {bits: (1 - eta) / 2 if bits[0] == bits[1]
                    else eta / 2 for bits in actual}
        require(actual == expected, "IID dilution did not reproduce the pair law")
        require(sum(actual.values()) == 1, "Pair law is not normalized")
        dilution_cases += 1

    innovation_cases = 0
    for delta in map(Fraction, ["0", "1/10", "1/2", "9/10", "1"]):
        law = {bits: Fraction(0) for bits in product([0, 1], repeat=2)}
        for initial, z1, z2, z3 in product([0, 1], repeat=4):
            probability = Fraction(1, 2)
            for z in (z1, z2, z3):
                probability *= delta if z else 1 - delta
            bits = [initial]
            for z in (z1, z2, z3):
                bits.append(bits[-1] ^ z)
            pair = (bits[0] ^ bits[1], bits[2] ^ bits[3])
            require(pair == (z1, z3), "Pair parity is not its odd innovation")
            law[pair] += probability
        for pair, probability in law.items():
            expected = Fraction(1)
            for bit in pair:
                expected *= delta if bit else 1 - delta
            require(probability == expected, "Two logical activations are not independent")
        innovation_cases += 1

    verifier_cases = 0
    for size in range(3, 9):
        for candidate in range(size):
            references = [j for j in range(size) if j != candidate][:2]
            for marked in [None, *range(size)]:
                for activation in product([0, 1], repeat=2):
                    minus = [bool(active and ((candidate == marked) != (reference == marked)))
                             for reference, active in zip(references, activation)]
                    accepts = all(minus)
                    require(not accepts or candidate == marked, "False phase certificate")
                    if candidate == marked:
                        require(accepts == all(activation), "True-candidate activation rule failed")
                    verifier_cases += 1

    return {
        "passed": True,
        "arithmetic": "exact rational and Boolean",
        "paired_dilution_parameters": dilution_cases,
        "two_pair_innovation_parameters": innovation_cases,
        "phase_certificate_cases": verifier_cases,
        "certificate_N_range": [3, 8],
    }
