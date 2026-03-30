class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        # visitSet = all courses that has been considered
        considered = set()

        def dfs(course):
            # base case:
            if course in considered:
                return False
            
            if preMap[course] == []:
                return True
            
            considered.add(course)
            for pre in preMap[course]:
                if not dfs(pre): 
                    return False
            considered.remove(course)
            preMap[course] = [] 
            return True

        for course in range(numCourses): 
            if not dfs(course): return False
        return True