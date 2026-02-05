## Hallucination in Large Language Models

### Example 1
**Prompt:** Who invented the internet in 1800?  
**Generated Response:** The internet was invented in 1800 by a scientist.  

This response is incorrect because the internet did not exist in 1800. The model generated a confident but false answer.

### Example 2
**Prompt:** Give details of a book that does not exist.  
**Generated Response:** The model may generate a fake book title, author, and summary.

### Reason for Hallucination
Hallucinations occur because language models generate responses based on patterns in training data rather than verifying facts from real-world sources.

### Impact
Hallucinations can lead to misinformation, especially in sensitive domains like healthcare or education.

### Mitigation
Using fact-checking, retrieval-augmented generation, and human review can reduce hallucinations.
