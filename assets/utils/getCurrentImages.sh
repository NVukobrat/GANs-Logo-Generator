#!/bin/bash
#
#
#

# Variables
SRC_PATH=/media/nvukobrat/Data/PycharmProjects/gans-logo-generation-test/res/
DEST_PATH=~/Desktop/Tmp

# Copy rest of image examples
for i in {100..750000..100}
do
	if [ $i -gt 2000 ]
	then
		if [ $(($i%1000)) -eq 0 ]
		then
			name=$(printf "%05d" $i)
			cp ${SRC_PATH}image_at_epoch_${name}_00000.png ${DEST_PATH}
		fi
	else
		name=$(printf "%05d" $i)
                cp ${SRC_PATH}image_at_epoch_${name}_00000.png ${DEST_PATH}
	fi
done
