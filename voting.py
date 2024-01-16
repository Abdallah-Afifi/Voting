def check_voting_eligibility(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("Sorry, you are not eligible to vote yet.")

def main():
    try:
        age = int(input("Enter your age: "))
        check_voting_eligibility(age)
    except ValueError:
        print("Invalid input. Please enter a valid age as a number.")

if __name__ == "__main__":
    main()
