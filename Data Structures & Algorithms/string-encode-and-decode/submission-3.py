class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in strs:
            encoded += str(len(i))+ '^' + i
        return encoded

    def decode(self, s: str) -> List[str]:

        i = 0
        length = 0

        decoded = []

        while i < len(s):
            length = 0
            while(s[i].isdigit()):
                length =length*10 + int(s[i])
                i += 1

            if(s[i]=='^'):
                i += 1 
            
            word = ''
            
            word += s[i:i+length]
            i += length
            
            decoded.append(word)
        return decoded

