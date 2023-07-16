def raise_error_with_cat(error_code):
    error_message = """
       /\_/\\
      ( o.o )
       > ^ <
    """
    if not type(error_code)==str:
        error_code = str(error_code)

    raise ValueError(f"Bingo Bongo, you have an error!\n\n{error_message}\nError Code: {error_code}")

# Calling the function to demonstrate the error
if __name__ == '__main__':
    raise_error_with_cat("Testing!")
