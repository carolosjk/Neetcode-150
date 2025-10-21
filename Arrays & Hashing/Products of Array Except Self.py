from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productsList= []
        totalZeroes = 0

        for n in nums:
            if n == 0:
                totalZeroes += 1
        
        if totalZeroes > 1:
            return [0] * len(nums)
        
        if totalZeroes == 1:
            for n in nums:
                if n != 0:
                    productsList.append(0)
                else:
                    product = 1
                    for nn in nums:
                        if nn != 0:
                            product *= nn
                    productsList.append(product)
        
        if totalZeroes == 0:
            totalProduct = 1
            for n in nums:
                totalProduct *= n
            for n in nums:
                productsList.append(totalProduct//n)


        return productsList

      


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,4,6]))
    print(solution.productExceptSelf([-1,0,1,2,3]))
    print(solution.productExceptSelf([-1,0,1,2,0,3]))


    
