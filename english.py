import time
import main

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    main.main1()

# Present Tenses
def ps():
    slow_print("""
--- PRESENT SIMPLE ---
Usage:
1. Habits and routines:
   - I wake up at 7 a.m. every day.
   - She goes to the gym on Mondays.

2. General truths and facts:
   - Water boils at 100°C.
   - The Earth orbits the Sun.

3. Timetables and schedules:
   - The train leaves at 6:30.
   - School starts at 8:00.

4. Permanent situations:
   - He works in a bank.
   - They live in New York.

Form:
[Subject + base verb (add 's' or 'es' for he/she/it)]

Examples:
- I eat breakfast at 8.
- She studies English every day.
""")

def pc():
    slow_print("""
--- PRESENT CONTINUOUS ---
Usage:
1. Actions happening right now:
   - I am reading a book.
   - They are watching a movie.

2. Temporary actions or situations:
   - She is staying with her friend this week.
   - We are living in London for the summer.

3. Future arrangements:
   - I am meeting my cousin tomorrow.
   - We are flying to Spain next weekend.

Form:
[Subject + am/is/are + verb + -ing]

Examples:
- He is talking on the phone.
- We are studying for the exam.
""")

def pp():
    slow_print("""
--- PRESENT PERFECT ---
Usage:
1. Actions that happened at an unspecified time:
   - I have seen that movie before.
   - They have visited Paris.

2. Actions that started in the past and continue to now:
   - She has worked here since 2020.
   - We have lived in this city for 10 years.

3. Recent events with results in the present:
   - He has broken his arm. (He still has a broken arm.)
   - I have lost my keys. (I still can't find them.)

Form:
[Subject + have/has + past participle]

Examples:
- I have finished my homework.
- She has never eaten sushi.
""")

def ppc():
    slow_print("""
--- PRESENT PERFECT CONTINUOUS ---
Usage:
1. Actions that began in the past and are still happening:
   - I have been studying all morning.
   - They have been playing football for 2 hours.

2. Recent actions with visible results:
   - She is tired because she has been working all day.
   - He has been crying. (His eyes are red.)

Form:
[Subject + have/has been + verb + -ing]

Examples:
- We have been waiting for 30 minutes.
- He has been learning English since January.
""")

# Past Tenses
def pas():
    slow_print("""
--- PAST SIMPLE ---
Usage:
1. Completed actions in the past:
   - I visited my grandmother last week.
   - He finished the book yesterday.

2. Specific time in the past:
   - They arrived at 8:00 p.m.
   - She graduated in 2020.

3. Series of past actions:
   - He opened the door, turned on the light, and walked in.

Form:
[Subject + past verb]

Examples:
- We watched a movie last night.
- She studied math all day.
""")

def pac():
    slow_print("""
--- PAST CONTINUOUS ---
Usage:
1. Ongoing actions at a specific time in the past:
   - At 5 PM, I was cooking dinner.
   - They were studying at 10 PM.

2. Interrupted actions:
   - I was sleeping when the phone rang.
   - She was watching TV when he arrived.

3. Parallel actions:
   - I was reading while he was writing.

Form:
[Subject + was/were + verb + -ing]

Examples:
- He was driving home when it started to rain.
- We were playing football all afternoon.
""")

def pap():
    slow_print("""
--- PAST PERFECT ---
Usage:
1. An action completed before another past action:
   - I had eaten before they arrived.
   - She had finished the test when the bell rang.

2. Showing cause and effect in the past:
   - He was tired because he had not slept well.
   - They were late because they had missed the bus.

Form:
[Subject + had + past participle]

Examples:
- We had never seen that place before.
- He had already left when I got there.
""")

def papc():
    slow_print("""
--- PAST PERFECT CONTINUOUS ---
Usage:
1. Duration of an action before another past event:
   - I had been studying for 3 hours before he called.
   - They had been working all day when the storm started.

2. Cause and result in the past:
   - She was crying because she had been arguing with her friend.

Form:
[Subject + had been + verb + -ing]

Examples:
- He had been traveling for weeks when he got sick.
- We had been waiting for a long time before the doors opened.
""")

# Future Tenses
def fs():
    slow_print("""
--- FUTURE SIMPLE ---
Usage:
1. Predictions:
   - It will snow tomorrow.
   - People will live on Mars one day.

2. Instant decisions:
   - I'm tired. I will go to bed.
   - I’ll call you back later.

3. Promises and offers:
   - I will help you with your homework.
   - Don’t worry, I’ll take care of it.

Form:
[Subject + will + base verb]

Examples:
- We will travel to Italy next summer.
- She will be fine.
""")

def fc():
    slow_print("""
--- FUTURE CONTINUOUS ---
Usage:
1. Ongoing action at a future time:
   - This time next week, I will be lying on the beach.
   - At 8 PM, they will be watching the movie.

2. Future events that are expected to happen:
   - Don’t call at 9. I’ll be driving.

Form:
[Subject + will be + verb + -ing]

Examples:
- She will be studying all night.
- We will be staying at a hotel in London.
""")

def fp():
    slow_print("""
--- FUTURE PERFECT ---
Usage:
1. Completed actions before a certain future time:
   - By next month, I will have finished the book.
   - He will have arrived by 10 a.m.

2. Expectations of results in the future:
   - She will have completed the course by then.

Form:
[Subject + will have + past participle]

Examples:
- They will have built the house by summer.
- I will have cleaned everything before you arrive.
""")

def fpc():
    slow_print("""
--- FUTURE PERFECT CONTINUOUS ---
Usage:
1. Duration of an ongoing action before a future time:
   - By 5 PM, I will have been working for 8 hours.
   - She will have been living in New York for 10 years by 2026.

2. Emphasizing how long something has been happening:
   - We will have been waiting for an hour by the time they get here.

Form:
[Subject + will have been + verb + -ing]

Examples:
- He will have been studying for 6 months before the exam.
- They will have been driving for hours by midnight.
""")
