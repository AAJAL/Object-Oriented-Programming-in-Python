from random import shuffle

class Deck:

    def __init__(self):
        self.__deck = [x for x in range(52)]
        self.__suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.__ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", 
        "9", "10", "Jack", "Queen", "King"]
        shuffle(self.__deck)

    def generateCards(self):
        self.__displayCardList = []
        for i in range(4):
            self.__suit = self.__suits[self.__deck[i] // 13]
            self.__rank = self.__ranks[self.__deck[i] % 13]
            self.__displayCardList.append("Card number: "+str(self.__deck[i])+" is the "+self.__rank+" of "+self.__suit)

        return self.__displayCardList

    def __eq__(self, other):
        return self.__displayCardList == other.__displayCardList

    def __str__(self):
        summary = ""
        for card in self.generateCards():
            summary += card + "\n"

        return summary


a = Deck()
b = Deck()

print(a)
print(b)
print(a == b)
