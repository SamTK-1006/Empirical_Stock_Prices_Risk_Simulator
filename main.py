from functools import partial

import Phase_1_Empirical_Time_Series as P1
import Phase_2_Distribution as P2
import Phase_3_Monte_Carlo as P3


def choose(title, options):
    # Shows a numbered menu and returns the chosen option's name (number or name accepted)
    names = list(options)
    menu = "\n".join(f" {i}. {name}" for i, name in enumerate(names, 1))
    answer = input(f"{title} \n{menu}\nEnter your choice (1-{len(names)}): ").strip().lower()

    if answer.isdigit() and 1 <= int(answer) <= len(names):
        return names[int(answer) - 1]
    for name in names:
        if answer == name.lower():
            return name
    print("Invalid choice. Please enter a valid option.")
    return None


def run_menu(title, options, data):
    choice = choose(title, options)
    if choice:
        options[choice](data)


DISTRIBUTION_OPTIONS = {
    "Normal Distribution Overlay": P2.distribution_ticker,
    "Q-Q Plot": P2.generate_qq,
}

MONTE_CARLO_OPTIONS = {
    "Geometric Brownian Motion (GBM)": partial(P3.Monte_Carlo_Simulations, model=P3.GBM_Simulator),
    "Standard": partial(P3.Monte_Carlo_Simulations, model=P3.Standard_Simulator),
    "Bootstrapping": partial(P3.Monte_Carlo_Simulations, model=P3.Bootstrapping_Simulator),
    "Comparison of Models": P3.Comparison_of_Models,
}

MAIN_OPTIONS = {
    "Time Series Analysis": P1.time_series,
    "Distribution Analysis": partial(run_menu, "Choose distribution analysis type:", DISTRIBUTION_OPTIONS),
    "Monte Carlo Simulations": partial(run_menu, "Choose simulation type:", MONTE_CARLO_OPTIONS),
    "Exit": None,
}


def main():
    print("Empirical Time Series Analysis")
    data = P1.load_data()
    if data is None:
        return

    while True:
        choice = choose("What would you like to view?", MAIN_OPTIONS)
        if choice == "Exit":
            print("Exiting...")
            break
        if choice:
            MAIN_OPTIONS[choice](data)


if __name__ == "__main__":
    main()
