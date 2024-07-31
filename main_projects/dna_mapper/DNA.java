/**
 * CS 1 22fa MP 7 Parts B/C
 * Porting Classes in Python and Java
 * Student name: Nyasha Makaya
 * Starter code for DNA.java
 * @author (original): El Hovik and Adam Abbas
 * 
 * This class represents a DNA sequence comprised of A', 'C', 'G', 'T' 
 * nucleotides. The class supports simple methods to represent the sequence 
 * as a String, get a complement sequence, compute information about
 * nucleotide counts and percentages, and transcription and translation to
 * mRNA and polypeptide Strings (chains of amino acids).
 */
import java.util.Random;

public class DNA {
    // String of DNA base characters in upper-case
    private String seq;
    // For the optional B.6. exercise
    private static Random mutator = new Random();
    private static final double MUTATION_RATE = 0.1;

    /**
     * Initializes a new (single-strand) DNA sequence using the provided 
     * seq String. A DNA sequence contains a sequence of the 4 DNA base 
     * nucleotides, 'A', 'T', 'C', 'G' (standardized to uppercase).
     * 
     * @param seq - sequence of 'A', 'T', 'C', 'G' bases.
     * @throws IllegalArgumentException if the sequence
     * is not comprised of ATCG nucleotide bases.
     */
    public DNA(String seq) {
        String sequence = seq.toUpperCase();
        for (int i = 0; i < sequence.length(); i++)
            if (sequence.charAt(i) != 'A' && sequence.charAt(i) != 'T' &&
            sequence.charAt(i) != 'C' && (sequence.charAt(i) != 'G')) 
            {
                throw new IllegalArgumentException("Invalid DNA sequence. Must only contain ATCG bases.");
            }
        this.seq = sequence;

    }

    /**
     * Returns the string representation of the DNA sequence,
     * defined as the sequence of nucleotide bases.
     * 
     * @return string sequence of nucleotide bases
     */
    public String toString() { 
        //B.2a 
        return this.seq;
    }

    /**
     * Returns the size of the DNA sequence, defined as the number of 
     * nucleotide bases it contains.
     * 
     * @return - number of bases in the sequence
     */
    public int size() { 
        String seq = this.seq;
        return seq.length();
    }

    /**
     * (Provided private helper method, do not change)
     * Returns the complement of the provided base character,
     * ignoring letter-case (the complement is returned in upper-case).
     * 
     * @param base - nucleotide base
     * 
     * @return - complement of `base`, in upper-case.
     * 
     * @throws IllegalArgumentException if the passed base
     * is not a valid DNA nucleotide base character.
     */
    private static char baseComplement(char base) {
        // to upper-case a char in Java, we need to use
        // the Character class.
        base = Character.toUpperCase(base);
        if (base == 'A') {
            return 'T';
        } else if (base == 'T') {
            return 'A';
        } else if (base == 'C') {
            return 'G';
        } else if (base == 'G') {
            return 'C';
        } else {
            String errMsg = "Invalid base.";
            throw new IllegalArgumentException(errMsg);
        }
    }

    /**
     * Returns the compliment DNA sequence. For example, if this DNA
     * is comprised of the bases 'ATACGC', its complement is returned as
     * 'TATGCG'.
     * 
     * @return the complement DNA sequence.
     */
    public String complement() {
        String result = "";
        for (int i = 0; i < this.seq.length(); i++)
            result += DNA.baseComplement(this.seq.charAt(i));
        return result;
    }

    /**
     * Returns the number of occurrences of the given nucleotide base,
     * ignoring letter-casing.
     *
     * @param base nucleotide base char (one of ATCG)
     *
     * @return count of given base in this sequence
     *
     * @throws IllegalArgumentException if given an invalid base
     */
    public int countOccurrences(char base) {
        int result = 0;
        base = Character.toUpperCase(base);
        if (base != 'A' && base != 'T' && base != 'C' && base != 'G') 
        {
            throw new IllegalArgumentException("Invalid base.");
        }
        for (int i = 0; i < this.seq.length(); i++)
            if (this.seq.charAt(i) == base)
            {
                result += 1;
            }

        return result;
    }

    /**
     * Returns the percentage of the given base (ignoring
     * letter-casing) in this DNA sequence as a float value
     * between 0.0 and 1.0. (100%). Note that the percentage of any
     * valid base in an empty DNA will be considered 0.0 (but the base
     * validation will take precedence).
     * 
     * @param base nucleotide base char (one of ATCG)
     * 
     * @return Percentage of base between 0.0 and 1.0
     * 
     * @throws IllegalArgumentException if given an invalid base
     */
    public double percentageOf(char base) {
        double occurences = this.countOccurrences(base);
        System.out.println(occurences);
        if (occurences == 0)
        {
            return 0.0;
        }
        return occurences / this.seq.length(); 
        
        
    }

    /**
     * Transcribes the current DNA sequence to mRNA, by 
     * taking the complement of all of the bases and 
     * switching the "T" nucleotide to "U".
     * 
     * @return the transcribed mRNA
     */
    public mRNA transcribe() { 
        String compl = this.complement();
        String newSeq = compl.replace('T', 'U');
        return new mRNA(newSeq);
    }

    /**
     * Translates the current DNA to an Amino Acid chain by 
     * transcribing to an RNA chain, finding the start codon 
     * ("AUG") and then parsing 3-letter codons and looking
     * up their respective amino acids in the "codon.txt" files.
     * 
     * @return full string of translated Amino Acids
     */
    public String translate() {
        //C.2.2
        mRNA newStrand = this.transcribe();
        return newStrand.toPolypeptide();
        
    }

    /**
     * Optional B.6.
     */
    public DNA mutate(int mutationTime) {
        String mutatedSeq = this.seq;
        // Provided pseudocode:
        // For mutationTime times:
        // if mutator.nextDouble() < MUTATION_RATE
        // randomly select an index of the mutatedSeq, and
        // replace mutatedSeq with the prefix (unchanged), the complement
        // of the randomly-selected character, and the suffix (unchanged)
        // Note that the result String should have the same length as this.seq
        // and this.seq should not be changed as a result of this method.
        

        return new DNA(mutatedSeq);
    }
}
