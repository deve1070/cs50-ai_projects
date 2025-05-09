from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
A_statement=And(AKnight,AKnave)
knowledge0 = And(
    Not(And(AKnave ,AKnight)),
    Or(AKnave,AKnight),
    Implication(AKnight,A_statement),
    Implication(AKnave,Not(A_statement))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_statement1=And(AKnave,BKnave)
knowledge1 = And(
    Not(And(AKnave ,AKnight)),
    Or(AKnave,AKnight),
    Implication(AKnight,A_statement1),
    Implication(AKnave,Not(A_statement1)),
    Not(And(BKnave ,BKnight)),
    Or(BKnave,BKnight),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_statement2=Or(And(AKnave,BKnave),And(AKnight,BKnight))
B_statement=Or(And(AKnave,BKnight),And(AKnight,BKnave))
knowledge2 = And(
     Not(And(AKnave ,AKnight)),
    Or(AKnave,AKnight),
    Implication(AKnight,A_statement2),
    Implication(AKnave,Not(A_statement2)),
    Not(And(BKnave ,BKnight)),
    Or(BKnave,BKnight),
    Implication(BKnight,B_statement),
    Implication(BKnave,Not(B_statement)),
)
    


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A_statement3=Or(AKnave,AKnight)
B_statement1=CKnave

C_statement=AKnight
knowledge3 = And(
    Not(And(AKnave ,AKnight)),
    Or(AKnave,AKnight),
    Implication(AKnight,A_statement2),
    Implication(AKnave,Not(A_statement2)),
    Not(And(BKnave ,BKnight)),
    Or(BKnave,BKnight),
    Implication(BKnight,B_statement),
    Implication(BKnave,Not(B_statement)),
    Not(And(CKnave,CKnight)),
    Or(CKnight,CKnave),
    Implication(CKnight,C_statement),
    Implication(CKnave,Not(C_statement)),


)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
