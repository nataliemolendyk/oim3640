## Date: 2025-02-24

**What I asked AI to do:**
I asked AI to explain why my value for the bill wasn't printing even though I included the print function.

**What I didn't understand in the generated code:**
I was confused why return was used instead of print for the tax_bill and bill. I then looked back in past practice problems/notes and realized that the values didn't need to be printed, they just needed to be saved for future calculations.

**What I learned:**
I learned that I can't put the value that I want to be called before other parts of the function, I have to wait until the end for everything to be printed all together. I learned that it was better to use a return function in the function and the print function at the end because the values in the function just need to be saved, not printed. I also learned that an f-string is needed for printing strings that include variables. I thought that the I only needed to include brackets.

## Date: 2025-03-01

**What I asked AI to do:**
I asked AI to critique my proposal and then used the proposal with the given suggestions to create a plan with the help of the chatbot in VS Code. After, the chatbot generated code to create the bill calcultor based on the plan from previously.

**What I didn't understand in the generated code:**
I was confused what some of the lines of code meant. For example, I didn't understand what the enumerate function did. The chatbot explained to me that it will count the states and number each state based on alphabetical order. I was confused what rounded.index(max(rounded)) was and it gives you the index of the person with the highest share of the bill. if __name__ == "__main__": checks if the file is being executed directly or imported as a module.

**What I learned:**
I learned that I need to be more specific about what I should include in my calculator and what the problem I am actually trying to solve is. The chatbot helped me make my proposal more focused and personalized by clarifying features in the calculator to differentiate it from other calculators.

## Date: 2025-03-05

**What I asked AI to do:**
I asked AI to explain lines in the code that I didn't understand and I went through each line that I didn't understand so I would get a better understanding of what each line is doing.

**What I didn't understand in the generated code:**
I was confused with the function .keys. The chatbot told me that the function extracts the keys which are the abbreviations of each state. I asked what print(f"  {len(STATE_TAXES) + 1}. Enter custom tax rate manually") did and I learned that it takes the amount of numbered states and add it by 1 to get the next numbered option in the list to be Enter custom tax rate manually. I then had the chatbot explain the entire def get_tax_rate() function and I learned that choice = input("Enter choice (number): ").strip() gets the user's input and converts it into a string wihout the whitespaces. 

**What I learned:**
I learned that we use choice - 1 because the lists start at 0 but the menu of states starts at 1. Costs = [] creates an empty list under the variable name of costs. append(cost) adds the next cost to the end of the list. print("\n" + "=" * 60) prints a blank line with 60 spaces to create division between the calculations the summary breakdown. The chatbot explained that ${pretax_total:.2f}") gives two decimal points with the .2f. I learned that zip takes multiple lists, in this case, and pairs the corresponding elements together.

