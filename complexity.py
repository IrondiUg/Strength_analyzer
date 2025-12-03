import re

def suggestions():
    print('=====PASSWORD COMPLEXITY SUGGESTIONS=====')
    print('1. Use at least 8 characters (12+ for better security).')
    print('2. Include both uppercase and lowercase letters.')
    print('3. Add numbers to your password.')
    print('4. Incorporate special characters (e.g., !, @, #, $, etc.).')
    print('5. Avoid common words or easily guessable information.')
    print('6. Consider using a passphrase for added security.')
    print('7. Avoid birthdays, petnames, or simple patterns like "12345" or "password".')

def recommendations(criteria):
    if not criteria['length']:
        print('- Increase the length of your password to at least 8 characters.')
    if not criteria['length_bonus']:
        print('- For better security, consider using 12 or more characters.')
    if not criteria['upper']:
        print('- Add uppercase letter(s) to your password.')
    if not criteria['lower']:
        print('- Include lowercase letter(s) in your password.')
    if not criteria['number']:
        print('- Incorporate number(s) into your password.')
    if not criteria['spe_char']:
        print('- Use special character(s) to enhance password strength.')
    

def check_strength(password):
    score = 0
    criteria = {
        'length': len(password)>=8,
        'length_bonus': len(password)>=12,
        'upper': bool(re.search(r'[A-Z]', password)),
        'lower': bool(re.search(r'[a-z]', password)),  
        'number': bool(re.search(r'[0-9]', password)), 
        'spe_char': bool(re.search(r'[!@#$%^&*()_\+\-\=\[\]{}\\|;:\'"<,.>/?]', password)), 
    }
    if criteria['length']:
        score+=20
    if criteria['length_bonus']:
        score+=5
    if len(password)>=16:
        score+=10
    if criteria['upper']:
        score+=15
    if criteria['lower']:
        score+=15
    if criteria['number']:
        score+=15
    if criteria['spe_char']:
        score+=10

    if score<30:
        pass_strength = 'WEAK'
    elif score<60:
        pass_strength = 'FAIR'
    elif score<80:
        pass_strength = 'GOOD'
    else:
        pass_strength ='STRONG'

    return{
        'score': score,
        'strength': pass_strength,
        'criteria': criteria
    }

def feedback(result):
    print('\n====STRENGTH ANALYSIS====')
    print(f"\nStrength: {result['strength']} (Score: {result['score']}/100)")

def main():
    print('PASSWORD COMPLEXITY CHECKER')
    suggestions()
    while True:
        password = input('\nEnter Password To Check \n:: ').strip()
        if not password:
            print('Cannot Be Empty')
            continue
        result = check_strength(password)
        feedback(result)

        if result['strength'] != 'STRONG':
            print('\n====RECOMMENDATIONS TO IMPROVE PASSWORD STRENGTH====')
            recommendations(result['criteria'])
if __name__ == "__main__":
    main() 