class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1 ,-1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits

            digits[i] = 0
            if i == 0: # checking if for loop is @ index[0]
                return [1] + digits

        # result = "".join(map(str, digits))
        # result_int = int(result)
        # result_int = result_int + 1
        # res = list(map(int, str(result_int)))
        # # res = str(res).replace(" ","")
        # return res
            