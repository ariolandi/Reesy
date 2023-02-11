from threading import Thread
from dependencies.common import join
from decoding.scytale import scytale
from decoding.caesar import caesar

CIPHERS = [scytale, caesar]


def decode(text):
    # We need muitable object if we want to get access to the results from threading
    def decode_cipher(text, cipher, result):
        for decoding in cipher(text):
            result.append(decoding)

    def thread_control(tread_list, action):
        for t in tread_list:
            action(t)
    
    cipher_results = [(cipher, []) for cipher in CIPHERS]
    cipher_threads = [Thread(target=decode_cipher, args=(text, cipher, result))
                     for (cipher, result) in cipher_results]
    
    # Start all threads
    thread_control(cipher_threads, lambda x: x.start())
    
    # Wait for all threads
    thread_control(cipher_threads, lambda x: x.join())
    
    possible_decodings = join([result for (cipher, result) in cipher_results])
    possible_decodings.sort(key = lambda x: x[1])
    return possible_decodings


if __name__ == '__main__':
    text = "WLORELADTRDETRSTAGOUS_THDE\
SNEENT_EEOCIGISDA_LWURNUTNEN_"
    
    # print(decode(text))
    scytale(text)

