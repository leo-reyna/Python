def tax_calculator(subtotal, sales_tax=.06):
    """takes in a subtotal and tax rate and returns tax and total owed

    Args:
        subtotal(float): cost of items in transaction
        tax_rate (float, optional): tax rate at store location. Defaults to .06

    Returns:
        list: list containing subtotal, total, and tax
    """
    tax = round(subtotal * sales_tax, 2)
    total = round(subtotal + tax, 2)

    return [subtotal, tax, total]
