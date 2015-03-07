def swap(arr, arg1, arg2):
	arr[arg1], arr[arg2] = arr[arg2], arr[arg1]

class WordState:
	def __init__(self, wordIndex, tableAssignment):
		self.wordIndex = wordIndex
		self.tableAssignment = tableAssignment

class DOCState:
	def __init__(self, instance, docID):
		self.instance = instance
		self.docID = docID
		self.numTables = 0
		self.documentLength = len(instance)
		self.words = []
		self.wordCountByTable = []
		self.tableToTopic = []
		for i in range(documentLength):
			words.append(new WordState(instance[i], -1))

	def defragment(kOldToKNew):
		tOldToTNew = []
		newNumberOfTables = 0
		for t in range(numTables):
			if wordCountByTable[t] > 0:
				tOldToTNew.append(newNumberOfTables)
				tableToTopic.append(kOldToKNew[tableToTopic[t]])
				swap(wordCountByTable, newNumberOfTables, t)
				newNumberOfTables = newNumberOfTables + 1
			else:
				tableToTopic.append(-1)

		numTables = newNumberOfTables
		for i in range(documentLength):
			words[i].tableAssignment = tOldToTNew[words[i].tableAssignment]