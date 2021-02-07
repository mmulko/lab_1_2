"""Link"""
def validate_board(player_board: list):
    """
    Main function to check board

    >>> validate_board(["****1****", "*** 2****", "**  3****", "*   4****",\
    "    56781", "        *", "2      **", "      ***", "3 4  ****"])
    False
    """
    if board_row_check(player_board) is False:
        return False
    elif board_row_check(row_to_column_list(player_board)) is False:
        return False
    elif check_colors(player_board) is False:
        return False
    else:
        return True


def board_row_check(board: list):
    """
    This function checks all rows for repeated numbers

    >>> board_row_check(["****1****", "*** 2****", "**  3****", "*   4****",\
    "    56781", "        *", "2      **", "      ***", "3 4  ****"])
    True
    """
    for num in range(len(board)):
        row = board[num]
        r_list = list(row)
        if row_check(r_list) is False:
            return False
    return True


def row_to_column_list(row_board: list):
    """
    This function makes column list out of row list

    >>> row_to_column_list(["123", "***", "321",])
    [['1', '*', '3'], ['2', '*', '2'], ['3', '*', '1']]
    """
    f_list = []
    for num_2 in range(len(row_board)):
        c_list = []
        for num in range(len(row_board)):
            row = row_board[num]
            row_list = list(row)
            c_list.append(row_list[num_2])
        f_list.append(c_list)
    return f_list


def row_check(r_list: list):
    """
    This function checks row for repeated numbers in row

    >>> row_check(['*', '*', '*', '*', ' ', ' ', '2', ' ', '3', '3', ' ', '4',\
     ' ', ' ', '*', '*', '*', '*'])
    False
    """
    num_list = []
    for num_2 in range(len(r_list)):
        if r_list[num_2].isdigit():
            num_list.append(int(r_list[num_2]))
    if len(num_list) > 1:
        for num_3 in range(len(num_list)):
            for times in range(1, len(num_list) - num_3):
                if num_list[num_3] == num_list[num_3 + times]:
                    return False


def check_colors(a_board: list):
    """
    This function checks weather there are different numbers in colored tiles

    >>> check_colors(["****1****", "*** 2****", "**  3****", "*   4****",\
    "    56781", "        *", "2      **", "      ***", "3 4  ****"])
    False
    """
    for num in range(len(a_board)):
        c_list = row_to_column_list(a_board)[num]
        row = a_board[len(a_board) - 1 - num]
        r_list = list(row)
        f_list = c_list + r_list
        if row_check(f_list) is False:
            return False
        else:
            return True
