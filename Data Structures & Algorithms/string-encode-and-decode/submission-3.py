class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = "" 
        delimiter = "#" 
        for word in strs:
            num = len(word) 
            encode += f"{num}#{word}"  
        print(encode) 
        return encode

    def decode(self, s: str) -> List[str]:
        decode, i = [], 0  
        while i < len(s): 
            j = i  
            while s[j] != "#": 
                j += 1 
            length = int(s[i:j]) 
            decode.append(s[j+1:j+1+length]) 
            i = 1 + j + length 
        return decode 

