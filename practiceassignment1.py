#create dict with student
students={101:{"Name":"shravani","scores":[85,88,90]},
         102:{"Name":"siddhi","scores":[75,98,94]},
         103:{"Name":"ankita","scores":[70.96,92]},
         104:{"Name":"vedu","scores":[75,84,93]}
}
#calculate avg
for sid,details in students.items():
    avg=sum(details["scores"])/len(details["scores"])
    details["average"]=avg
    details["passed"]=avg>=50 #boolen flag

#print names
print("students who passed:")
for sid,details in students.items():
    if details["passed"]:
        print(details["Name"])

#guess no. 

#create no.list&string acccept the valueform user, seprate the list form max no.,display name in sored value
