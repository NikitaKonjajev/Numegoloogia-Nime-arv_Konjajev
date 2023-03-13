def calculate_name_number(name):
    with open('russian_alphabet.txt', 'r', encoding='utf-8') as f:
        russian_alphabet = dict(line.strip().split() for line in f)
    with open('latin_alphabet.txt', 'r', encoding='utf-8') as f:
        latin_alphabet = dict(line.strip().split() for line in f)

    name_lower = name.lower()
    if name_lower[0] in russian_alphabet:
        alphabet = russian_alphabet
    elif name_lower[0] in latin_alphabet:
        alphabet = latin_alphabet
    else:
        return "Не удалось определить алфавит для имени."

    name_values = {c.lower(): int(alphabet.get(c.lower(), 0)) for c in name}
    name_number = sum(name_values.values())
    while name_number > 9:
        name_number = sum(int(d) for d in str(name_number))
    return name_number, name_values

