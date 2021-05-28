### Merge the tools!
Consider the following:

A string, **_s_**, of length **_n_** where **_<code>s = c<sub>0</sub>c<sub>1</sub>...c<sub>n-1</sub></code>_**.<br />
An integer, **_k_**, where **_k_** is a factor of **_n_**.<b />
We can split **_s_** into **_n/k_** substrings where each subtring, **_t<sub>i</sub>_**, consists of a contiguous block of **_k_** characters in **_s_**. Then, use each **_t<sub>i</sub>_** to create string  such that:

The characters in **_u<sub>i</sub>_** are a subsequence of the characters in **_t<sub>i</sub>_**.<br />
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

<br />
Task source: [HackerRank](https://www.hackerrank.com)