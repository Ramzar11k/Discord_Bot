import random

class HangMan():
    def __init__(self, word, difficulty = 0.6, lives = 3):
        self.fullWord = list(word)
        self.puzzleWord = list(word)
        self.difficulty = difficulty
        self.lives = lives
        self.lettersToDeduct = round(len(self.puzzleWord) * self.difficulty)
        self.lettersToDeductIndex = set([])
        self.letterToGuess = []
        while len(self.lettersToDeductIndex) < self.lettersToDeduct:
            _ = random.randint(0,len(self.fullWord)-1)
            self.lettersToDeductIndex.add(_)
        for i in self.lettersToDeductIndex:
            if self.fullWord[i] not in self.letterToGuess:
                self.letterToGuess.append(self.fullWord[i])
            self.puzzleWord[i] = "-"

        print(' '.join(self.puzzleWord))

    def guessLetter(self, letter):
        if letter in self.letterToGuess:
            index = 0
            for i in self.fullWord:
                if i == letter:
                    self.puzzleWord[index] = letter
                index += 1
            self.letterToGuess.remove(letter)
            msg = " ".join(self.puzzleWord)
        else:
            self.lives -= 1
            msg = "{0} is not part of the word, you have {1} lives left!".format(letter, self.lives)
            print(self.lives)
        return msg
        print(' '.join(self.puzzleWord))


class Riddle():
    def __init__(self, question, answer, hint):
        self.question = question
        self.answer = answer
        self.hint = hint


par = Riddle("?", "!", "???")
print(par.answer)
