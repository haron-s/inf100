from pathlib import Path

def best_alignment(genome, sequence):
    difference_dict = {
        i: alignment_difference(genome, sequence, i)
        for i in range(len(genome) - len(sequence) + 1)
    }
    return min(difference_dict, key=difference_dict.get)

def best_alignment_to_file(path, sequence):
    return best_alignment(Path(path).read_text(encoding="utf-8"), sequence)

def alignment_difference(genome, sequence, i):
    return sum(genome[i + j] != sequence[j] for j in range(len(sequence)))

def test_best_alignment():
    print('Testing best_alignment...', end='')
    genome = 'AAACACCCCCGGGGGTGTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    sequence = 'ACACCCCCGGGGATGT'
    assert 2 == best_alignment(genome, sequence)

    genome = 'AAAAAAAAAAAAAAAAACACCCCCGGGGGTGTTTTTTTTTTTTTT'
    sequence =                     'CCGGGGATGT'
    assert 22 == best_alignment(genome, sequence)

    genome = 'TTTAAG'
    sequence = 'AAGT'
    assert 2 == best_alignment(genome, sequence)
    print(' OK')

def test_best_alignment_to_file():
    print('Testing best_alignment_to_file...', end='')
    path = 'human_genome_excerpt.txt'
    assert 30864 == best_alignment_to_file(path, 'AAACAAAGAA')
    assert 2097 == best_alignment_to_file(path, 'GAGTGGGATGAGCCATTGTTCATCT')
    assert 0 == best_alignment_to_file(path, 'TAACCC' * 18)
    assert 49913 == best_alignment_to_file(path, 'CATTTCAGTAGTAATAGGAATCTCCAC')
    print(' OK')

test_best_alignment()
test_best_alignment_to_file()