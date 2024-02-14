import re

def build_scam_patterns():
    scam_patterns = {
        "Generic 12-digit numbers": r"^\d{12}$",
        "Malaysian phone numbers": r"^(\+?6?01)[0-46-9]-*\d{7,8}$",
        "US phone numbers": r"^(\+?1-?)?(\()?(\d{3})(?(2)\))[-.\s]?\d{3}[-.\s]?\d{4}$",
        "Indian phone numbers": r"^(\+?91|0)?[789]\d{9}$",
        "Chinese phone numbers": r"^(\+?86-?)?1[3456789]\d{9}$",
        # Add more patterns for other high-risk Asian countries as needed
    }
    return scam_patterns

def check_scammer_number(phone_number, scammer_patterns):
    for pattern_name, pattern in scammer_patterns.items():
        if brute_force_search(phone_number, pattern):
            return True, pattern_name
    return False, None

def brute_force_search(text, pattern):
    matches = re.finditer(pattern, text)
    return any(match.group(0) == text for match in matches)

# Example usage
scammer_numbers = build_scam_patterns()

while True:
    phone_number = input("Enter a phone number (or 'exit' to quit): ")

    if phone_number.lower() == 'exit':
        break

    is_scammer, pattern_name = check_scammer_number(phone_number, scammer_numbers)

    if is_scammer:
        print(f"The number matches a scammer pattern: {pattern_name}. Exercise caution!")
    else:
        print("The number does not match any known scammer patterns.")
