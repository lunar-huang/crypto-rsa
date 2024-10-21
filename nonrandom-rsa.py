import random
from sympy import isprime, nextprime

# 生成固定的256位基准质数
def generate_fixed_prime():
    base = random.getrandbits(240) << 16  # 固定前240位
    for i in range(2**16):  # 尝试16位的变化
        candidate = base + i
        if isprime(candidate):
            return candidate
    return None

# 生成非随机质数的RSA密钥对
def generate_non_random_rsa():
    p = generate_fixed_prime()
    q = nextprime(p)  # 使用下一个质数，模拟非随机性

    n = p * q
    phi = (p - 1) * (q - 1)

    # 使用常用的公钥指数 e = 65537
    e = 65537
    d = pow(e, -1, phi)

    return (e, n, d, p, q)

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

# 解密函数
def decrypt(ciphertext, d, n):
    m = pow(ciphertext, d, n)
    return int_to_string(m)

# 测试生成非随机质数的RSA加密
if __name__ == '__main__':
    e, n, d, p, q = generate_non_random_rsa()

    message = "NON_RANDOM_RSA"
    ciphertext = encrypt(message, e, n)

    print("\n--- RSA Encryption with Non-Random Primes ---")
    print(f"Original message: {message}")
    print(f"Encrypted message (as number): {ciphertext}")
    print(f"Public key: (e={e}, n={n})")
    print(f"Private key: d={d}")
    print(f"Factors: p={p}, q={q}")
