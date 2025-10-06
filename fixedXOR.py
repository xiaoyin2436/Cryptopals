def fixedXOR(hex1, hex2):
    # 将十六进制字符串转换为字节
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)
    # 计算XOR
    result = bytes(a ^ b for a, b in zip(bytes1, bytes2))
    # 返回十六进制字符串
    return result.hex()

# 示例
if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    print("XOR结果:", fixedXOR(hex1, hex2))
    print(bytes.fromhex(fixedXOR(hex1, hex2)))  # 输出字节形式
