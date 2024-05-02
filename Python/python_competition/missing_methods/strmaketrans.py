def transcribe_to_mrna(dna):
    translation = str.maketrans('ACGT', 'UGCA')

    return dna.translate(translation)