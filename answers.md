# CMPS 2200 Recitation 04
## Answers

**Name:**Lily Goldman


Place all written answers from `recitation-04.md` here for easier grading.

- **4) (2 pts)** Assume that a word `w` appears `n` times. What is the **work** and **span** of `word_count_reduce` for this word, assuming a parallel implementation of the `reduce` function?


 **Work: $\Theta(n)$. Span: $\Theta(\log n)$.**

  **Work** is the total number of additions. `reduce` splits the list in half, adds up each half, then adds those two answers together. Every number in the list has to be added in eventually, so this takes $n - 1$ additions no matter what, which is $\Theta(n)$.

  **Span** is how long it takes if we have as many processors as we want. The two halves do not depend on each other, so they can run at the same time. That means we only wait for one half, not both. Each step cuts the list size in half, so after $\log n$ steps we are down to a single number. The span is $\Theta(\log n)$.

- **5) (2 pts)** What is the problem that prevents us from easily parallelizing this solution?

 **The `counts` dictionary is shared, and each update depends on the one before it.**

  The line `counts[term] = counts.get(term, 0) + 1` does three things in order: read the current count, add one to it, and write it back.

  If two processors handle the word `sam` at the same time, both might read the same old count, say 4. Both add one and both write back 5. The real answer should be 6, so one of the counts is lost.

  This means the loop steps are not independent. Each one has to see the result of the step before it, so we cannot safely split the work across processors. 