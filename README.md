README

trimmomatic PE XXX_R1_001.fastq.gz XXX_R2_001.fastq.gz XXX_R1_pe.fastq XXX_R1_se.fastq XXX_R2_pe.fastq XXX_R2_se.fastq ILLUMINACLIP:/mnt/z/2020/Paul_Scripts/adapters.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36


bwa mem \
        -t 10 \
        -Y \
        -R '@RG\tID:RRR\tLB:string\tPL:string\tPM:string\tSM:rrr' \
        YYY \
        XXX \
        XXX \
        > XXX.sam


samtools view -b -o XXX.bam XXX.sam
samtools sort -o XXX.sorted.bam XXX.bam
samtools index -b XXX.sorted.bam

##IF MULTIPLE ALIGNMENT FILES REPRESENT SINGLE POPULATION -->> MERGE FILES INTO ONE###
##ALLOWS FASTER PIPELINES##

samtools merge XXX.merged.bam XXX*sorted.bam
samtools index -b XXX.merged.bam



##SPLIT FILES FOR FREEBAYES####


samtools view -h XXX 'lcl|Scaffold_1':0-2499999 -b > XXX_SN:lcl_Scaffold_1_0split.bam
samtools view -h XXX 'lcl|Scaffold_1':2500000-4999999 -b > XXX_SN:lcl_Scaffold_1_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':5000000-7499999 -b > XXX_SN:lcl_Scaffold_1_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':7500000-9999999 -b > XXX_SN:lcl_Scaffold_1_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':10000000-12499999 -b > XXX_SN:lcl_Scaffold_1_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':12500000-14999999 -b > XXX_SN:lcl_Scaffold_1_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':15000000-17499999 -b > XXX_SN:lcl_Scaffold_1_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':17500000-19999999 -b > XXX_SN:lcl_Scaffold_1_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':20000000-22499999 -b > XXX_SN:lcl_Scaffold_1_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':22500000-24999999 -b > XXX_SN:lcl_Scaffold_1_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':25000000-27499999 -b > XXX_SN:lcl_Scaffold_1_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':27500000-29999999 -b > XXX_SN:lcl_Scaffold_1_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':30000000-32499999 -b > XXX_SN:lcl_Scaffold_1_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':32500000-34999999 -b > XXX_SN:lcl_Scaffold_1_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':35000000-37499999 -b > XXX_SN:lcl_Scaffold_1_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':37500000-39999999 -b > XXX_SN:lcl_Scaffold_1_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':40000000-42499999 -b > XXX_SN:lcl_Scaffold_1_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':42500000-44999999 -b > XXX_SN:lcl_Scaffold_1_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':45000000-47499999 -b > XXX_SN:lcl_Scaffold_1_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':47500000-49999999 -b > XXX_SN:lcl_Scaffold_1_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':50000000-52499999 -b > XXX_SN:lcl_Scaffold_1_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':52500000-54999999 -b > XXX_SN:lcl_Scaffold_1_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':55000000-57499999 -b > XXX_SN:lcl_Scaffold_1_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':57500000-59999999 -b > XXX_SN:lcl_Scaffold_1_57500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':60000000-62499999 -b > XXX_SN:lcl_Scaffold_1_60000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':62500000-64999999 -b > XXX_SN:lcl_Scaffold_1_62500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':65000000-67499999 -b > XXX_SN:lcl_Scaffold_1_65000000split.bam
samtools view -h XXX 'lcl|Scaffold_1':67500000-69999999 -b > XXX_SN:lcl_Scaffold_1_67500000split.bam
samtools view -h XXX 'lcl|Scaffold_1':70000000-72499999 -b > XXX_SN:lcl_Scaffold_1_70000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':0-2499999 -b > XXX_SN:lcl_Scaffold_2_0split.bam
samtools view -h XXX 'lcl|Scaffold_2':2500000-4999999 -b > XXX_SN:lcl_Scaffold_2_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':5000000-7499999 -b > XXX_SN:lcl_Scaffold_2_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':7500000-9999999 -b > XXX_SN:lcl_Scaffold_2_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':10000000-12499999 -b > XXX_SN:lcl_Scaffold_2_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':12500000-14999999 -b > XXX_SN:lcl_Scaffold_2_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':15000000-17499999 -b > XXX_SN:lcl_Scaffold_2_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':17500000-19999999 -b > XXX_SN:lcl_Scaffold_2_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':20000000-22499999 -b > XXX_SN:lcl_Scaffold_2_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':22500000-24999999 -b > XXX_SN:lcl_Scaffold_2_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':25000000-27499999 -b > XXX_SN:lcl_Scaffold_2_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':27500000-29999999 -b > XXX_SN:lcl_Scaffold_2_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':30000000-32499999 -b > XXX_SN:lcl_Scaffold_2_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':32500000-34999999 -b > XXX_SN:lcl_Scaffold_2_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':35000000-37499999 -b > XXX_SN:lcl_Scaffold_2_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':37500000-39999999 -b > XXX_SN:lcl_Scaffold_2_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':40000000-42499999 -b > XXX_SN:lcl_Scaffold_2_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':42500000-44999999 -b > XXX_SN:lcl_Scaffold_2_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':45000000-47499999 -b > XXX_SN:lcl_Scaffold_2_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':47500000-49999999 -b > XXX_SN:lcl_Scaffold_2_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':50000000-52499999 -b > XXX_SN:lcl_Scaffold_2_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':52500000-54999999 -b > XXX_SN:lcl_Scaffold_2_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':55000000-57499999 -b > XXX_SN:lcl_Scaffold_2_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':57500000-59999999 -b > XXX_SN:lcl_Scaffold_2_57500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':60000000-62499999 -b > XXX_SN:lcl_Scaffold_2_60000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':62500000-64999999 -b > XXX_SN:lcl_Scaffold_2_62500000split.bam
samtools view -h XXX 'lcl|Scaffold_2':65000000-67499999 -b > XXX_SN:lcl_Scaffold_2_65000000split.bam
samtools view -h XXX 'lcl|Scaffold_2':67500000-69999999 -b > XXX_SN:lcl_Scaffold_2_67500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':0-2499999 -b > XXX_SN:lcl_Scaffold_3_0split.bam
samtools view -h XXX 'lcl|Scaffold_3':2500000-4999999 -b > XXX_SN:lcl_Scaffold_3_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':5000000-7499999 -b > XXX_SN:lcl_Scaffold_3_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':7500000-9999999 -b > XXX_SN:lcl_Scaffold_3_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':10000000-12499999 -b > XXX_SN:lcl_Scaffold_3_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':12500000-14999999 -b > XXX_SN:lcl_Scaffold_3_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':15000000-17499999 -b > XXX_SN:lcl_Scaffold_3_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':17500000-19999999 -b > XXX_SN:lcl_Scaffold_3_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':20000000-22499999 -b > XXX_SN:lcl_Scaffold_3_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':22500000-24999999 -b > XXX_SN:lcl_Scaffold_3_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':25000000-27499999 -b > XXX_SN:lcl_Scaffold_3_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':27500000-29999999 -b > XXX_SN:lcl_Scaffold_3_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':30000000-32499999 -b > XXX_SN:lcl_Scaffold_3_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':32500000-34999999 -b > XXX_SN:lcl_Scaffold_3_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':35000000-37499999 -b > XXX_SN:lcl_Scaffold_3_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':37500000-39999999 -b > XXX_SN:lcl_Scaffold_3_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':40000000-42499999 -b > XXX_SN:lcl_Scaffold_3_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':42500000-44999999 -b > XXX_SN:lcl_Scaffold_3_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':45000000-47499999 -b > XXX_SN:lcl_Scaffold_3_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':47500000-49999999 -b > XXX_SN:lcl_Scaffold_3_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':50000000-52499999 -b > XXX_SN:lcl_Scaffold_3_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':52500000-54999999 -b > XXX_SN:lcl_Scaffold_3_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':55000000-57499999 -b > XXX_SN:lcl_Scaffold_3_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':57500000-59999999 -b > XXX_SN:lcl_Scaffold_3_57500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':60000000-62499999 -b > XXX_SN:lcl_Scaffold_3_60000000split.bam
samtools view -h XXX 'lcl|Scaffold_3':62500000-64999999 -b > XXX_SN:lcl_Scaffold_3_62500000split.bam
samtools view -h XXX 'lcl|Scaffold_3':65000000-67499999 -b > XXX_SN:lcl_Scaffold_3_65000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':0-2499999 -b > XXX_SN:lcl_Scaffold_4_0split.bam
samtools view -h XXX 'lcl|Scaffold_4':2500000-4999999 -b > XXX_SN:lcl_Scaffold_4_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':5000000-7499999 -b > XXX_SN:lcl_Scaffold_4_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':7500000-9999999 -b > XXX_SN:lcl_Scaffold_4_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':10000000-12499999 -b > XXX_SN:lcl_Scaffold_4_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':12500000-14999999 -b > XXX_SN:lcl_Scaffold_4_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':15000000-17499999 -b > XXX_SN:lcl_Scaffold_4_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':17500000-19999999 -b > XXX_SN:lcl_Scaffold_4_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':20000000-22499999 -b > XXX_SN:lcl_Scaffold_4_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':22500000-24999999 -b > XXX_SN:lcl_Scaffold_4_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':25000000-27499999 -b > XXX_SN:lcl_Scaffold_4_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':27500000-29999999 -b > XXX_SN:lcl_Scaffold_4_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':30000000-32499999 -b > XXX_SN:lcl_Scaffold_4_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':32500000-34999999 -b > XXX_SN:lcl_Scaffold_4_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':35000000-37499999 -b > XXX_SN:lcl_Scaffold_4_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':37500000-39999999 -b > XXX_SN:lcl_Scaffold_4_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':40000000-42499999 -b > XXX_SN:lcl_Scaffold_4_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':42500000-44999999 -b > XXX_SN:lcl_Scaffold_4_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':45000000-47499999 -b > XXX_SN:lcl_Scaffold_4_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':47500000-49999999 -b > XXX_SN:lcl_Scaffold_4_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':50000000-52499999 -b > XXX_SN:lcl_Scaffold_4_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':52500000-54999999 -b > XXX_SN:lcl_Scaffold_4_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':55000000-57499999 -b > XXX_SN:lcl_Scaffold_4_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':57500000-59999999 -b > XXX_SN:lcl_Scaffold_4_57500000split.bam
samtools view -h XXX 'lcl|Scaffold_4':60000000-62499999 -b > XXX_SN:lcl_Scaffold_4_60000000split.bam
samtools view -h XXX 'lcl|Scaffold_4':62500000-64999999 -b > XXX_SN:lcl_Scaffold_4_62500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':0-2499999 -b > XXX_SN:lcl_Scaffold_5_0split.bam
samtools view -h XXX 'lcl|Scaffold_5':2500000-4999999 -b > XXX_SN:lcl_Scaffold_5_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':5000000-7499999 -b > XXX_SN:lcl_Scaffold_5_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':7500000-9999999 -b > XXX_SN:lcl_Scaffold_5_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':10000000-12499999 -b > XXX_SN:lcl_Scaffold_5_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':12500000-14999999 -b > XXX_SN:lcl_Scaffold_5_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':15000000-17499999 -b > XXX_SN:lcl_Scaffold_5_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':17500000-19999999 -b > XXX_SN:lcl_Scaffold_5_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':20000000-22499999 -b > XXX_SN:lcl_Scaffold_5_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':22500000-24999999 -b > XXX_SN:lcl_Scaffold_5_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':25000000-27499999 -b > XXX_SN:lcl_Scaffold_5_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':27500000-29999999 -b > XXX_SN:lcl_Scaffold_5_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':30000000-32499999 -b > XXX_SN:lcl_Scaffold_5_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':32500000-34999999 -b > XXX_SN:lcl_Scaffold_5_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':35000000-37499999 -b > XXX_SN:lcl_Scaffold_5_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':37500000-39999999 -b > XXX_SN:lcl_Scaffold_5_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':40000000-42499999 -b > XXX_SN:lcl_Scaffold_5_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':42500000-44999999 -b > XXX_SN:lcl_Scaffold_5_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':45000000-47499999 -b > XXX_SN:lcl_Scaffold_5_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':47500000-49999999 -b > XXX_SN:lcl_Scaffold_5_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':50000000-52499999 -b > XXX_SN:lcl_Scaffold_5_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':52500000-54999999 -b > XXX_SN:lcl_Scaffold_5_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':55000000-57499999 -b > XXX_SN:lcl_Scaffold_5_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_5':57500000-59999999 -b > XXX_SN:lcl_Scaffold_5_57500000split.bam
samtools view -h XXX 'lcl|Scaffold_5':60000000-62499999 -b > XXX_SN:lcl_Scaffold_5_60000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':0-2499999 -b > XXX_SN:lcl_Scaffold_6_0split.bam
samtools view -h XXX 'lcl|Scaffold_6':2500000-4999999 -b > XXX_SN:lcl_Scaffold_6_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':5000000-7499999 -b > XXX_SN:lcl_Scaffold_6_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':7500000-9999999 -b > XXX_SN:lcl_Scaffold_6_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':10000000-12499999 -b > XXX_SN:lcl_Scaffold_6_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':12500000-14999999 -b > XXX_SN:lcl_Scaffold_6_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':15000000-17499999 -b > XXX_SN:lcl_Scaffold_6_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':17500000-19999999 -b > XXX_SN:lcl_Scaffold_6_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':20000000-22499999 -b > XXX_SN:lcl_Scaffold_6_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':22500000-24999999 -b > XXX_SN:lcl_Scaffold_6_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':25000000-27499999 -b > XXX_SN:lcl_Scaffold_6_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':27500000-29999999 -b > XXX_SN:lcl_Scaffold_6_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':30000000-32499999 -b > XXX_SN:lcl_Scaffold_6_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':32500000-34999999 -b > XXX_SN:lcl_Scaffold_6_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':35000000-37499999 -b > XXX_SN:lcl_Scaffold_6_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':37500000-39999999 -b > XXX_SN:lcl_Scaffold_6_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':40000000-42499999 -b > XXX_SN:lcl_Scaffold_6_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':42500000-44999999 -b > XXX_SN:lcl_Scaffold_6_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':45000000-47499999 -b > XXX_SN:lcl_Scaffold_6_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':47500000-49999999 -b > XXX_SN:lcl_Scaffold_6_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':50000000-52499999 -b > XXX_SN:lcl_Scaffold_6_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':52500000-54999999 -b > XXX_SN:lcl_Scaffold_6_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':55000000-57499999 -b > XXX_SN:lcl_Scaffold_6_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_6':57500000-59999999 -b > XXX_SN:lcl_Scaffold_6_57500000split.bam
samtools view -h XXX 'lcl|Scaffold_6':60000000-62499999 -b > XXX_SN:lcl_Scaffold_6_60000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':0-2499999 -b > XXX_SN:lcl_Scaffold_7_0split.bam
samtools view -h XXX 'lcl|Scaffold_7':2500000-4999999 -b > XXX_SN:lcl_Scaffold_7_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':5000000-7499999 -b > XXX_SN:lcl_Scaffold_7_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':7500000-9999999 -b > XXX_SN:lcl_Scaffold_7_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':10000000-12499999 -b > XXX_SN:lcl_Scaffold_7_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':12500000-14999999 -b > XXX_SN:lcl_Scaffold_7_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':15000000-17499999 -b > XXX_SN:lcl_Scaffold_7_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':17500000-19999999 -b > XXX_SN:lcl_Scaffold_7_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':20000000-22499999 -b > XXX_SN:lcl_Scaffold_7_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':22500000-24999999 -b > XXX_SN:lcl_Scaffold_7_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':25000000-27499999 -b > XXX_SN:lcl_Scaffold_7_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':27500000-29999999 -b > XXX_SN:lcl_Scaffold_7_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':30000000-32499999 -b > XXX_SN:lcl_Scaffold_7_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':32500000-34999999 -b > XXX_SN:lcl_Scaffold_7_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':35000000-37499999 -b > XXX_SN:lcl_Scaffold_7_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':37500000-39999999 -b > XXX_SN:lcl_Scaffold_7_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':40000000-42499999 -b > XXX_SN:lcl_Scaffold_7_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':42500000-44999999 -b > XXX_SN:lcl_Scaffold_7_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':45000000-47499999 -b > XXX_SN:lcl_Scaffold_7_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':47500000-49999999 -b > XXX_SN:lcl_Scaffold_7_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':50000000-52499999 -b > XXX_SN:lcl_Scaffold_7_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_7':52500000-54999999 -b > XXX_SN:lcl_Scaffold_7_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_7':55000000-57499999 -b > XXX_SN:lcl_Scaffold_7_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':0-2499999 -b > XXX_SN:lcl_Scaffold_8_0split.bam
samtools view -h XXX 'lcl|Scaffold_8':2500000-4999999 -b > XXX_SN:lcl_Scaffold_8_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':5000000-7499999 -b > XXX_SN:lcl_Scaffold_8_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':7500000-9999999 -b > XXX_SN:lcl_Scaffold_8_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':10000000-12499999 -b > XXX_SN:lcl_Scaffold_8_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':12500000-14999999 -b > XXX_SN:lcl_Scaffold_8_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':15000000-17499999 -b > XXX_SN:lcl_Scaffold_8_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':17500000-19999999 -b > XXX_SN:lcl_Scaffold_8_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':20000000-22499999 -b > XXX_SN:lcl_Scaffold_8_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':22500000-24999999 -b > XXX_SN:lcl_Scaffold_8_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':25000000-27499999 -b > XXX_SN:lcl_Scaffold_8_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':27500000-29999999 -b > XXX_SN:lcl_Scaffold_8_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':30000000-32499999 -b > XXX_SN:lcl_Scaffold_8_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':32500000-34999999 -b > XXX_SN:lcl_Scaffold_8_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':35000000-37499999 -b > XXX_SN:lcl_Scaffold_8_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':37500000-39999999 -b > XXX_SN:lcl_Scaffold_8_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':40000000-42499999 -b > XXX_SN:lcl_Scaffold_8_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':42500000-44999999 -b > XXX_SN:lcl_Scaffold_8_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':45000000-47499999 -b > XXX_SN:lcl_Scaffold_8_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':47500000-49999999 -b > XXX_SN:lcl_Scaffold_8_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':50000000-52499999 -b > XXX_SN:lcl_Scaffold_8_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_8':52500000-54999999 -b > XXX_SN:lcl_Scaffold_8_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_8':55000000-57499999 -b > XXX_SN:lcl_Scaffold_8_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':0-2499999 -b > XXX_SN:lcl_Scaffold_9_0split.bam
samtools view -h XXX 'lcl|Scaffold_9':2500000-4999999 -b > XXX_SN:lcl_Scaffold_9_2500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':5000000-7499999 -b > XXX_SN:lcl_Scaffold_9_5000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':7500000-9999999 -b > XXX_SN:lcl_Scaffold_9_7500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':10000000-12499999 -b > XXX_SN:lcl_Scaffold_9_10000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':12500000-14999999 -b > XXX_SN:lcl_Scaffold_9_12500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':15000000-17499999 -b > XXX_SN:lcl_Scaffold_9_15000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':17500000-19999999 -b > XXX_SN:lcl_Scaffold_9_17500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':20000000-22499999 -b > XXX_SN:lcl_Scaffold_9_20000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':22500000-24999999 -b > XXX_SN:lcl_Scaffold_9_22500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':25000000-27499999 -b > XXX_SN:lcl_Scaffold_9_25000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':27500000-29999999 -b > XXX_SN:lcl_Scaffold_9_27500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':30000000-32499999 -b > XXX_SN:lcl_Scaffold_9_30000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':32500000-34999999 -b > XXX_SN:lcl_Scaffold_9_32500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':35000000-37499999 -b > XXX_SN:lcl_Scaffold_9_35000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':37500000-39999999 -b > XXX_SN:lcl_Scaffold_9_37500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':40000000-42499999 -b > XXX_SN:lcl_Scaffold_9_40000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':42500000-44999999 -b > XXX_SN:lcl_Scaffold_9_42500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':45000000-47499999 -b > XXX_SN:lcl_Scaffold_9_45000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':47500000-49999999 -b > XXX_SN:lcl_Scaffold_9_47500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':50000000-52499999 -b > XXX_SN:lcl_Scaffold_9_50000000split.bam
samtools view -h XXX 'lcl|Scaffold_9':52500000-54999999 -b > XXX_SN:lcl_Scaffold_9_52500000split.bam
samtools view -h XXX 'lcl|Scaffold_9':55000000-57499999 -b > XXX_SN:lcl_Scaffold_9_55000000split.bam
samtools view -h XXX 'lcl|Scaffold_10' -b > XXXSN:lcl_Scaffold_10_split.bam
samtools view -h XXX 'lcl|Scaffold_11' -b > XXXSN:lcl_Scaffold_11_split.bam
samtools view -h XXX 'lcl|Scaffold_12' -b > XXXSN:lcl_Scaffold_12_split.bam
samtools view -h XXX 'lcl|Scaffold_13' -b > XXXSN:lcl_Scaffold_13_split.bam
samtools view -h XXX 'lcl|Scaffold_14' -b > XXXSN:lcl_Scaffold_14_split.bam
samtools view -h XXX 'lcl|Scaffold_15' -b > XXXSN:lcl_Scaffold_15_split.bam
samtools view -h XXX 'lcl|Scaffold_16' -b > XXXSN:lcl_Scaffold_16_split.bam
samtools view -h XXX 'lcl|Scaffold_17' -b > XXXSN:lcl_Scaffold_17_split.bam
samtools view -h XXX 'lcl|Scaffold_18' -b > XXXSN:lcl_Scaffold_18_split.bam


RUN FREEBAYES

freebayes --use-best-n-alleles 4 --pooled-discrete -m 20 -p 25 -C 2 -f YYY *XXX.bam > XXX.fb.out

cat *fb.out > ALL.fb.out

FreeBayesvcf_Ploidy_filter_harsh.py ALL.fb.out > ALL.filtered.fb.out


cat split_vcf/Scaffold_1_0split.fb.out | grep '#' >> allv3_filtered.vcf
cat split_vcf/*fb.out | grep -v '#' >> allv3_filtered.vcf
cat allv3_filtered.vcf | awk '$1 ~ /^#/ {print $0;next} {print $0 | "sort -k1,1 -k2,2n"}' > out_sorted.vcf
bcftools convert -o out_sorted.vcf.gz -O z out_sorted.vcf
tabix -p vcf out_sorted.vcf.gz
cat out_sorted.vcf | grep -v /5 | grep -v /4 | grep -v /3 | grep -v /2 > out_sorted_bi.vcf
cat out_sorted.vcf | grep -e /5 -e /4 -e /3 -e /2 > out_sorted_multi.vcf
python ~/PANGENOME/Paul_Scripts/FB_Allele_freq.py out_sorted_bi.vcf > out_sorted_AF.vcf

