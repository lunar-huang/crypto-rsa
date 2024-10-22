from sympy import mod_inverse

# 扩展欧几里得算法
def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = extended_gcd(b, a % b)
        return y, x - (a // b) * y, g

# 共模攻击函数
def common_modulus_attack(n, e_list, c_list):
    """
    使用扩展欧几里得算法对给定的 e 和 c 列表进行共模攻击
    :param n: 模数 n
    :param e_list: 公钥指数列表 [e1, e2, ..., ek]
    :param c_list: 密文列表 [c1, c2, ..., ck]
    :return: 恢复的明文 m（整数形式）
    """
    k = len(e_list)
    if k < 2:
        print("至少需要 2 对 (e, c) 才能进行共模攻击。")
        return None

    # 初始化线性组合的系数
    s_list = [1] * k
    for i in range(1, k):
        s1, s2, g = extended_gcd(e_list[i-1], e_list[i])
        if g != 1:
            print("公钥指数不互质，攻击失败。")
            return None
        s_list[i-1], s_list[i] = s1, s2

    # 计算 m 的合并幂次
    m_final = 1
    for i, s in enumerate(s_list):
        if s < 0:
            c_inv = mod_inverse(c_list[i], n)
            m_final *= pow(c_inv, -s, n)
        else:
            m_final *= pow(c_list[i], s, n)
        m_final %= n

    return m_final

# 主程序
if __name__ == '__main__':
    # 输入模数 n
    n = int(input("Enter the modulus n: "))

    # 输入 e 和 c 的对数
    num_pairs = int(input("Enter the number of (e, c) pairs: "))
    if num_pairs < 2:
        print("至少需要 2 对 (e, c) 才能进行共模攻击。")
        exit()

    # 输入所有 e 和 c 对
    e_list = []
    c_list = []
    for i in range(num_pairs):
        e = int(input(f"Enter the value of e{i+1}: "))
        c = int(input(f"Enter the value of c{i+1} (encrypted message): "))
        e_list.append(e)
        c_list.append(c)

    # 使用共模攻击恢复原始明文
    m = common_modulus_attack(n, e_list, c_list)

    if m:
        print(f"\n--- RSA Attack using Common Modulus ---")
        print(f"Recovered plaintext (as number): {m}")
    else:
        print("Attack failed.")
