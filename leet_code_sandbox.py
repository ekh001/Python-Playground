"""
Return the starting indices of all the concatenated substrings ('words') in a given string 's'. You can return the answer in any order.
"""

s = "barfoothefoobarman"
words = ["foo","bar"]

# Note: So I did end up looking up a solution, but I have a general understanding of it and tried to explain it myself. #3 and #4 are pretty confusing, though!
def findSubstring(s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # Set yourself up an empty list to store the permutations: 
        indices = []

        # -------------------------------------- 1. Put all the words in a dictionary.
        # Empty dictionary for all the words in the 'words' list.        
        word_count = dict()
        # For loop that stores the count of each word in 'words'. It will add each word to the dictionary (else statement), but if there is a repeated word, it will just increase the value by one.
        for a in range(len(words)):
            if words[a] in word_count:
                word_count[words[a]] += 1
            else:
                word_count[words[a]] = 1
                
        #-------------------------------------- 2. Get the length of your permutation:
        #  Find the length of the first word in the array, because they're all the same length so it will tell you all the words' lengths:
        length_of_words = len(words[0])
        # Multiply by the NUMBER of words to find the length of the permutation you're looking for:
        length_of_substring = length_of_words * len(words)

        #-------------------------------------- 3. Write a loop that will go through every character in the 's' string:
        for a in range(0, len(s) - length_of_substring + 1):
            # (This means that it takes the length of the string, subtracts the length of the permutation, + 1 to that, and uses that number in a range from index 0)
            # Fetch the input string:  (***** This is where it gets hairy for me, and I don't get it....)

            current_string = s[a:a + length_of_substring]
            # Put the word count in a dictionary
            word_map = dict()
            # index to 0 so it loops through the given list
            index = 0
            # index to partition the current string 
            j = 0


        #-------------------------------------- 4. Make my while loop that actually goes through the words: (I think I get it)
            while index < len(words):
                part = current_string[j: j + length_of_words]    
                if part in word_map:
                    word_map[part] += 1
                else:
                    word_map[part] = 1

                # Update your index: (Okay, back in business with the understanding)
                j += length_of_words
                index += 1
            
            #-------------------------------------- 5.  Compare your dictionaries:
            if word_map == word_count:
                indices.append(a)

        return indices

print(findSubstring(s, words))
