class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        new_array = sorted(num_dict, key= num_dict.get, reverse = True)
        
        return new_array[:k]

# 파이썬 딕셔너리는 sort() 메서드가 없고 sorted()를 사용

# value 기준으로 키 정렬
# sorted(count, key=count.get, reverse=True)

# 키와 value를 함께 정렬
# sorted(count.items()) -> 결과적으로 튜플의 첫번째 값인 키를 기준으로 정렬

# 리스트를 딕셔너리로 바꾸려면 dict() 사용
# sorted_count = dict(
#    sorted(count.items(), key=lambda x: x[1], reverse=True)
# )
            