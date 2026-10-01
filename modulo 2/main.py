""" Este desafio consiste en implementar una funcion que use una
pila para verificar si una expresion tiene caracteres balanceados."""

from stack import Stack


def balanced_character_checker(expression):

    stack = Stack()

    pairs = {')' : '(', ']' : '[', '}' : '{'}


    for char in expression:
        if char in pairs.values():
            stack.push(char)

        elif char in pairs:
            if stack.is_empty():
                return False

            if stack.pop() != pairs[char]:
                return False

        else:
            return False
            

    return stack.is_empty()

def main():
    print("Character Checker")

    result = balanced_character_checker("([{])")
    print(f"Balanced: {result}")

    return


if __name__ == "__main__":
    main()