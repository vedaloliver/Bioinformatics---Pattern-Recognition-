# Bioinformatics Mini-Project: Pattern recognition and the read alignment problem

This was inspired by a set assignment given by the"Genomic Data Science" MOOC, offered by Johns Hopkins university.

The taught module explained the read alignment problem in Bioinformatics, and the ways the problem was algorithmically solved.
I decided to combine aspects of the learned content with the wrapping of a small sequence of code which allows a user to independently check for alignment rates of reads against a reference genome.


________________________________________________________________________________________________________________________________________________________________________________


Mapping is performed with the naive algorithm, with added functionality relevant to the problem:

- The native algorithm possesses functionality by also taking the reverse complement of each read and mapping to the reference genome; if the pattern and it's reverse complement is the same, it will not be included.

- A second function is present which attempts to map to the genome allowing for mismatches to be present: this is important to include such functionality due to changes in quality of the sequence affecting the output to possibly produce errors.

________________________________________________________________________________________________________________________________________________________________________________


To do:

While i suffer from time contrainsts a prominent feature i am intending to include is to add more efficient algorithms (for example, Boyer-Moore) to this project, which will allow me to compare the efficiency and speed of alignment.

Also, to add:
- Prompt the user the amount of mismatches they'd like to include in the naive pattern recognition algorithm
- Reinsert the final function which provides the user with a count of how many reads were successfully mapped to the reference genome
- Provide an example genome and corresponding reads
