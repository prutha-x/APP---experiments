def knapsack_bottom_up(item_weights, item_profits, max_capacity):
    item_count = len(item_weights)

    dp_table = [[0] * (max_capacity + 1)
                for _ in range(item_count + 1)]

    for item_index in range(1, item_count + 1):
        for current_capacity in range(max_capacity + 1):

            if item_weights[item_index - 1] <= current_capacity:
                include_item = (
                    item_profits[item_index - 1]
                    + dp_table[item_index - 1]
                    [current_capacity - item_weights[item_index - 1]]
                )

                exclude_item = dp_table[item_index - 1][current_capacity]

                dp_table[item_index][current_capacity] = max(
                    include_item, exclude_item
                )

            else:
                dp_table[item_index][current_capacity] = (
                    dp_table[item_index - 1][current_capacity]
                )

    return dp_table[item_count][max_capacity]


def knapsack_top_down(item_weights, item_profits, item_count, max_capacity, dp_table):

    if item_count == 0 or max_capacity == 0:
        return 0

    if dp_table[item_count][max_capacity] != -1:
        return dp_table[item_count][max_capacity]

    current_weight = item_weights[item_count - 1]
    current_profit = item_profits[item_count - 1]

    if current_weight <= max_capacity:

        include_item = current_profit + knapsack_top_down(
            item_weights,
            item_profits,
            item_count - 1,
            max_capacity - current_weight,
            dp_table
        )

        exclude_item = knapsack_top_down(
            item_weights,
            item_profits,
            item_count - 1,
            max_capacity,
            dp_table
        )

        dp_table[item_count][max_capacity] = max(
            include_item, exclude_item
        )

    else:
        dp_table[item_count][max_capacity] = knapsack_top_down(
            item_weights,
            item_profits,
            item_count - 1,
            max_capacity,
            dp_table
        )

    return dp_table[item_count][max_capacity]


item_weights = [4, 5, 1]
item_profits = [1, 2, 3]
max_capacity = 4

item_count = len(item_weights)

bottom_up_result = knapsack_bottom_up(
    item_weights, item_profits, max_capacity
)

top_down_table = [
    [-1] * (max_capacity + 1)
    for _ in range(item_count + 1)
]

top_down_result = knapsack_top_down(
    item_weights,
    item_profits,
    item_count,
    max_capacity,
    top_down_table
)

print("Bottom-Up Maximum Profit:", bottom_up_result)
print("Top-Down Maximum Profit:", top_down_result)
