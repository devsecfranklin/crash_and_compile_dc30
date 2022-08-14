# DEFCON30 Crash and Compile Contest

```
 ____  _____ _____ ____ ___  _   _   _____  ___  
|  _ \| ____|  ___/ ___/ _ \| \ | | |___ / / _ \ 
| | | |  _| | |_ | |  | | | |  \| |   |_ \| | | |
| |_| | |___|  _|| |__| |_| | |\  |  ___) | |_| |
|____/|_____|_|   \____\___/|_| \_| |____/ \___/ 
                                                 

                    _                       _ 
  ___ _ __ __ _ ___| |__     __ _ _ __   __| |
 / __| '__/ _` / __| '_ \   / _` | '_ \ / _` |
| (__| | | (_| \__ \ | | | | (_| | | | | (_| |
 \___|_|  \__,_|___/_| |_|  \__,_|_| |_|\__,_|
                                              
                           _ _      
  ___ ___  _ __ ___  _ __ (_) | ___ 
 / __/ _ \| '_ ` _ \| '_ \| | |/ _ \
| (_| (_) | | | | | | |_) | | |  __/
 \___\___/|_| |_| |_| .__/|_|_|\___|
                    |_|             

```

As explained on the [Crash and Compile Website](https://crashandcompile.org/), this is a
coding challenge with a twist. You must complete the challenges while consuming many alcoholic
beverages. And because it's DEFCON, you must also endure no small amount of haranguing
from "Team Distraction".

Just happened to bump into [PunkAB](https://twitter.com/punk_ab) on his way to set things
up and I was thinking I'd at least stop by to check it out. He suggested I compete. I had
a laptop and the requisite wired Ethernet gear. I had no excuse not to join. 

For my part, I was on the "Control Team". Scientific experiments require a control, and
this one is no different. So I got to play without having to endure the liver damage.

## Round One

Had no clue what was going on. Someone shouted "GO" and it was then I realized my team
wasn't registered because we were on the wrong website. So that's five minutes gone. 
Everyone was screaming and going crazy. People drinking large amounts of alcohol and
acting up. The participants, the organizers, the audience, everyone. We had three people
trying to help but just me doing Python. Another person was expert level in C++ but we
were getting caught up on syntax and small mistakes, trying to swithc ideas between
languages. Wasted at least five minutes trying to figure out that `python` was actually
calling the old version 2, whcih I didn't even know was still installed on my machine?
Only one laptop for the whole team... just a wild environment to try to work in. 

I think our solution did work but never got to try it against the grader. 
The [output](round1/output.txt) file here shows the same output that is expected
in the exmaple solution. (Which I meant to capture a PDF of but forgot) Another problem was
I didn't realize I needed to submit before the clock ran out. Also realized I needed
to add the `N` back to the string holding the node name. (That bit was completed after
the clock ran out and everyone was doing shots and running off to vomit). We lose a team
mate at the end of this round.

So... zero points for round one! [The possibly working but ungraded soution is here](round1/nodes.py)

## Round Two 

OK so this round I am determined to get some points on the board before time runs out.
Again someone shouts "GO" and I'm trying to understand the problem. About then was when
I began getting pelted with ping pong balls. A lady in a Deadpool costume has her 
armpit in my face trying loudly to recall the last time she showered. Jocularity...
debauchery... just madness. I'm forgetting and trying to look up things I've done easily
every day so many times in the past. Can't figure out why the directions are saying?
It's jsut about starting to make sense, when suddenly a LITERAL FASHION SHOW breaks out
right then and there. Lucky my water had a lid because it sas sideways on my keyboard 
before I knew what was happening. A second team mate elects to drop out at the end of
this round.

Zero points for round two. [Possibly broken solution is here](round2/api.py)

## Round Three

There was a break for a while between rounds. Some people are too inebreiated to continue
the contest. It's just me now, and someone has a machine that is surrounding me with
soap bubbles. Everything is getting sticky, which is awful. The round starts, OK. Unlike
the previous rounds there are no difficulty levels. Just `HARD` or nothing. OK, hard mode
it is. The code from round two is similar and can be reused somewhat. There is a man
stomping on the stage and it's shaking so loudly, extremely jarring effect, the worst
thing so far. I notice this challenge has cardinal directions (North, South, East, West)
and I ask someone who tells me something about trying not to bump into a wall? After a while
I notice there is a game board with different colored lines off to the side of the stage... OK 
am red I guess? It becomes apparent to me that I need to "claim" spaces on the board for points.

So I'm sure I have working code, I'm getting good responses from the API. Trying to understand
why my token keeps changing, other various and sundry mini mental side quests. Lost some
not insignificant amount of time since I forgot to switch from the test to the
`production` endpoints.  Show my code to the proctor who agrees it's right but
no one knowns why I don't have points yet. But then... I do suddenly. First 5, then 12,
then I figure out I can change the direction in my API call and as long as a
valid move it will get points. I know I need to go back and automate this loop
by parsing the  JSON for the valid list of next moves
but the clock is running down fast and I am getting points by just changing the
direction manually, then hitting up arrow and enter. 

Round three, 50 or so points earned the hard way. One up arrow at a time.

[Here is my mostly working solution](round3/arena.py)

## Summary

Had a total blast, a definite highlight of the conference for me! Was of course bummed
I couldn't adapt faster and get a better score, but there was so much going on. And
honestly no one is really sure how to get a giant metal decahedron home form the conference
anyway, much to the delight of [Krux](https://twitter.com/krux).

I'm sharing my awful code and explaining as best I can in the hopes that other brave
souls will choose to come forward and rise to the challenge! 

Very much looking forward to next time. :)
