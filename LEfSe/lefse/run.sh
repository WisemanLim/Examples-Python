#!/bin/bash
# Checking arguments and initialize
while getopts i:c:s:u:f: flag
do
    case "${flag}" in
        i) input_filename=${OPTARG};;
        c) option_c=${OPTARG};;
        s) option_s=${OPTARG};;
        u) option_u=${OPTARG};;
        f) features_runnung=${OPTARG};;
    esac
done
if [[ ( $input_filename == "" ) ]]; then
  echo "-i or input_filename(only filename) is required. i.e. -i hmp_small_aerobiosis [-c 1 -s 2 -u 3]"
  exit
fi
in_filename="$input_filename.in"
res_filename="$input_filename.res"
png_filename="$input_filename.png"
cladogram_png_filename="$input_filename.cladogram.png"
input_filename="$input_filename.txt"
#echo "input_filename : $input_filename";
#echo "-c: $option_c";
#echo "-s: $option_s";
#echo "-u: $option_u";
#echo "-f: $features_runnung";
if [[ ( $option_c == "" ) ]]; then
  option_c=1
fi
#if [[ ( $option_s == "" ) ]]; then
#  option_s=2
#fi
if [[ ( $option_u == "" ) ]]; then
  option_u=$option_c
fi
if [[ ( $features_runnung == "" ) ]]; then
  features_runnung="n"
fi
# As using LEfSe through bioconda, need to activate the LEfSe installation:
#source activate lefse

# Running the LEfSe commands with -h gives the list of available options

# lefse-format_input.py convert the input data matrix to the format for LEfSe.
#
# In this example we use the class information in the first line (-c 1)
# the subclass in the second line (-s 2) and the subject in the third (-u 3).
# If the subclass or the subject are not present in the data you need to set
# the value -1 for them.
# -o 1000000 scales the feature such that the sum (of the same taxonomic leve)
# is 1M: this is done only for obtaining more meaningful values for the LDA score
if [[ ( $option_c != "" ) && ( $option_s != "" ) && ( $option_u != "" ) ]]; then
  lefse_format_input.py $input_filename $in_filename -c $option_c -s $option_s -u $option_u -o 1000000
elif [[ ( $option_c != "" ) && ( $option_s != "" ) ]]; then
  lefse_format_input.py $input_filename $in_filename -c $option_c -s $option_s -o 1000000
elif [[ ( $option_c != "" ) && ( $option_u != "" ) ]]; then
  lefse_format_input.py $input_filename $in_filename -c $option_c -u $option_u -o 1000000
else
  lefse_format_input.py $input_filename $in_filename -c $option_c -o 1000000
fi

# lefse_run.py performs the actual statistica analysis
#
# Apply LEfSe on the formatted data producing the results (to be further processed
# for visualization with the other modules). The option available
# can be listed using the -h option
lefse_run.py $in_filename $res_filename

# lefse_plot_res.py visualizes the output
#
# Plot the list of biomarkers with their effect size
# Severak graphical options are available for personalizing the output
lefse_plot_res.py $res_filename $png_filename --dpi 300

# lefse_plot_cladogram.py visualizes the output on a hierarchical tree
#
# Plot the representation of the biomarkers on the hierarchical tree
# specified in the input data (using | in the name of the features)
# In this case we will obtain the RDP taxonomy.
# This is an early implementation of the module. I'm working on an improved version
# that will be released independently from LEfSe
lefse_plot_cladogram.py $res_filename $cladogram_png_filename --format png --dpi 300

if [[ ( $features_runnung == "Y" ) || ( $features_runnung == "y" ) ]]; then
# Create a directory for storing the raw-data representation of the discovered biomarkers
  mkdir biomarkers_raw_images

# lefse_plot_features.py visualizes the raw-data features
#
# The module for exporting the raw-data representation of the features.
# With the default options we will obtain the images for all the features that are
# detected as biomarkers
  lefse_plot_features.py $in_filename $res_filename biomarkers_raw_images/
fi

## Turn lefse back off
#source deactivate lefse

## bonus: seasonal greetings
# echo '~ Oíche Shamhna féile dhuit!'

# sh run.sh -i ../data/lefse_aib_220726 -c 1 -u 2 -f n
# sh run.sh -i ../data/ch_220718_1st_2nd -c 1 -f n