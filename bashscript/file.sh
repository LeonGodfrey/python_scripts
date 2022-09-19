
#!/bin/bash

> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for file in $files; do
if test -e /home/student-02-c98a7adb4a74$file; then echo /home/student-02-c98a7adb4a74${file} >> oldFiles.txt;
else echo "File doesn't exist"; fi
done

