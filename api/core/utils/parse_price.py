def parse_price(price_str):
    """Converts Human price string to decimal values
    
    Arguments:
        price_str {str} -- Example $720K, $150M, $1200, 100
    
    Returns:
        float -- The dollar value as a float.
    """
    if not price_str:
        return 0
        
    if price_str.startswith('$'):
        price_str = price_str[1:]
    
    is_millions = price_str[-1].lower() == "m"
    is_thousands = price_str[-1].lower() == "k"

    magnitude = 1
    if is_millions:
        magnitude = 1000000
        price_str = price_str[:-1]

    if is_thousands:
        magnitude = 1000
        price_str = price_str[:-1]

    return float(price_str) * magnitude
