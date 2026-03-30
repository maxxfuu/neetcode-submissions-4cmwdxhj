class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        print(hashmap)

        considered = set()
        # This ensures that during backtracking, the node is removed from the 
        # set to allow it to be revisited in other branches of the search.

        # iterating through all the courses. Assume 3 courses, then 0, 1, 2
        def dfs(course: int): 
            if course in considered: return False
            if hashmap[course] == []: return True 

            considered.add(course)
            for adj in hashmap[course]:
                if not dfs(adj): 
                    return False
            considered.remove(course)
            hashmap[course] = []
            return True
        
        for i in range(numCourses):
            print(i)
            if not dfs(i): return False
        
        return True



        
