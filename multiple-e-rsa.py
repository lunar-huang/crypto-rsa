from sympy import isprime, nextprime, gcd
import random

# 生成一个指定长度的质数
def generate_prime(bits=16):
    candidate = random.getrandbits(bits)
    while not isprime(candidate):
        candidate = random.getrandbits(bits)
    return candidate

# 加密函数
def encrypt(plaintext, e, n):
    c = pow(plaintext, e, n)
    return c

# 模拟RSA加密部分
if __name__ == '__main__':
    # 生成质数 p 和 q，并计算模数 n
    p = generate_prime(16)  # 16位质数
    q = generate_prime(16)  # 16位质数
    n = p * q
    phi = (p - 1) * (q - 1)

    # 生成3个不同且互质的公钥指数 e
    e_list = []
    while len(e_list) < 3:
        e = random.randint(2, phi)
        if gcd(e, phi) != 1 or any(gcd(e, ex) != 1 for ex in e_list):
            continue
        e_list.append(e)

    # 选择一个数字形式的明文
    plaintext = 42  # 示例数字明文
    print(f"Original plaintext: {plaintext}")

    # 使用不同的 e 加密消息
    c_list = [encrypt(plaintext, e, n) for e in e_list]

    # 输出加密结果
    for i, (e, c) in enumerate(zip(e_list, c_list), start=1):
        print(f"Encrypted message with e{i} (as number): {c}")
    print(f"Public key: n = {n}, e_list = {e_list}")

    # 提示如何将数据输入到攻击部分
    print("\nUse the following inputs in the attack script:")
    print(f"n: {n}")
    print(f"c_list: {c_list}")
    print(f"e_list: {e_list}")
