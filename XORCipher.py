class XORCipher:
    """
    一个用于处理 XOR 加密/解密的类
    包含：
    - fixedXOR:对两串等长的 hex 进行 XOR
    - single_byte_xor:用单个字节 XOR 加解密
    - score_english_text:对结果打分（判断是否像英文）
    """
    def __init__(self):
        # 可以预定义字母频率表（用于打分）
        self.english_letter_freq = {
            'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
            'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
            'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
            'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
            'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
            'z': 0.00074, ' ': 0.13  # 空格也很常见
        }

    def fixedXOR(self, hex1: str, hex2: str) -> str:
        # 将十六进制字符串转换为字节
        bytes1 = bytes.fromhex(hex1)
        bytes2 = bytes.fromhex(hex2)
        # 计算XOR
        result = bytes(a ^ b for a, b in zip(bytes1, bytes2))
        # print(result)
        # 返回十六进制字符串
        return result.hex()
    
    def single_byte_xor_decrypt(self, ciphertext: str):
        """
        尝试所有单字节 key,返回得分较高的结果。
        """
        # ciphertext = bytes.fromhex(hex_str)
        keyList = range(256)
        plaintext = {}
        # print(keyList,plaintext)
        for key in keyList:
            key_byte = bytes([key])
            expandedKey = key_byte * len(bytes.fromhex(ciphertext))
            plaintext[key] = self.fixedXOR(ciphertext, expandedKey.hex())

    

    
    def score_english_text(self, text: str) -> float:
        """
        给文本打分
        """
        text = text.lower()
        return sum(self.english_letter_freq.get(ch, 0) for ch in text)






# 示例
if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    xor = XORCipher()
    xor.single_byte_xor_decrypt(hex1)
    
