# Bioinformatics Mini-Project: Pattern Recognition

This was included a mini project in course number 4 of the "Genomic Data Science" MOOC.

This mini-project functions by taking sequenced reads of a genome and running against a given reference genome, finding and returning the number of Matchces found.

________________________________________________________________________________________________________________________________________________________________________________

Mapping is performed with the naive algorithm, with variances:

- The native algorithm possesses functionality by also taking the reverse complement of each read and mapping to the reference genome; if the pattern and it's reverse complement is the same, it will not be included.
- a second function is present which attempts to map to the genome allowing for mismatches to be present: this is important to include such functionality due to changes in quality of the sequence affecting the output to possibly produce errors.

________________________________________________________________________________________________________________________________________________________________________________


To do:

- Prompt the user the amount of mismatches they'd like to include in the pattern
- Reinsert the final function which gave the user a count of how many reads were mapped to the reference genome
-input an example genome+reads
