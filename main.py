import re

def check_password_strength(password, common_passwords):
    # Criteria assessment
    length_criteria = len(password) >= 6
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Wordlist checker
    if password in common_passwords:
        return "A senha está na lista de senhas comuns! Escolha uma senha diferente."

    # Counting the number of criteria met
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Password strength assessment
    if not length_criteria:
        return "A senha deve ter pelo menos 6 caracteres!"
    elif criteria_met == 8:
        return "A força da senha é forte."
    elif criteria_met == 5:
        return "A força da senha é média."
    else:
        missing_criteria = []
        if not uppercase_criteria:
            missing_criteria.append("um caractere maiúsculo")
        if not lowercase_criteria:
            missing_criteria.append("um caractere minúsculo")
        if not digit_criteria:
            missing_criteria.append("um dígito")
        if not special_char_criteria:
            missing_criteria.append("um caractere especial")

        missing_criteria_message = " e ".join(missing_criteria)
        return f"A senha deve conter pelo menos {missing_criteria_message}!"

# Function that receives as a parameter the path of the file that contains the list of common passwords.

def load_common_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            common_passwords = file.read().splitlines()
        return common_passwords
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

def main():
    common_passwords = load_common_passwords('commons.txt')
    if not common_passwords:
        return
    
    while True:
        try:
            password = input("Por favor, insira a senha: ")
            print(check_password_strength(password, common_passwords))
        except Exception as e:
            print(f"Ocorreu um erro ao processar a senha: {e}")
        
        try:
            cont = input("Deseja verificar outra senha? (s/n): ").strip().lower()
            if cont != 's':
                print("Encerrando o programa.")
                break
        except Exception as e:
            print(f"Ocorreu um erro ao processar a entrada: {e}")
            print("Encerrando o programa.")
            break

if __name__ == "__main__":
    main()
