import random
from sympy import nextprime, isprime, mod_inverse, gcd

# 生成一个指定长度的质数
def generate_prime(length=512):
    while True:
        prime_candidate = random.getrandbits(length)
        if isprime(prime_candidate):
            return prime_candidate

# 生成连续质数的RSA密钥对
def generate_consecutive_rsa(length=512):
    p = generate_prime(length)
    q = nextprime(p)  # 生成 p 之后的下一个质数 q

    n = p * q
    phi = (p - 1) * (q - 1)

    # 选择公钥指数 e = 65537（常用值）
    e = 65537
    if gcd(e, phi) != 1:
        return generate_consecutive_rsa(length)

    # 计算私钥 d
    d = mod_inverse(e, phi)

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

# 测试生成连续质数的RSA加密
if __name__ == '__main__':
    e, n, d, p, q = generate_consecutive_rsa(length=512)  # 使用较小长度用于快速测试

    message = "CONSECUTIVE_RSA"
    print(f"\nOriginal message: {message}")

    # Encrypt the message
    ciphertext = encrypt(message, e, n)
    print(f"Encrypted message (as number): {ciphertext}")
    print(f"Public key: (e={e}, n={n})")
    print(f"Private key: d={d}")
    print(f"Factors: p={p}, q={q}")
