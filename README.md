# picture_sorter
Automates the process of organizing photos of family and friends


Purpose:
- This program is designed to organize photos into seperate directories

Features:
- Automatically checks for and creates directories for organization
- Checks if files already copied
- Appends SHA256 hash to each copied file for unique name to avoid overwriting
- Creates <file.ext.copied> file upon completion 

Usage:
- python pic_sorter.py -n <comma seperated family names> -f <file.ext>
Ex: 
- python pic_sorter.py -n mom,dad,grandma -f sample.jpg

********************************************************************************
LIST OF FILES IN CURRENT DIRECTORY 
********************************************************************************
$ ls -la 

drwxr-xr-x 2 root root 4096 Jan 27 21:03 .\n
drwxr-xr-x 4 root root 4096 Jan 27 19:46 ..\n
-rw-r--r-- 1 root root 3622 Jan 27 20:41 pic_sorter.py\n
-rw-r--r-- 1 root root 4197 Jan 27 19:39 sample.jpg\n

********************************************************************************
CREATING COPIES OF SAMPLE.JPG FOR MOM,DAD,BROTHER
********************************************************************************
$ python pic_sorter.py -n mom,dad,brother -f sample.jpg
[+] Beginning copying process for file: sample.jpg

[+] Successfully copied the following files:
----/root/building_picture_sorter/testing_environment/mom/mom-78c52be015
----/root/building_picture_sorter/testing_environment/dad/dad-78c52be015
----/root/building_picture_sorter/testing_environment/brother/brother-78c52be015

[+] The following files already exist:

[+] Completed!

********************************************************************************
LISTING ALL OF FILES/DIRECTORIES CREATED 
********************************************************************************
$ ls -la
-rw-r--r-- 1 root root 3622 Jan 27 20:41 pic_sorter.py
-rw-r--r-- 1 root root 4197 Jan 27 19:39 sample.jpg
-rw-r--r-- 1 root root 4197 Jan 27 21:04 sample.jpg.copied

brother:
total 16
drwxr-xr-x 2 root root 4096 Jan 27 21:04 .
drwxr-xr-x 5 root root 4096 Jan 27 21:04 ..
-rw-r--r-- 1 root root 4197 Jan 27 21:04 brother-78c52be015

dad:
total 16
drwxr-xr-x 2 root root 4096 Jan 27 21:04 .
drwxr-xr-x 5 root root 4096 Jan 27 21:04 ..
-rw-r--r-- 1 root root 4197 Jan 27 21:04 dad-78c52be015

mom:
total 16
drwxr-xr-x 2 root root 4096 Jan 27 21:04 .
drwxr-xr-x 5 root root 4096 Jan 27 21:04 ..
-rw-r--r-- 1 root root 4197 Jan 27 21:04 mom-78c52be015

********************************************************************************
RUNNING SAME ARGUMENTS AGAIN
********************************************************************************
$ python pic_sorter.py -n mom,dad,brother -f sample.jpg
[+] File sample.jpg is already copied
----sample.jpg
----sample.jpg.copied

********************************************************************************
ADDING MORE PEOPLE FOR SAME PHOTO (Ignores <file_name.ext.copied> file during initial check)
********************************************************************************
$ python pic_sorter.py -n mom,dad,brother,sister -f sample.jpg -a
[+] Beginning copying process for file: sample.jpg

[+] Successfully copied the following files:
----/root/building_picture_sorter/testing_environment/sister/sister-78c52be015

[+] The following files already exist:
----/root/building_picture_sorter/testing_environment/mom/mom-78c52be015
----/root/building_picture_sorter/testing_environment/dad/dad-78c52be015
----/root/building_picture_sorter/testing_environment/brother/brother-78c52be015

[+] Completed!
