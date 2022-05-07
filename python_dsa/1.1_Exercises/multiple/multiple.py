def is_multiple(num: int, divisor: int):
    if divisor == 0:
        print("Error: Division by Zero")
        return
    if num % divisor == 0:
        print("True")
        return True
    else:
        print("False")
        return False

if __name__ == "__main__":
    
    (
    
    is_multiple(20, 5)
    
    )