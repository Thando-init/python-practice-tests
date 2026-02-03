import re

class AssessmentTwo:

    # ===== BASIC =====

    def count_negative_numbers(self, numbers):
        """Return the number of negative values in the list."""
        negatives = len([num for num in numbers if num < 0])
        return negatives

    def average(self, numbers):
        """Return the average of numbers or None if list is empty."""
        if not numbers:
            return None
        
        avrg = sum(numbers)/len(numbers)
        return avrg

    def first_and_last(self, items):
        """Return a tuple of (first, last) item or None if list is empty."""
        if not items:
            return None
        
        f_l = (items[0], items[-1])
        return f_l

    def count_consonants(self, text):
        """Return the number of consonants in the string (letters only)."""
        text = text.lower()
        only_letters = re.sub(r'[^a-zA-z]', "", text)
        consonants = re.sub(r'[aeiou]', "", only_letters)

        # consonants = [char for char in text.lower() if char.isalpha() and char not in "aeiou"]
        return len(consonants)

    def is_even_length(self, text):
        """Return True if the string length is even."""
        return len(text) % 2 == 0
    
    # ===== INTERMEDIATE =====

    def remove_duplicates_preserve_order(self, numbers):
        """Remove duplicates while preserving order."""
        if not numbers:
            return []
        
        return list(set(numbers))

    def word_lengths(self, sentence):
        """Return a dictionary mapping each word to its length."""
        my_dict = {}
        sentence_list = sentence.strip().split() #into a list

        for word in sentence_list:
            my_dict[word] = len(word)
        return my_dict


    def second_largest(self, numbers):
        """Return the second largest number or None if it doesn't exist."""
        if not numbers or len(numbers) < 2:
            return None
        
        sorted_list = sorted(numbers)
        return sorted_list[-2]

    def chunk_list(self, numbers, size):
        """Split list into chunks of given size."""
        result = []

        for i in range(0, len(numbers), size):
            chunk = numbers[i:i+size]
            result.append(chunk)
        return result
        

    def is_anagram(self, s1, s2):
        """Return True if the two strings are anagrams (ignore case & spaces)."""
        return sorted(set(s1)) == sorted(set(s2))


    # ===== ADVANCED =====

    def running_sum(self, numbers, total = 0):
        """Return a list of running sums."""
        if not numbers:
            return []
        
        new_total = total + numbers[0] #start the sum(1st one)

        return [new_total] + self.running_sum(numbers[1:], new_total)
    
    # def running_sum(self, numbers):
    #     """Return a list of running sums."""
    #     if not numbers:
    #         return []
        
    #     run_sum = []
    #     current_sum = 0
    #     for num in numbers:
    #         current_sum += num
    #         run_sum.append(current_sum)
    #     return run_sum


    def longest_unique_substring(self, text: str) -> int:
        """Return the length of the longest substring without repeating characters."""
        if not text:
            return 0  # empty string -> 0

        # sliding window + last seen index map
        last_seen = {}
        longest = 0
        left = 0

        for right, char in enumerate(text):
            if char in last_seen and last_seen[char] >= left:
                # move left to right after last occurrence
                left = last_seen[char] + 1

            # update last seen position
            last_seen[char] = right

            # calculate window length
            window_length = right - left + 1

            # update longest if bigger
            if window_length > longest:
                longest = window_length

        return longest

            

    def rotate_matrix_90(self, matrix):
        """Rotate a square matrix 90 degrees clockwise."""
        pass

    def validate_palindrome_number(self, n):
        """Return True if integer n is a palindrome."""
        if n < 0 :
            return False
        
        original = n
        reversed = 0

        while n > 0:
            digit = n % 10
            reversed *= 10 + digit

            n = n // 10 #update n

        return original == reversed


    def generate_pascal_row(self, n):
        """Return the nth row of Pascal's Triangle (0-indexed)."""
        pass
