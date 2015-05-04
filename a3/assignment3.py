# Ben Gunning
# Assignment 3
# Professor Wang
from __future__ import division
import fileinput
import csv

# Number of Sources
m = 30

# Number of Claims
n = 2000

# Initialize d between 0 and 1
d = .5

# Initialize empty lists
s = []
a = []
b = []

# Initialize List Data
SC = []
for i in range(0,m):
	SC.append([])
for j in range(0,n):
	for i in range(0,m):
		SC[i].append(0)

# Open Initialization File
truthTxt = open('a3t3' , 'r')
truthRows = csv.reader(truthTxt)
for row in truthRows:
	SC[int(row[0])-1][int(row[1])-1] = 1
truthTxt.close()

# Initialize s, a, and b
for i in range(0,m):
	s.append(0)
	a.append(0)
	b.append(0)
	for j in range(0,n):
		s[i] += float(SC[i][j]) / n
	a[i] = float(s[i])
	b[i] = float(s[i]) / 2.0

# Initialize Z, A, and B
Z = []
A = []
B = []
for j in range(0,n):
	Z.append(1)
	A.append(1)
	B.append(1)

# Old and New Represent Theta(t) and Theta(t+1)
old = []
new = []
for i in range(0,3):
	old.append([])
	new.append([])
new[0] = list(a)
new[1] = list(b)
new[2] = d
t = 0
while (old != new and t < 50):
	for i in range(0,2):
		old[i] = list(new[i])
	old[2] = new[2]
	t += 1
	Ztot = 0
	for j in range(0,n):
		A[j] = 1
		B[j] = 1
		for i in range(0,m):
			source = SC[i]
			A[j] *= (float(a[i]) ** source[j]) * ((1.0 - float(a[i])) ** (1 - source[j]))
			B[j] *= (float(b[i]) ** source[j]) * ((1 - b[i]) ** (1 - source[j]))
		Z[j] = A[j] * d / (A[j] * d + B[j] * (1 - d))
		Ztot += float(Z[j])
	for i in range(0,m):
		a[i] = 0
		b[i] = 0
		source = SC[i]
		for j in range(0,n-1):
			if (source[j]):
				a[i] += float(Z[j])
				b[i] += 1.0
				b[i] -= float(Z[j])
		a[i] /= float(Ztot)
		b[i] /= float(n - Ztot)
	d = Ztot / n
	new[0] = list(a)
	new[1] = list(b)
	new[2] = d

h = []
for j in range(0,n):
	h.append(0)
	if (Z[j] >= .5):
		h[j] = 1
	else:
		h[j] = 0

e = []
for i in range(0,m):
	e.append(0)
	denom = 0
	source = SC[i]
	for j in range(0,n):
		if (source[j]):
			denom += 1
			e[i] += h[j]
	if (denom):
		e[i] /= denom
	else:
		e[i] = 0

target = open('a3s3' , 'w')
target.truncate()
for j in range(1,n+1):
	next = "%d,%d\n" % (j , h[j-1])
	target.write(next)
target.close()
