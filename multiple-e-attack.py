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

# 使用中国余数定理进行共模攻击
def common_modulus_attack(n, e_list, c_list):
    # 扩展欧几里得算法，寻找 e 的线性组合
    s_list = []
    for i in range(len(e_list)):
        s1, s2, g = extended_gcd(e_list[i], e_list[0])  # 对每个 e 和第一个 e 求线性组合
        if g != 1:
            print("Public exponents are not coprime, attack failed.")
            return None
        s_list.append(s1)

    # 计算 m^s1, m^s2, ..., 并组合结果
    m_parts = [pow(c_list[i], s_list[i], n) for i in range(len(e_list))]
    m_final = 1
    for m in m_parts:
        m_final = (m_final * m) % n

    return int_to_string(m_final)

# Main function for attacking RSA
if __name__ == '__main__':
    # 输入模数 n
    n = int(input("Enter the value of n: "))

    # 输入 e 和密文的数量
    num = int(input("Enter the number of e-c pairs: "))

    # 输入所有 e 和密文 c
    e_list = []
    c_list = []
    for i in range(num):
        e = int(input(f"Enter the value of e{i+1}: "))
        c = int(input(f"Enter the value of c{i+1}: "))
        e_list.append(e)
        c_list.append(c)

    # 使用共模攻击解密消息
    decrypted_message = common_modulus_attack(n, e_list, c_list)

    if decrypted_message:
        print(f"\n--- RSA Attack using Common Modulus ---")
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Attack failed.")
