from math import isqrt

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

# trial division near sqrt(n)
def sqrt_trial_attack(n):
    sqrt_n = isqrt(n)
    for i in range(sqrt_n - 1000, sqrt_n + 1000):
        if n % i == 0:
            p = i
            q = n // p
            return p, q
    return None, None

# Main function for attacking RSA
if __name__ == '__main__':
    # 输入 n 和加密消息
    n_input = int(input("Enter the value of n: "))
    ciphertext_input = int(input("Enter the encrypted message (as number): "))

    # 通过平方根附近的试除法对 n 进行因式分解
    p_found, q_found = sqrt_trial_attack(n_input)

    if p_found and q_found:
        print("\n--- RSA Attack with Non-Random Primes ---")
        print(f"Attack successful! Found factors: p = {p_found}, q = {q_found}")

        # 计算 phi(n)
        phi_found = (p_found - 1) * (q_found - 1)

        # 假设 e = 65537
        e_found = 65537
        d_found = pow(e_found, -1, phi_found)

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
        print("Attack failed. Could not find factors of n.")
