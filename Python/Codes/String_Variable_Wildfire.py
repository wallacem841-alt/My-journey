x = '''Wrapped in biting wind
Hearts will never bleed
Frozen and banished
Out of grief
In their restless dreams
They try so hard to breathe
Pulses flutter and sting
Within this bleakness

Pain will come with the blade
Pain will wake up the despondent crowd in this dormant world
Somehow
Unsheathe a sword not to kill
Unsheathe a sword to rend those clouds above the ground
Wake up, it's time to gather now'''

print(len(x))
print('Pain' in x)
print('pain' in x) # returns as false because of lowercase
if "Pain" in x:
  print("Yes, 'Pain' is present.")
print('Loud' not in x)
#print only if "Loud" is NOT present:
if 'Loud' not in x:
  print('Loud is not in Wildfire')