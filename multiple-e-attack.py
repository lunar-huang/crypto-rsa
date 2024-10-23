from sympy import mod_inverse

# 将整数转换回字符串消息
def int_to_string(m):
    try:
        return m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    except:
        return "Failed to decode the message."

# 扩展欧几里得算法
def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = extended_gcd(b, a % b)
        return y, x - (a // b) * y, g

# common_modulus_attack e and c
def common_modulus_attack(n, e1, e2, c1, c2):

    # use extend euclid algo
    s1, s2, g = extended_gcd(e1, e2)
    if g != 1:
        print("public exponent e are not coprime with each other")
        return None

    # 计算 m 的合并幂次
    if s1 < 0:
        c1_inv = mod_inverse(c1, n)
        m_final = pow(c1_inv, -s1, n) * pow(c2, s2, n) % n
    else:
        m_final = pow(c1, s1, n) * pow(c2, s2, n) % n

    return m_final

# 主程序
if __name__ == '__main__':
    # 输入模数 n
    n = int(input("Enter the modulus n: "))

    # 输入两对 (e, c)
    e1 = int(input("Enter the value of e1: "))
    c1 = int(input("Enter the value of c1 (encrypted message): "))
    e2 = int(input("Enter the value of e2: "))
    c2 = int(input("Enter the value of c2 (encrypted message): "))

    # 使用共模攻击恢复原始明文
    m = common_modulus_attack(n, e1, e2, c1, c2)

    if m:
        recovered_message = int_to_string(m)
        print(f"\n--- RSA Attack using Common Modulus ---")
        print(f"Recovered plaintext (as number): {m}")
        print(f"Recovered plaintext (as string): {recovered_message}")
    else:
        print("Attack failed.")
