#!/bin/bash

filecnt=1

STEP_COUNT=`cat steps.txt | grep "^---" | wc -l`

echo "number of steps: ${STEP_COUNT}"
mkdir --parents frames
for line in `cat steps.txt` ; do
    `echo $line | grep -q '^---'`
    if [ $? -ne "0" ] ; then
        echo "$line" >> /tmp/step_"$filecnt"
    else
        # generate plot
        echo "set terminal png" > tmp.plt
        echo "unset border" >> tmp.plt
        echo "unset xtics; unset ytics" >> tmp.plt
        echo "set output \"plot_frame${filecnt}.png\"" >> tmp.plt
        echo "plot \"/tmp/step_${filecnt}\" every ::1 with boxes"  >> tmp.plt
        gnuplot tmp.plt
        filecnt=`expr $filecnt + 1`
    fi
done
rm -rf /tmp/step_*

FRAMERATE=5
OUT=plot.gif
rm -rf $OUT
ffmpeg -r $FRAMERATE -i plot_frame%d.png $OUT
