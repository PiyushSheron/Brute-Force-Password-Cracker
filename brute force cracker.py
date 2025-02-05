import hashlib
import itertools
import time
import threading

# Function to attempt password cracking using brute force with multi-threading
def brute_force_worker(hash_to_crack, char_set, length, result):
    for guess in itertools.product(char_set, repeat=length):
        guess_password = ''.join(guess)
        hashed_guess = hashlib.md5(guess_password.encode()).hexdigest()
        
        if hashed_guess == hash_to_crack:
            result.append(guess_password)
            return

def brute_force_crack(hash_to_crack, char_set, max_length):
    start_time = time.time()
    result = []
    threads = []
    
    for length in range(1, max_length + 1):
        thread = threading.Thread(target=brute_force_worker, args=(hash_to_crack, char_set, length, result))
        threads.append(thread)
        thread.start()
        
        for thread in threads:
            thread.join()
            if result:
                break
        
        if result:
            break
    
    if result:
        end_time = time.time()
        print(f"[+] Password found: {result[0]}")
        print(f"[+] Time taken: {end_time - start_time:.2f} seconds")
    else:
        print("[-] Password not found within the given constraints.")

if __name__ == "__main__":
    hash_to_crack = input("Enter MD5 hash to crack: ")
    char_set = "abcdefghijklmnopqrstuvwxyz0123456789"  # Character set to use
    max_length = int(input("Enter maximum password length: "))
    
    brute_force_crack(hash_to_crack, char_set, max_length)
