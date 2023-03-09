from dependencies.thread import Thread
from dependencies.common import join
from decoding.scytale import scytale
from decoding.caesar import caesar

CIPHERS = [scytale, caesar]


def decode(text):
    cipher_threads = [Thread(cipher, text) for cipher in CIPHERS]

    # Start all threads
    for t in cipher_threads:
        t.start()

    # Wait for all threads and get the result
    possible_decodings = join([t.join() for t in cipher_threads])
    possible_decodings.sort(key=lambda x: x[1], reverse=True)
    return possible_decodings


if __name__ == '__main__':
    text = input("Enter a text to decode: ")

    decoding = decode(text)

    if not decoding:
        print("We need one more try...")
        decoding = decode(text)

    print(f'The most probable decoding is "{decoding[0][0]}"')

    if decoding[1:]:
        print(f"Other decodings: {decoding[1:]}")
