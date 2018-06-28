import sklearn
from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
x = int(input())
y = int(input())

z = clf.predict([[x,y]])

if z == 1:
	print("Orange")
	
else:
	print("Apple")	
