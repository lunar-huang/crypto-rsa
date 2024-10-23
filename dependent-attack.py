from math import isqrt
from sympy import mod_inverse, gcd

# start trial division from sqrt(n)
def sqrt_trial_attack(n):
    sqrt_n = isqrt(n)
    for i in range(sqrt_n, sqrt_n - 10000, -1):  # try 10000 times
        if n % i == 0:
            p = i
            q = n // p
            return p, q
    return None, None

# 将整数转换回字符串消息
def int_to_string(m):
    try:
        return m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    except:
        return "Failed to decode the message."

# 解密函数
def decrypt(ciphertext, d, n):
    m = pow(ciphertext, d, n)
    return int_to_string(m)

# Main function for attacking RSA
if __name__ == '__main__':
    # 输入 n 和加密消息
    n_input = int(input("Enter the value of n: "))
    ciphertext_input = int(input("Enter the encrypted message (as number): "))

    # 通过平方根试除法对 n 进行因式分解
    p_found, q_found = sqrt_trial_attack(n_input)

    if p_found and q_found:
        print(f"Factorization successful: p = {p_found}, q = {q_found}")

        # 计算 phi(n)
        phi_found = (p_found - 1) * (q_found - 1)

        # 假设 e = 65537
        e_found = 65537
        if gcd(e_found, phi_found) != 1:
            print("e and phi(n) are not coprime. Please check the inputs.")
        else:
            # 计算私钥 d
            d_found = mod_inverse(e_found, phi_found)
            print(f"Calculated private key d = {d_found}")

            # 输出所有参与RSA的参数
            print("\n--- RSA Parameters ---")
            print(f"p = {p_found}")
            print(f"q = {q_found}")
            print(f"n = {n_input}")
            print(f"phi(n) = {phi_found}")
            print(f"e = {e_found}")
            print(f"d = {d_found}")
            
            # 解密消息
            plaintext_found = decrypt(ciphertext_input, d_found, n_input)
            print(f"Decrypted message: {plaintext_found}")
    else:
        print("Factorization failed. Could not find factors of n.")
