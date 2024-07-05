import re


def english_to_propositional_logic(sentence):
    # Convert sentence to lowercase and remove any extra whitespace
    sentence = sentence.strip().lower()

    # Replace common English phrases with their propositional logic equivalents
    translation = {
        'if and only if': '<->',
        'if': '->',
        'then': '->',
        'implies': '->',
        'only if': '<->',
        'equivalent to': '<->',
        'equals': '<->',
        'is true': '',
        'is false': '~',
    }
    for phrase, logic in translation.items():
        sentence = sentence.replace(phrase, logic)

    # Identify simple statements in the sentence and assign them unique variable names
    # A pattern to match simple statements
    statement_pattern = re.compile(r'[a-z\s]*[a-z]+')
    # Find all simple statements in the sentence
    statements = statement_pattern.findall(sentence)
    var_dict = {statement: f'p{i}' for i, statement in enumerate(statements)}

    # Replace the simple statements with their assigned variable names
    for statement, var_name in var_dict.items():
        sentence = sentence.replace(statement, var_name)

    # Replace any remaining English words with their propositional logic equivalents
    sentence = re.sub(r'\bnot\b', '~', sentence)
    sentence = re.sub(r'\band\b', '&', sentence)
    sentence = re.sub(r'\bor\b', '|', sentence)

    # Wrap the translated sentence in parentheses
    sentence = f'({sentence})'

    # Construct the final propositional logic premise by combining the variable assignments and the translated sentence
    premise = ' & '.join(
        [f'{var_name} = {var_value}' for var_name, var_value in var_dict.items()])
    premise += f' -> {sentence}'

    return premise


print(english_to_propositional_logic("If it is raining, then it is cloudy."))

print(english_to_propositional_logic("I will go to the beach if and only if it is sunny and not raining."))

print(english_to_propositional_logic("It is not true that if it is raining then it is sunny."))


def apply_modus_ponens(premise, premises):
    # Extract the conclusion from the premise
    conclusion = premise.split('->')[-1].strip()

    # Check if the conclusion matches the antecedent of any of the other premises
    for other_premise in premises:
        antecedent = other_premise.split('->')[0].strip()
        if antecedent == conclusion:
            # If there is a match, return the new premise that results from applying modus ponens
            return f'{other_premise.split("->")[1].strip()}'

    # If there is no match, return None
    return "no match"


# Convert two English sentences into propositional logic premises
premise1 = english_to_propositional_logic(
    "If it is raining, then the ground is wet.")
premise2 = english_to_propositional_logic("It is raining.")
# Apply modus ponens to derive a new premise
new_premise = apply_modus_ponens(premise1, [premise2])

# Apply modus ponens to derive a new premise
new_premise = apply_modus_ponens(premise1, [premise2])
print(new_premise)
# output: 'the ground is wet'

premise = 'p -> q'
premises = ['p', 'q -> r']
new_premise = apply_modus_ponens(premise, premises)
print(new_premise)
