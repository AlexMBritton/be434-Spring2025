import argparse

def count_bases(dna_sequence):
    """Count the occurrences of each base (A, C, G, T) in the given DNA sequence."""
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in dna_sequence:
        if base in counts:
            counts[base] += 1
    return counts["A"], counts["C"], counts["G"], counts["T"]

def main():
    parser = argparse.ArgumentParser(
        description="Tetranucleotide frequency"
    )
    parser.add_argument("DNA", help="Input DNA sequence")
    args = parser.parse_args()

    a, c, g, t = count_bases(args.DNA)
    print(a, c, g, t)

if __name__ == "__main__":
    main()