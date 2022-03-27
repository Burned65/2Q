import random

import SampleGenerator
import CacheTester
from threading import Thread
from caches import TwoQ

if __name__ == '__main__':
    number_of_possible_pages = 50000
    sample_size = 1000000

    random_sample = SampleGenerator.get_random_distributed_sample(number_of_possible_pages, sample_size)
    zipf_05_sample = SampleGenerator.get_zipf_distributed_sample(number_of_possible_pages, 0.5, sample_size)
    zipf_086_sample = SampleGenerator.get_zipf_distributed_sample(number_of_possible_pages, 0.86, sample_size)

    CacheTester.experiments_to_csv(random_sample, "random")
    CacheTester.experiments_to_csv(zipf_05_sample, "zipf05")
    CacheTester.experiments_to_csv(zipf_086_sample, "zipf086")
