# MIT 6.006 L1 Algorithms and Computation

|__________________________________________|

[Lecture 1. Algorithms and Computation](https://www.youtube.com/watch?v=ZA-tUyM_y7s&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&ab_channel=MITOpenCourseWare)

<ul>
    <li><a href="#u1">1. GOALs</a></li>
    <li><a href="#u2">2. Problem</a></li>
    <li><a href="#u3">3. Algorithms</a></li>
    <li><a href="#u4">4. Correctness</a></li>
    <li><a href="#u5">5. Asymptotic Notation</a></li>
    <li><a href="#u6">6. Memory Address</a></li>
</ul>

<h2 id="u1">1. GOALs</h2>

<pre><code>
<b><u>GOALs</u></b>
1) <u>Solve compputaional problems;</u>
2) <u>Prove correctness;</u>
3) <u>Argue effieciency;</u>
4) <u>Communication;</u>
</code></pre>

<h2 id="u2">2. Problem</h2>

<pre><code>
<b><u>Problem</u></b>

INPUTS              OUTPUTS
0--------------------o
0--------------------o
0--------------------o
0--------------------o

o. The size of INPUTS can grow more and more larger, so we need a fixed sized algorithm for our general problem.
Not just a specific case of the problem.
</code></pre>

<h2 id="u3">3. Algorithms</h2>

<pre><code>
<b><u>Algorithms</u></b>
o. Function : Input = Output
o. f : I = O

o.  For Birthday problem:
    Maintain a record;
    Interview students in order;
        - Check if birthday in record;
            - If so return pair
        - If not add birthday to record;
    Return it;

</code></pre>

<h2 id="u4">4. Correctness</h2>

<pre><code>
<b><u>Correctness</u></b>
Inductive Hypothesis :
    If first k students contain match then
        Alg returns a match before interview;
            student k +1;

</code></pre>

<h2 id="u5">4. Efficiency</h2>

<pre><code>
<b><u>Correctness</u></b>
o. We don't mesure time, insted count Operations;
o. Asymptotic Analysis
o. Expect performance to depend on size of the inputs;
o. Asymptotic Notation:
   o. O() upper bound
   o. Ω() lower bound
   o. Θ() Both
</code></pre>

<h2 id="u5">5. Asymptotic Notation</h2>
<pre><code>
<b><u>Asymptotic Notation</u></b>
Θ(1) Θ(lg n)  Θ(n)  Θ(n2)  Θ(n lg n)
^ 1000
|           / 1 linear
|         /
|       /
|     /
|   /
| /
|-----------------------> Θ(n) good
|-----------------------> Θ(lg n) is almost as good as a constant good
------------------------->Θ(1) good

</code></pre>

<h2 id="u5">6. Memory Address</h2>
<pre><code>
<b><u>Memory Address</u></b>
o. 8bits = 1 Byte
o. RAM - Random Access Memory
o. x32 bits -> 2 to 32 -> 4Gb
o. x64 bits -> 20 ExaBita -> More then Google , so it's enough for now;
<b><u>Operations</u></b>
o. Arithmetic Operators
o. Logical Operators
o. Bitwise Operators
</code></pre>
