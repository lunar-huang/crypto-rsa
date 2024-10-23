# 将整数转换回字符串消息
def int_to_string(m):
    try:
        return m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    except:
        return "Failed to decode the message."

# decrypt
def decrypt(ciphertext, d, n):
    m = pow(ciphertext, d, n)
    return int_to_string(m)

# brute force for small d to attack
def short_d_attack(ciphertext, n, max_d=2**16):
    # try every possible d smaller than 2^16
    for d in range(2, max_d):
        plaintext = decrypt(ciphertext, d, n)
        if "Failed to decode the message" not in plaintext:
            return plaintext, d
    return None, None

# Main function for attacking RSA
if __name__ == '__main__':
    # 输入 n 和加密消息
    n_input = int(input("Enter the value of n: "))
    ciphertext_input = int(input("Enter the encrypted message (as number): "))

    # 通过暴力枚举 d 进行攻击
    decrypted_message, d_found = short_d_attack(ciphertext_input, n_input, max_d=2**8)

    if decrypted_message:
        print("\n--- RSA Attack ---")
        print(f"Attack successful! Decrypted message: {decrypted_message}")
        print(f"Found decryption exponent: d = {d_found}")
    else:
        print("Attack failed. Could not find the correct decryption exponent.")
