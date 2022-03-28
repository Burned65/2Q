from caches import FIFO
from caches import LRU
from caches import TwoQ
from caches import SimplifiedTwoQ
import csv


def get_configured_caches(size, k_in):
    k_out = size//2
    am_size = size - (k_in + k_out)
    k_a1 = size//3
    k_a2 = size//4

    fifo = FIFO.FIFO(size)
    lru = LRU.LRU(size)
    two_queue = TwoQ.TwoQ(k_in, k_out, am_size)
    simplified_two_queue_1_3 = SimplifiedTwoQ.SimplifiedTwoQ(size-k_a1, k_a1)
    simplified_two_queue_1_2 = SimplifiedTwoQ.SimplifiedTwoQ(size-k_out, k_out)
    simplified_two_queue_1_4 = SimplifiedTwoQ.SimplifiedTwoQ(size-k_a2, k_a2)

    return [fifo, lru, two_queue, simplified_two_queue_1_3, simplified_two_queue_1_2, simplified_two_queue_1_4]


def get_cache_hit_ratio(sample, cache):
    cache_hits = 0
    for element in sample:
        if cache.cache(element) is True:
            cache_hits += 1
    return cache_hits / len(sample)


def get_hit_ratios(samples, caches):
    ratios = []

    for item in caches:
        ratios.append(get_cache_hit_ratio(samples, item))
    return ratios


def experiments_to_csv(samples, file_name):
    db_size = 50000

    results = []

    for i in range(5, 41, 5):
        size = int(((i/100)*db_size))

        caches = get_configured_caches(size, 1)
        cache_hit_ratios = get_hit_ratios(samples, caches)
        results.append([float(size)] + cache_hit_ratios)
    headers = ["buffer-size", "fifo", "lru", "2Q", "simplified2Q13", "simplified2q12", "simplified2q14"]
    print_samples_to_csv(results, file_name, headers)


def print_samples_to_csv(results, file_name, headers):
    with open("CSVFiles/" + file_name + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for item in results:
            writer.writerow(item)
