import pytarski as tw

# create a "truth table" with a sentence
tt = tw.BooleTruthTable('not p and q')

# create a list of dictionaries with your atomic statement (variable) names and 
# the values which make them true
l = [{'p': False, 'q': True}]

# check if all the dictionaries contain scenarios that are true
print(tt.checkTrue(l)) # should be True

# if you add a scenario that doesn't work, checkTrue will return False
l.append({'p': False, 'q': False})
print(tt.checkTrue(l)) # should be False

# likewise we can create a list that covers some or all of the false scenarios
m = [{'p': True, 'q': True}, {'p': True, 'q': False}, {'p': False, 'q': False}]

# and we can evaluate this list to check if they are all False, in which case 
# checkFalse will somewhat confusingly return True
print(tt.checkFalse(m)) # should be True
