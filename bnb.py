'''
Given a set of integers containing n elements (A[i] where 1<=i<=n) and thereafter T
question each containing single integer Z . you need to tell whether it is possible to
take any subset from the original set such that sum of the elements in it when XOR’d
with Z results in zero.
INPUT:
first line of the input contains a single integer n denoting the number of elements in
the set. Next line of input contains n space separated integers denoting elements of
set. Next line of input contains a single integer T denoting the number of
question.Next T lines contains T integers Z describing each question.(one per line)
OUTPUT:
output consists of T lines each containing either “Yes” or “No” (quotes for clarity)
depending upon existence of such subset.
'''
def branchAndBound(total, array) :
	l = len(array)
	if total in array or sum(array) == total :
		return True
	if l == 0 :
		return False
	elif total == 0 or array[0] == total :
		return True
	else :
		return (branchAndBound(total - array[0] ,array[1:]) or
		branchAndBound(total, array[1:]))

		
n = int(raw_input())
array = map(int, raw_input().strip().split())
t = int(raw_input())

for _ in range(t) :
	total = int(raw_input())
	print ("Yes" if branchAndBound(total, array) else "No")	

