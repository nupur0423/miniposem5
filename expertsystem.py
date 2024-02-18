knowledge_base = {
    'rule1': {
        'condition': lambda person: person['age'] >= 18,
        'result': 'You are eligible for a loan.'
    },
    'rule2': {
        'condition': lambda person: person['income'] > 30000,
        'result': 'You meet the income requirement for a loan.'
    },
    'rule3': {
        'condition': lambda person: person['credit_score'] >= 650,
        'result': 'You have a good credit score.'
    },
    'rule4': {
        'condition': lambda person: person['employment_status'] == 'employed',
        'result': 'You have a stable job.'
    },
    'rule5': {
        'condition': lambda person: person['age'] <= 60,
        'result': 'Your age is within the acceptable range for a loan.'
    },
    'rule6': {
        'condition': lambda person: person['income'] > 50000,
        'result': 'Your income is above the threshold for a higher loan amount.'
    },
    'rule7': {
        'condition': lambda person: person['credit_score'] >= 750,
        'result': 'Your excellent credit score qualifies you for lower interest rates.'
    },
    'rule8': {
        'condition': lambda person: person['employment_status'] == 'self-employed',
        'result': 'Your self-employment status is considered for a loan application.'
    },
}

def evaluate_rules(person):
    results = []
    for rule_name in ['rule1', 'rule2', 'rule3', 'rule4','rule5', 'rule6', 'rule7', 'rule8']:
        if not knowledge_base[rule_name]['condition'](person):
            return results
        results.append(knowledge_base[rule_name]['result'])
    return results

person = {
    'age': int(input("Enter your age: ")),
    'income': float(input("Enter your annual income: ")),
    'credit_score': int(input("Enter your credit score: ")),
    'employment_status': input("Enter your employment status (employed/unemployed/self-employed): ")
}

eligibility_results = evaluate_rules(person)

if eligibility_results:
    print("Loan Eligibility Results:")
    for result in eligibility_results:
        print(result)
else:
    print("You are not eligible for a loan.")