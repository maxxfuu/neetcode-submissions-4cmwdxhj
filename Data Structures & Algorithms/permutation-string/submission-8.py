class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
      return False

    freq1 = [0] * 26
    for value in s1: 
      freq1[ord(value) - ord('a')] += 1 
    
    for left in range(len(s2) - len(s1) + 1):
      right = left
      freq2 = [0] * 26

      count = 0
      while right < len(s2) and count < len(s1):
        freq2[(ord(s2[right]) - ord('a'))] += 1
        right += 1
        count += 1

      if freq1 == freq2:
        return True
        
    return False




