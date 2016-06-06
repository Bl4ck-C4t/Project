import re
txt = "Stefan:14*Math:6,5,4 Biology:4,5,7 ;Prasi:15*Math:6,3,4 Biology:3,5,7 ;"
for x in txt.split(";")[:-1]:
    grades = {}
    name = re.search(r"\w+",x).group()
    age = re.search(r"\d+",x).group()
    ls.append(Students(name,age))
    x = re.search(r"\*.+",x).group()
    x = x[1:]
    subject = x.split(" ")[:-1]
    for y in subject:
        sub = re.search(r"[a-zA-Z]+",y).group()
        grade = re.findall(r"\d+",y)
        grades[sub] = grade
        ls[-1].grades = grades
    
