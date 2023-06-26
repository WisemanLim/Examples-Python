import pysam
import vcfpy as vcf

# FASTQ 파일 경로와 출력 BAM 파일 경로를 지정합니다.
fastq_file = "12001_R1.fastq" # "example.fastq"

fasta_file = pysam.FastaFile(fastq_file)
vcf_file = pysam.VCFWriter("example.vcf", fasta_file.references, fasta_file.pileup())

""" replace code above : VCFWriter
for reference_name in fasta_file.references:
    for pileupcolumn in fasta_file.pileup(reference_name):
        position = pileupcolumn.pos
        ref_base = pileupcolumn.reference_base
        alt_base = set(pileupread.alignment.query_sequence[pileupread.query_position] for pileupread in pileupcolumn.pileups if not pileupread.is_del and not pileupread.is_refskip)
        if alt_base:
            vcf_record = pysam.VariantRecord(
                reference_name,
                position,
                alleles=[ref_base] + list(alt_base),
                id=".",
                qual=0,
                filter="PASS",
                info={},
                format="GT",
                samples=[]
            )
            vcf_file.write(vcf_record)
fasta_file.close()
vcf_file.close() """

# 예시로 알려드린 SNP position 정보 20개를 리스트에 저장합니다.
snp_positions = [1234567, 2345678, 3456789, 4567890, 5678901, 
                 6789012, 7890123, 8901234, 9012345, 12345678, 
                 23456789, 34567890, 45678901, 56789012, 67890123, 
                 78901234, 89012345, 90123456, 123456789, 234567890]

# 검색할 VCF 파일과 필요한 컬럼 정보를 지정합니다.
# vcf_file = "GCA_000001215.4_current_ids.vcf"
vcf_columns = ["CHROM", "POS", "REF", "ALT", "GENE"]

# VCF 파일을 파싱하여 SNP position 정보가 일치하는 레코드를 찾습니다.
with open(vcf_file, 'r') as f:
    vcf_reader = vcf.Reader(f)
    for record in vcf_reader:
        if record.POS in snp_positions:
            chrom = record.CHROM
            pos = record.POS
            ref = record.REF
            alt = record.ALT
            gene = record.INFO.get("GENE", "")

            # 필요한 정보를 출력합니다.
            print(f"SNP position {pos} is found in gene {gene} on chromosome {chrom}.")
            print(f"The reference allele is {ref} and the alternative allele is {alt}.\n")
