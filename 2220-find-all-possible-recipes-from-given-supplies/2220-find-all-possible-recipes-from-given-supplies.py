class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        weight = defaultdict(int)
        graph = defaultdict(list)
        res = []

        for recipe in range(len(recipes)):
            for ing in ingredients[recipe]:
                graph[ing].append(recipes[recipe])
                weight[recipes[recipe]] += 1


        queue = deque()
        visited = set()

        for i in range(len(recipes)):
            for ing in ingredients[i]:

                if ing in supplies and ing not in visited:
                    queue.append(ing)

                    if ing in recipes and weight[ing] == 0:
                        res.append(ing)
                    visited.add(ing)

        while queue:
            node = queue.popleft()

            for neigh in graph[node]:

                if neigh not in visited:
                    weight[neigh] -= 1

                    if weight[neigh] == 0:

                        if neigh in recipes and neigh not in res:
                            res.append(neigh)

                        queue.append(neigh)
                        visited.add(neigh)

        for i in supplies:
            if i in recipes and i not in res:
                res.append(i)

        return res