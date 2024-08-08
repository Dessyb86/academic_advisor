import json

read_file = open("./data/courses/farmingdale_state_college.txt", "r", encoding="utf-8")
write_file = open("./data/JSON/farmingdale.json", "w")
line = read_file.readline()
JSONs = []
JSON_to_add = {"course_name": "",
               "department_code": "",
               "course_num": 000,
               "description": "",
               "syllabus_url": "",
               "textbook_ISBN": -1,
               "course_offered": [],
               "corereqs": [],
               "prereqs": -1,
               "credits": -1}
while line:
    if line[0:3].isupper() and line[4:7].isnumeric():
        JSON_to_add["department_code"] = line[0:3]
        JSON_to_add["course_num"] = int(line[4:7])
        JSON_to_add["course_name"] = line[7:]

    elif "Course Offered:" in line:
        JSON_to_add["course_offered"] = line[16:]
    elif "Credits:" in line:
        JSON_to_add["credits"] = line[9]
        print(JSON_to_add)
        JSONs.append(JSON_to_add)
        JSON_to_add = {"course_name": "",
                       "department_code": "",
                       "course_num": 000,
                       "description": "",
                       "syllabus_url": "",
                       "textbook_ISBN": -1,
                       "course_offered": [],
                       "corereqs": [],
                       "prereqs": -1,
                       "credits": -1}
    else:
        JSON_to_add["description"] += line
        if "Prerequisite(s):" in line or JSON_to_add["prereqs"] != -1:
            try:
                start = line.index("Prerequisite(s):")
                JSON_to_add["prereqs"] = line[start + 17:]
            except ValueError:
                JSON_to_add["prereqs"] += line
    line = read_file.readline()

json.dump(JSONs, write_file)