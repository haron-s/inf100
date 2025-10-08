import random


def main():
    '''
    This program runs multiple simulations of the following scenario:
    A pack of football cards is bought until the entire set of possible
    cards is collected. The recorded output of a single simulation is
    how many packs was bought.

    This function runs multiple simulations, and reports the average
    and (simplified) quartiles of the simulation outputs.
    '''

    K = 409  # possible cards to collect
    P = 8  # number of cards in each pack
    TRAILS = 100  # number of simulations to run
    
    sim_results = repeated_simulations(TRAILS, K, P)
    sim_results.sort()

    mean = sum(sim_results) / len(sim_results)
    q1 = sim_results[1 * TRAILS // 4]
    q2 = sim_results[2 * TRAILS // 4]  # (median)
    q3 = sim_results[3 * TRAILS // 4]

    print('Simulation average:', mean)
    print('Simulation quartiles:', q1, q2, q3)


def repeated_simulations(trails, k, p):
    '''
    Runs the simulation `trails` number of times. The returned value
    is a list of results, one from each run of the simulations.
    '''
    results = []
    for _ in range(trails):
        result = simulate(k, p)
        results.append(result)
    return results


def simulate(k, p):
    '''
    Simulate buying football card packs with p cards in each pack until
    the entire set of k unique football cards is collected.
    '''
    collection = []
    pack_count = 0
    while len(collection) < k:
        pack = get_pack_of_cards(k, p)
        pack_count += 1
        insert_pack_into_collection(collection, pack)
    return pack_count


def insert_pack_into_collection(collection, pack):
    '''
    Given a collection and a pack of new cards, this function 
    will destructively insert the new cards into the collection,
    unless they are already there (in which case they are ignored)
    '''
    for card in pack:
        if card not in collection:
            collection.append(card)


def get_pack_of_cards(k, p):
    '''
    Get a random list of p cards. Each card is a number between 1 and k
    selected uniformly at random with replacement.
    '''
    cards = []
    for _ in range(p):
        card = random.randrange(1, k + 1)
        cards.append(card)
    return cards


if __name__ == '__main__':
    main()