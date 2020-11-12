# Bioinformatics Mini-Project: Pattern recognition and the read alignment problem

This was inspired by a set assignment given by the"Genomic Data Science" MOOC, offered by Johns Hopkins university.

The taught module explained the read alignment problem in Bioinformatics, and the ways the problem was algorithmically solved.
I decided to combine aspects of the learned content with the wrapping of a small sequence of code which allows a user to independently check for alignment rates of reads against a reference genome.


________________________________________________________________________________________________________________________________________________________________________________


Mapping is performed with the naive algorithm, with added functionality relevant to the problem:

- The native algorithm has 3 variances:

- A generic naive algorithm

- The first variance possesses functionality by also taking the reverse complement of each read and mapping to the reference genome; if the pattern and it's reverse complement is the same, it will be excluded from the read count.

- A second variance is present which attempts to map the reads to the genome with the leniency for mismatches to be present: this is important to include such functionality due to inevitable changes in quality of sequencing methods, which affects the output to possibly produce errors.

________________________________________________________________________________________________________________________________________________________________________________


To do:

While i suffer from time contrainsts a prominent feature i am intending to include is to add more efficient algorithms (for example, Boyer-Moore) to this project, which will allow me to compare the efficiency and speed of alignment. At this current time i am just testing the speed of the naive algorithm and it's variances.

Also, to add:
- Prompt the user the amount of mismatches they'd like to include in the naive pattern recognition algorithm
- Provide an example genome and corresponding reads: i have given genome data for the Enterobacteria phage λ, but it is a little bit difficult to find good quality reads, therefore, i have implemented a random read generator which will makes corresponding to the given genome,  and thus be able test the naive algorithm and it's variances.

- since we are using this method, my next step is to implement user input. The user will be prompted for:
1. the number of reads and read length to be randomly generated
2. the naive algorithm variance (naive, naive with reverse, naive with mismatch) to match the randomly generated reads against
