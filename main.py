from jokes import search
from categories import CATEGORIES

def main():
    print("Welcome to the Random Joke Generator!\n")
    print("Categories available: general, programming, dark, pun, spooky, misc\n")

    category = input("Enter a joke category (or leave blank for a random category): ").capitalize()

        # Validate the category
    if not category or category.lower() not in VALID_CATEGORIES:
        print("Invalid or empty category! Defaulting to a random joke.")
        category = "Any"

        # Fetch and display the joke
        joke = search(category)
        print("\nHere's your joke:")
        print(joke)

    if __name__ == "__main__":
        main()
