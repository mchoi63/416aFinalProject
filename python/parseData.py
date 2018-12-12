data, newData = [], []

with open('CSE 416 Data Uncleaned.csv', 'r') as f:
	f.readline()
	for line in f:
		data.append(tuple([x for x in line.strip().split(',')]))
iterator = 0
for entry in data:
	ID, School, Year, South_40, Village, AC_Frat_Row, Bauer_Law_School, DUC_Area, Bio_Psych, Chemistry, Engineering_Quad, Brookings_Quad, Brown_School, Sam_Fox, Northest_Corner = entry
	stats = ["South_40", "Village", "AC_Frat_Row", "Bauer_Law_School", "DUC_Area", "Bio_Psych", "Chemistry", "Engineering_Quad", "Brookings_Quad", "Brown_School", "Sam_Fox", "Northest_Corner"]
	for i, x in enumerate([South_40, Village, AC_Frat_Row, Bauer_Law_School, DUC_Area, Bio_Psych, Chemistry, Engineering_Quad, Brookings_Quad, Brown_School, Sam_Fox, Northest_Corner]):
		newData.append((School, Year, stats[i], str(int(ID)+50)))
		for y in x.split('. '):
			if y == 'I don\'t have any class here': continue
			newData.append((School, Year, str(int(ID)+50), y))
			iterator += 1

with open('Student-ID.csv', 'w') as f:
	f.write('School,Year,Source,Target\n')
	for entry in newData:
		f.write('%s,%s,%s,%s\n' % entry)