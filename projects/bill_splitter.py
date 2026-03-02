"""
Bill Splitter with Fairness Feature
Calculates tip, tax, and splits bills proportionally by meal cost.
"""

# State tax rates (percentage)
STATE_TAXES = {
    "CA": 8.625,
    "TX": 8.25,
    "NY": 8.875,
    "IL": 6.25,
    "FL": 6.0,
    "WA": 6.5,
    "CO": 7.65,
    "OR": 0.0,
    "MT": 0.0,
    "NH": 0.0,
}


def display_state_menu():
    """Display available states for tax rate selection."""
    print("\nAvailable states:")
    for i, state in enumerate(sorted(STATE_TAXES.keys()), 1):
        print(f"  {i}. {state}")
    print(f"  {len(STATE_TAXES) + 1}. Enter custom tax rate manually")


def get_tax_rate():
    """Get tax rate from user via state selection or manual entry."""
    while True:
        display_state_menu()
        choice = input("\nEnter choice (number): ").strip()
        
        states_list = sorted(STATE_TAXES.keys())
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(states_list):
                state = states_list[choice - 1]
                rate = STATE_TAXES[state]
                print(f"Selected {state}: {rate}% tax")
                return rate
            elif choice == len(states_list) + 1:
                try:
                    rate = float(input("Enter tax rate (as percentage, e.g., 7.5): "))
                    if rate < 0:
                        print("Tax rate cannot be negative. Try again.")
                        continue
                    print(f"Using custom tax rate: {rate}%")
                    return rate
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
        
        print("Invalid choice. Try again.")


def get_number_of_people():
    """Get number of people splitting the bill."""
    while True:
        try:
            num = int(input("\nHow many people are splitting the bill? "))
            if num < 1:
                print("Must be at least 1 person.")
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_meal_costs(num_people):
    """Get meal cost for each person."""
    costs = []
    print("\nEnter meal cost for each person:")
    for i in range(num_people):
        while True:
            try:
                cost = float(input(f"Person {i + 1} meal cost ($): "))
                if cost < 0:
                    print("Meal cost cannot be negative. Try again.")
                    continue
                costs.append(cost)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    return costs


def get_tip_percentage():
    """Get tip percentage from user."""
    while True:
        try:
            tip = float(input("\nEnter tip percentage (e.g., 20): "))
            if tip < 0:
                print("Tip percentage cannot be negative. Try again.")
                continue
            return tip
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_pretax_total(meal_costs):
    """Calculate total of all meals before tax."""
    return sum(meal_costs)


def calculate_tax_amount(pretax_total, tax_rate):
    """Calculate tax amount based on pretax total and tax rate."""
    return pretax_total * (tax_rate / 100)


def calculate_tip_amount(subtotal_with_tax, tip_percentage):
    """Calculate tip based on subtotal (including tax) and tip percentage."""
    return subtotal_with_tax * (tip_percentage / 100)


def calculate_final_bill(pretax_total, tax_rate, tip_percentage):
    """Calculate final bill total with tax and tip."""
    tax = calculate_tax_amount(pretax_total, tax_rate)
    subtotal_with_tax = pretax_total + tax
    tip = calculate_tip_amount(subtotal_with_tax, tip_percentage)
    final_bill = subtotal_with_tax + tip
    return final_bill, tax, tip


def calculate_proportional_shares(meal_costs, final_bill):
    """Calculate each person's proportional share of the final bill."""
    pretax_total = sum(meal_costs)
    shares = []
    
    for cost in meal_costs:
        proportion = cost / pretax_total
        share = proportion * final_bill
        shares.append(share)
    
    return shares


def round_and_adjust_shares(shares):
    """Round shares to nearest cent, then adjust one person for leftover cents."""
    rounded = [round(share, 2) for share in shares]
    total_rounded = sum(rounded)
    
    # Calculate leftover cents
    leftover = round(total_rounded - sum(shares), 2)
    
    # Find person with highest share to absorb the adjustment
    if leftover != 0:
        max_index = rounded.index(max(rounded))
        rounded[max_index] += leftover
    
    return rounded


def display_breakdown(meal_costs, shares, adjusted_shares, pretax_total, tax_amount, tip_amount, final_bill):
    """Display detailed breakdown including fairness metrics."""
    print("\n" + "=" * 60)
    print("BILL BREAKDOWN")
    print("=" * 60)
    
    print(f"\nSubtotal (meals):     ${pretax_total:.2f}")
    print(f"Tax:                  ${tax_amount:.2f}")
    print(f"Tip:                  ${tip_amount:.2f}")
    print(f"FINAL BILL:           ${final_bill:.2f}")
    
    print("\n" + "-" * 60)
    print("SPLIT BREAKDOWN & FAIRNESS")
    print("-" * 60)
    
    for i, (meal, ideal_share, actual_share) in enumerate(zip(meal_costs, shares, adjusted_shares)):
        difference = actual_share - ideal_share
        difference_sign = "+" if difference > 0 else ""
        
        print(f"\nPerson {i + 1}:")
        print(f"  Meal cost:          ${meal:.2f} ({meal/pretax_total*100:.1f}% of meals)")
        print(f"  Fair share:         ${ideal_share:.2f}")
        print(f"  Pays:               ${actual_share:.2f}")
        print(f"  Fairness delta:     {difference_sign}${difference:.2f} ({difference/ideal_share*100:+.1f}%)")
        
        if difference > 0.01:
            print(f"  ↑ Overpays by ${difference:.2f}")
        elif difference < -0.01:
            print(f"  ↓ Underpays by ${-difference:.2f}")
        else:
            print(f"  ✓ Pays fair share")
    
    print("\n" + "=" * 60)
    print(f"Total checked: ${sum(adjusted_shares):.2f}")
    print("=" * 60)


def run_calculator():
    """Main workflow for bill splitter."""
    print("\n" + "=" * 60)
    print("BILL SPLITTER WITH FAIRNESS FEATURE")
    print("=" * 60)
    
    # Gather inputs
    tax_rate = get_tax_rate()
    num_people = get_number_of_people()
    meal_costs = get_meal_costs(num_people)
    tip_percentage = get_tip_percentage()
    
    # Calculate totals
    pretax_total = calculate_pretax_total(meal_costs)
    final_bill, tax_amount, tip_amount = calculate_final_bill(pretax_total, tax_rate, tip_percentage)
    
    # Calculate splits
    ideal_shares = calculate_proportional_shares(meal_costs, final_bill)
    adjusted_shares = round_and_adjust_shares(ideal_shares)
    
    # Display results
    display_breakdown(meal_costs, ideal_shares, adjusted_shares, pretax_total, tax_amount, tip_amount, final_bill)


def main():
    """Main program loop."""
    while True:
        run_calculator()
        
        again = input("\nCalculate another bill? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThank you for using Bill Splitter! Goodbye.")
            break


if __name__ == "__main__":
    main()
