## Purpose

Our goal is to optimize a resume with given resume and job descriptions. For that we have parser, job analyst, gap analyzer, rewriter, and critic agents.

## Methodology

To do that, I'll run parser parallel with job analyzer and compare their results with gap analyzer. Then we'll have a eval-optimizer loop with rewriter and critic agents. 

This is a workflow with one bounded loop. I got a predetermined process and all the order of the processes are clear without any exception.

I'll use LangGraph for orchestiration as it is widely used and a wanted skill to have.

I am planning to use Anthropic as the model provider just because I loaded 100$ to it by accident and would like to use it. However, I am not sure about its performance on certain things. If there's a cheap and effective alternative, I might use that too.


## Rules

Do not EVER add new things to the resume. Only rephrase or reorder things. If time allows I might add a feature that asks user for certain details (eg. ask user to provide how many users using his/her website to show it more attractive.)

