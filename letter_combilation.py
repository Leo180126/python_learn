string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z", 
}
print(string_maps["1"][0])
def letter_combinations(a, b):
    ans = []
    for i in range(len(string_maps[a])):
        for j in range(len(string_maps[b])):
            ans.append(string_maps[a][i] + string_maps[b][j])
    return ans
print(letter_combinations("2", "3"))