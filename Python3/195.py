    
__________________________________________________________________________________________________
awk '{if(NR == 10) print $0}' file.txt
__________________________________________________________________________________________________
awk 'NR == 10' file.txt
__________________________________________________________________________________________________
sed -n 10p file.txt