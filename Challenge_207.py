DNA_Pairs = {'A': 'T', 'C': 'G', 'T': 'A', 'G' : 'C'}
CODON_pairs = {
'TTT': "Phe", 'TTC': "Phe", 'TTA': 'Leu', 'TTG': 'Leu', 'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu', 'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile', 'ATG': 'Met',
'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val', 'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser',
'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro', 'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala', 'TAT': 'Tyr', 'TAC': 'Tyr', 'TAC': 'Tyr', 'TAA': 'Stop',
'CAT': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 'AAT': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
'GAT': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', 'TGT': 'Cys', 'TGC': 'Cys', 'TGA': 'Stop', 'TGG': 'Trp',
'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGT': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', 'TAG': 'Stop'}

def pair(sequence):
	paired = []
	for char in sequence:
		paired.append(DNA_Pairs[char.upper()])
	print paired

def codon(sequence):

	codons = []
	if len(sequence) % 3 != 0:
		print "Invalid sequence, must be in 3's"
		exit()
	if sequence[0:3] != 'ATG':
		print "Invalid sequence, must start with ATG (Met codon)"
		exit()

	for i in range(0, len(sequence) - 2, 3):
		codon = sequence[i:i+3]
		codons.append(CODON_pairs[codon.upper()])
		if CODON_pairs[codon.upper()] == 'Stop':
			break

	print codons

def main():
	codon(raw_input('Please enter DNA sequence for pairing:'))

if __name__ == '__main__':
	main()
