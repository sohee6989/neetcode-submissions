from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict()
    
        for str in strs:
            sort_str_list = sorted(str)
            sort_str = ''.join(sort_str_list)
        
            if sort_str not in strs_dict:
                strs_dict[sort_str] = []
            strs_dict[sort_str].append(str)
        
        return list(strs_dict.values())

# d.keys()      # 모든 키
# d.values()    # 모든 값
# d.items()     # (키, 값) 쌍