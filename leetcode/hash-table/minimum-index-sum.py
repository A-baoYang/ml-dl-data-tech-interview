class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx_sum = 2000
        output = []
        list1 = {s: i for i, s in enumerate(list1)}
        list2 = {s: i for i, s in enumerate(list2)}
        for s in list1:
            if s in list2:
                if list1[s] + list2[s] < idx_sum:
                    idx_sum = list1[s] + list2[s]
                    output = [s]
                elif list1[s] + list2[s] == idx_sum:
                    output.append(s)
        return output
