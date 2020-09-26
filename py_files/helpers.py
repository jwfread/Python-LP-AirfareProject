# List of helper functions:


def read_range(sheet, begin, end):
    """ Pulls specified cell range of data - returns list of row lists or a single list depending on if it is an array of data or a vector of data respectively
    Args:
        sheet (spreadsheet object type utilized in 'openpyxl' library): Sheet of data to pull from
        begin (str): upper left cell
        end (str): bottom right cell
    """
    # specify upper left and lower right cells, returns a list or list of lists representing rows
    table = sheet[begin:end]
    height = len(table)
    width = len(table[0])
    if height == 1 or width == 1:
        # for a single row or column produce a list
        tmp = [cell.value for row in table for cell in row]
    else:
        # for an array of cells produces a list of row lists
        tmp = [[cell.value for cell in row] for row in table]
    return (tmp)
