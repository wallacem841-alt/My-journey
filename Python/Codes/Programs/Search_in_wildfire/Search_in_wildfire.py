WFL = '''Wrapped in biting wind
Hearts will never bleed
Frozen and banished
Out of grief
In their restless dreams
They try so hard to breathe
Pulses flutter and sting
Within this bleakness
(Ah, ah)

Pain will come with the blade
Pain will wake up the despondent crowd in this dormant world
Somehow
Unsheathe a sword not to kill
Unsheathe a sword to rend those clouds above the ground
Wake up, it's time to gather now

The only warmth remains
In hands clasped so tight
The only fire exists
In brave hearts
Seasons that refuse
To change over the years
Will find their way back
Back on track
(Oh, oh, oh, oh, oh)

We've made a choice, go fight against your fate!
Pain will come with the blade
Pain will wake up the despondent crowd in this dormant world
Somehow
Unsheathe a sword not to kill
Unsheathe a sword to rend those clouds above the ground
Wake up, it's time to gather now

Forget about the rules written on weathered rock
There were chasers of light
Find the way or get lost
We have no way to know where they all headed for
See the light from afar, just blaze through the thorns
We know it's right over there
We have something to declare
Whatever is arriving, we'll be prepared

We've made a choice, go fight against your fate!
Pain will come with the blade
Pain will wake up the despondent crowd in this dormant world somehow
Unsheathe a sword not to kill
Unsheathe a sword to rend those clouds above the ground
Wake up to hear the cheering sound'''

IPT = input("Search in Wildfire Lyrics: ")

if IPT in WFL:
    print(IPT, "is in Wildfire")

if IPT not in WFL:
    print(IPT, "is not in Wildfire")

'''GPT gave this alternative for case-insensitive
IPT = input("Enter a phrase: ").lower()
WFL_lower = WFL.lower()

if IPT in WFL_lower:
    print(IPT, "is in Wildfire")

if IPT not in WFL_lower:
    print(IPT, "is not in Wildfire")
'''
input("Press Enter to exit...") # this makes the prompt stay open