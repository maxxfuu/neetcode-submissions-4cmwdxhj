class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = "" 
        for word in strs: 
            encode += word + "人" 

        return encode 

    def decode(self, s: str) -> List[str]:
        decode = [] 
        temp = ""
        for char in s: 
            if char != "人": 
                temp += char 
            else: 
                decode.append(temp) 
                temp = "" 

        return decode 