
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"DAY 8/table{n}", "w") as f:
        f.write(table)
for i in range(1, 11):
    generateTable(i)