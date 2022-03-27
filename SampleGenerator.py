from ZipfGenerator import ZipfGenerator
import random


def get_random_distributed_sample(number_of_elements, sample_size):
    samples = []
    for i in range(sample_size):
        samples.append(random.randint(0, number_of_elements-1))
    return samples


def get_zipf_distributed_sample(number_of_elements, exponent, sample_size):
    zipf_generator = ZipfGenerator(number_of_elements, exponent)
    return zipf_generator.generate_sample(sample_size)
