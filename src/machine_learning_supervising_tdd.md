Machine Learning supervising TDD
Ravi Kalia, PhD
Ravi Kalia, PhD
Jul 23 · 6 min read

Photo by Samuel Zeller on Unsplash
Hi folks, I’m coming to Test Driven Development (TDD) from a Machine Learning (ML) background. A few weeks ago I attended @swcraftmontreal talk by the excellent @Khris_Fernandez — we’ve started a conversation.
In software, often our tools are not as good as those we build for customers — the phrase the Cobbler’s children have no shoes is used. We are so busy building tools for customers we often don’t build our own.
Kris mentioned the now ingrained quote Software Is Eating the World but that even now most software is not verified — hence the need for TDD. It made me think of the quote AI Is Eating Software, and so what does this mean for TDD. I sense that there is an application of ML to TDD practice.
TDD Is Desperately Needed in ML
I think TDD is great, I love it.
Definitely has use for writing robust abstracted ML algorithms — although we use the word ‘test’ in a different sense. Also, a Product Manager(PM) may specify the test for a good application specific implementation with probabilistic measures (I want a program which works with 98% accuracy, 90% recall, 95% precision, 80% f1-score in 0.4 seconds, etc — for a classifier solution — something similar can be specified for regression or even reinforcement learning).
It got me thinking about TDD and ML. The idea has been festering, so I’m writing a medium article about it.
Replacing some TDD with ML
TDD is essentially a harness to guide the (Software Engineer)SWE from prose requirements to a sequence of 1 and 0’s (the program) that behaves within the requirements. One might view the whole problem as a supervised learning task (we want to find a solution program which passes all tests — these tests being examples in ML parlance). Some TDD can/will be automated using ML. In other words, an ML algorithm would process tests and then generate a sequence — a supervised sequence model if you will.
I think the big picture of how to replace the subtasks of TDD is as follows:
​0. raw data examples (natural language specs -the PM’s requirements).
1. processed data examples (red failing tests, for now still needs to be SWE defined from specs).
2. learning algorithm (programmer’s brain neural network).
3. training/optimizing step (writing code to make tests go green).
4. regularizing (refactoring code).
A little odd for the ML setting (where batch learning from many examples is the norm), but for each test example shown to the system it can run the learning algorithm and produce a new sequence of 1’s and 0's. That is, performing the learning to create a program from each new test written and for all past tests that have accumulated.
Fruit Cart Totalizer
​In particular with Kris we did a dojo of programming a fruit shopping cart, with increasingly sophisticated tests that it needed to pass. We did tests such as checking that an empty cart totals to 0; that a single fruit from the list costs its unit price; that some given combinations total as expected. Then we got a little more complicated with promotions and membership discounts.
So for that specific case, we could gather a database dump of prices, amounts and totals from receipts from a major retailer (say Walmart). Then the learning algorithm just needs to learn the function that maps from (prices, amounts) to totals for all the examples (or tests) in the database. It could learn all kinds of promotions, membership discounts and conditions just from the examples.
ML Calculator
Another example is this excellent calculator. It is a calculator trained from examples. This calculator is trained from ensembling traditional ML models. The data is examples created from base test templates of addition, subtraction, division and multiplication. The final program is a model with learned weights and we can see it working. It could also be programmed using traditional TDD practice.
​More examples/tests can be added later and the learning algorithm can rewrite the solution to make them green. One might even add them one at a time, or in any groupings suitable.
Criticism: Regularizing Isn’t Really Refactoring
​The regularizing part simplifies the solution, removing or reducing the cruft in the the solution program and ensuring it works on unseen examples from the same test family. This regularization can be interpreted in many ways — its effect is to compress the solution program.
I’ve been shopping the idea around on the software crafters slack channel. One valid criticism is that the program can’t be refactored in the conventional sense as it isn’t expressed as tokens, expressions, functions and classes plain text format. This is true — but if it’s never seen by a human, does it matter?
As long as it works — i.e. passes all tests and maybe some time and space requirements are met, then it’s good software. Incrementally adding more tests is not a problem as the ML algorithm will just learn a new program each time.
Not So Blue Skies Thinking
Of course one might say, well what about when you have no database. Well then this ML powered solution doesn’t apply straight away, we’d need to write the tests first from the prose. Following that, an algorithm can learn a program that passes all the SWE specified tests.
However, one could take this idea 3–10 years in the future and hope for a NLP tool to go from subtask 0 to subtask 1. That is a sophisticated/specially trained sequencer could parse natural language specs and output tests.​
Right now, translating from Japanese to Spanish on Google translate is powered by a ML program, GNMT. Although not perfect, it’s getting close. It shouldn’t be that difficult to input prose from a PM and output tests in a mainstream programming language.
One language that comes to mind is Python. The standard library module doctest applied to docstring tests provide many examples of test right there in the source code— we just need a few million examples. Then to go from Python to any other language could be done via a transpiler.
All of this might even be possible now.
Generating Many Tests (Examples)
For ML algorithms to work well on future unseen examples, they usually need training and tuning — which calls for the examples to be split into at least two disjoint sets. To remedy this, I suspect we’d need more than one instance of a test for a specific feature, at least one in the training test and one in the tuning set (usually called the validation or dev set — but I don’t want to confuse with agile terminology). Ideally we’d want more than 2 examples of this feature, but these should be cheap to create.
Going deeper, these tests are instances of a desired feature — that which is specified in the prose of the PM. So could it be that there is a test generator which maps from arguments of a function to the desired behaviour — the feature. This would be a mapping from types to types — makes me think of categorical type theory. I’m not sure how to push this further…
Conclusion
​There could be significant gain in performance per unit of resource by working in this way. One downside is that the solution program won’t be human intelligible, but if it works does that really matter.
A downside to this approach is that we can’t prove that the program will always be correct, just that we expect it to be correct based on its performance on the tuning set.
One other point is that a SWE is limited to how many tests can be processed — she might get through dozens, let’s say hundreds of tests in a day. By comparison, a ML algorithm should be able to process millions of tests in the blink of an eye. OK, so there should be lots of caveats and big-O notation to qualify this, but fact would remain that the scale of time taken to pass tests with a program is vastly different for Human SWE vs Machine with a smart ML algorithm.
It’s worth considering that ML has traditionally considered as useful for tasks that have a stochastic element or very difficult to write enough tests for. For example, write a program to detect cars from color images — the data being (say 1000 pixels by 1000 pixels) — multidimensional arrays of numbers. One might take a lifetime and never get good enough performance for self driving. This is now solved with ML.
What I’m suggesting is that ML can write programs when there is a battery of tests provided by a PM/SWE, not just for problems with inherent uncertainty.
​So is that a backwards self-driving bicycle :-)
​Or put another way. The. Cobbler’s. Children. Will. Have. Shoes.
Or from another perspective. The. Cobbler’s children don’t need to walk. They. Can. Run. In. Sneakers. Powered by ML of course.
Grateful for comments.
