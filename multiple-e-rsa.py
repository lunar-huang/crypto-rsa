from sympy import isprime, nextprime, gcd
import random

# 生成一个指定长度的质数
def generate_prime(bits=64):
    candidate = random.getrandbits(bits)
    while not isprime(candidate):
        candidate = random.getrandbits(bits)
    return candidate

# 将字符串消息转换为整数
def string_to_int(message):
    return int.from_bytes(message.encode('utf-8'), byteorder='big')

# 将整数转换回字符串消息
def int_to_string(m):
    try:
        return m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    except:
        return "Failed to decode the message."

# 加密函数
def encrypt(plaintext, e, n):
    m = string_to_int(plaintext)
    c = pow(m, e, n)
    return c

# 模拟RSA加密部分
if __name__ == '__main__':
    # 生成质数 p 和 q，并计算模数 n
    p = generate_prime(64)  # 16位质数
    q = generate_prime(64)  # 16位质数
    n = p * q
    phi = (p - 1) * (q - 1)

    # 生成2个不同且互质的公钥指数 e
    e_list = []
    while len(e_list) < 2:
        e = random.randint(2, phi)
        if gcd(e, phi) != 1 or any(gcd(e, ex) != 1 for ex in e_list):
            continue
        e_list.append(e)

    # 输入一个字符串形式的明文
    message = "HELLO_RSA"
    print(f"Original message: {message}")

    # 使用不同的 e 加密消息
    c_list = [encrypt(message, e, n) for e in e_list]

    # 输出加密结果
    for i, (e, c) in enumerate(zip(e_list, c_list), start=1):
        print(f"Encrypted message with e{i} (as number): {c}")
    print(f"Public key: n = {n}, e_list = {e_list}")

    # 提示如何将数据输入到攻击部分
    print("\nUse the following inputs in the attack script:")
    print(f"n: {n}")
    print(f"c_list: {c_list}")
    print(f"e_list: {e_list}")
