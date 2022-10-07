import Bio.Data.CodonTable
from Bio.Seq import Seq

def complementary_conversion():
    x = input("Please enter DNA :  ")
    my_seq = Seq(x)
    complement = my_seq.complement()
    print("Complementary DNA is:    " + complement)

def reverse_complementary_conversion():
    x = input("Please enter DNA :  ")
    coding_dna = Seq(x)
    transcribe = coding_dna.reverse_complement()
    print("Reverse complementary DNA is:    " + transcribe)

def transcribe_conversion():
    x = input("Please enter DNA :  ")
    sequence = Seq(x)
    mRNA = sequence.transcribe()
    print("Transcribed DNA is:    " + mRNA)

def all_operations():
    x = input("Please enter DNA :  ")
    my_seq = Seq(x)
    complement = my_seq.complement()
    print("Complementary DNA is:    " + complement)
    coding_dna = Seq(x)
    transcribe = coding_dna.reverse_complement()
    print("Reverse complementary DNA is:    " + transcribe)
    sequence = Seq(x)
    mRNA = sequence.transcribe()
    print("Transcribed DNA is:    " + mRNA)


def chart():
    sequence = "AUGGGUACCCUAAUACUAGUCCUAAAAAGC"
    length = len(sequence)
    codons = []
    for i in range(0,30,3):
        codon = sequence[i:i+3]
        print(codon)
        codons.append(codon)
        print(codons)
        codons.count('CCU')
        codons.count('AUG')
        stop_codon1 = codons.count('UGA')
        stop_codon2 = codons.count('UAA')
        stop_codon3 = codons.count('UAA')
        total_stop = (stop_codon1 + stop_codon2 + stop_codon3)
        print(total_stop)

def repeat():
    answer = input("Repeat y/n:  ")
    if answer == 'y':
        main()
    else:
        quit()

# triggers
complementary_triggers = ["1"]
reverse_complementary_triggers =["2"]
transcribe_triggers = ["3"]
all_triggers = ["4"]

def main():
    choices = ["1. Complementary", "2. Reverse", "3. Transcribe", "4. All"]
    print("Possible choices : " )
    print(choices)
    operation = input("Please select operation by number:    ")

    if operation in complementary_triggers:
        complementary_conversion()
    if operation in reverse_complementary_triggers:
        reverse_complementary_conversion()
    if operation in transcribe_triggers:
        transcribe_conversion()
    if operation in all_triggers:
        all_operations()
    repeat()
chart()
main()
