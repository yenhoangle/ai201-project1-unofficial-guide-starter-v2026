# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
I allow missing one answer in my criteria because the questions I ask do not have the exact information in one sentence. Since the question pool size is small, I can accept one scenario that the retrieved chunks will not contain all the information to get my answer perfectly.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
I expect all of the system’s answers to be only based on the information in the city guides documents that the system retrieved from and not from outside or hallucinated sources, so having this criteria is a way for me to check whether the system is running smoothly or not.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
Since the out of scope criteria is based on distance between data points, questions about cities or recommendations might falsely pass the gate. One false pass is not a concern because the success rate is still 80% which is acceptable to me without further refinements, but it will be a concern if the gate allows for 2 or more irrelevant questions to pass because then the gate will be too lenient (40%+ fail rate). Having a high success rate for the relevance gate is important in obtaining the correct answers from the existing city guides corpus as well as saving unnecessary time and token cost from attempting to fetch information that is not there. 

---

## 4. Chunks do not contain too many headers

For 5 out of 5 chunks, chunks do not contain more than two topic headers.



**Why this target:**
The city guides are split into small sections with topic headers clearly labeled before the city information (ex: “Eat and drink”, “What to see”). Since the sections are short and are not all related, chunks with 3 topic headers in them are considered to be excessive. Allowing two headers is acceptable because a few sections are only a sentence or two long.


---

## 5. City names must be accurate

For every answer, if a city name is mentioned, the city name should be the same name as mentioned in the corpus.



**Why this target:**
Since the corpus maintains consistent naming conventions, the answers given must also maintain consistent naming conventions to prevent confusion. This criteria must not miss even once since it is expected that all answers are only based on information given in the corpus. If Halden Bay is the correct answer expected, then Halden Port should not be acceptable since it is not a real place mentioned in the guides. 


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
