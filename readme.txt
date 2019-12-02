Simple VCF exercise:

function:sort keyvalue in the VCF file
Python version:3.68
No other libiary needed.

How to use:
1.Unzip
2.command line: python vcf --sort --key KEY_NAME --filename FILENAME
--saved_path SAVED_PATH --order AES OR DES
3../data/SortByKEY_NAME.vcf will generate

filename: default as small_demo.vcf
order:default as AES
saved_path default as ./data/

Simple example: python vcf --sort --key BaseQRankSum

Notice: some Key cannot be used since some data mistakes
example: At 441 line, AC values 1,1. So this cannot be convert to float and used to sort.
TimSort algorithm is used. It's a stable sort which I think should be important for research. 

What's more, some more options may be added at the rest of this week, also, a well established readme file and github link will be submited tomorrow.
