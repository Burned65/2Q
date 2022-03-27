from caches import FIFO
from caches import LRU
from caches import TwoQ
import csv


def get_configured_caches(size, k_in):
    k_out = size//2
    am_size = size - (k_in + k_out)

    fifo = FIFO.FIFO(size)
    lru = LRU.LRU(size)
    two_queue = TwoQ.TwoQ(k_in, k_out, am_size)

    return [fifo, lru, two_queue]


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
        k_in = 1

        caches = get_configured_caches(size, k_in)
        cache_hit_ratios = get_hit_ratios(samples, caches)
        results.append([float(size)] + cache_hit_ratios)
    headers = ["buffer-size", "fifo", "lru", "2Q"]
    print_samples_to_csv(results, file_name, headers)


def print_samples_to_csv(results, file_name, headers):
    with open("CSVFiles/" + file_name + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for item in results:
            writer.writerow(item)
