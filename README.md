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

drwxr-xr-x 2 root root 4096 Jan 27 21:03 .<br/>
drwxr-xr-x 4 root root 4096 Jan 27 19:46 ..<br/>
-rw-r--r-- 1 root root 3622 Jan 27 20:41 pic_sorter.py<br/>
-rw-r--r-- 1 root root 4197 Jan 27 19:39 sample.jpg<br/>

********************************************************************************
CREATING COPIES OF SAMPLE.JPG FOR MOM,DAD,BROTHER
********************************************************************************
$ python pic_sorter.py -n mom,dad,brother -f sample.jpg
[+] Beginning copying process for file: sample.jpg<br/>

[+] Successfully copied the following files:<br/>
----/root/building_picture_sorter/testing_environment/mom/mom-78c52be015<br/>
----/root/building_picture_sorter/testing_environment/dad/dad-78c52be015<br/>
----/root/building_picture_sorter/testing_environment/brother/brother-78c52be015<br/>

[+] The following files already exist:<br/>

[+] Completed!<br/>

********************************************************************************
LISTING ALL OF FILES/DIRECTORIES CREATED 
********************************************************************************
$ ls -la<br/>
-rw-r--r-- 1 root root 3622 Jan 27 20:41 pic_sorter.py<br/>
-rw-r--r-- 1 root root 4197 Jan 27 19:39 sample.jpg<br/>
-rw-r--r-- 1 root root 4197 Jan 27 21:04 sample.jpg.copied<br/>

brother:<br/>
total 16<br/>
drwxr-xr-x 2 root root 4096 Jan 27 21:04 .<br/>
drwxr-xr-x 5 root root 4096 Jan 27 21:04 ..<br/>
-rw-r--r-- 1 root root 4197 Jan 27 21:04 brother-78c52be015<br/>

dad:<br/>
total 16<br/>
drwxr-xr-x 2 root root 4096 Jan 27 21:04 .<br/>
drwxr-xr-x 5 root root 4096 Jan 27 21:04 ..<br/>
-rw-r--r-- 1 root root 4197 Jan 27 21:04 dad-78c52be015<br/>

mom:<br/>
total 16<br/>
drwxr-xr-x 2 root root 4096 Jan 27 21:04 .<br/>
drwxr-xr-x 5 root root 4096 Jan 27 21:04 ..<br/>
-rw-r--r-- 1 root root 4197 Jan 27 21:04 mom-78c52be015<br/>

********************************************************************************
RUNNING SAME ARGUMENTS AGAIN
********************************************************************************
$ python pic_sorter.py -n mom,dad,brother -f sample.jpg<br/>
[+] File sample.jpg is already copied<br/>
----sample.jpg<br/>
----sample.jpg.copied<br/>

********************************************************************************
ADDING MORE PEOPLE FOR SAME PHOTO (Ignores <file_name.ext.copied> file during initial check)
********************************************************************************
$ python pic_sorter.py -n mom,dad,brother,sister -f sample.jpg -a<br/>
[+] Beginning copying process for file: sample.jpg<br/>

[+] Successfully copied the following files:<br/>
----/root/building_picture_sorter/testing_environment/sister/sister-78c52be015<br/>

[+] The following files already exist:<br/>
----/root/building_picture_sorter/testing_environment/mom/mom-78c52be015<br/>
----/root/building_picture_sorter/testing_environment/dad/dad-78c52be015<br/>
----/root/building_picture_sorter/testing_environment/brother/brother-78c52be015<br/>

[+] Completed!<br/>
