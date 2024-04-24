# cleanGB

Clean names of sequences downloaded from GenBank and converts them to fasta files

Headings of sample names retain: Ascention_OrganismName_Code#

## Input
Input format is a genbank file (.gb) downloaded from GenBank, can contain a single or multiple sequences.

NOTE: 
This program clean sequence names based on factor number (i.e number of elements in the name) if your file have a non traditional name, double check the output names before proceeding.

## Usage
`python cleanGB.py [INPUT_FASTA] [OUTPUT_FILE_NAME]`

## Requirements
- Biopython 1.79

## License
The code within this repository is available under a 3-clause BSD license. See the License.txt file for more information.

## Citation
If you use this script for your own research, please provide the link to this software repository in your manuscript:
https://github.com/rmonjaraz/cleanGB
