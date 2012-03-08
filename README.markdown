TLUG-Gmane-backup
=======

GitHub Backup of TLUG mailing list from Gmane server
-------

This set of scripts creates a backup of tlug mailing list in a git repository as a single maildir file tlug_archive.txt

See furthed discussion here: http://thread.gmane.org/gmane.org.user-groups.linux.tolug/57370


### List of files

 * cron_submit.sh -- pull new emails from gmain, commit everything and push to origin.
 * get_latest.sh -- updates existing tlug_archive.txt with new messages. The number of messages saved so far is stored in a file `latest_msg`.
 * gmain_archive.py -- pull complete tlug archive from gmain while dealing with 30-second server-side php script execution time limit.
 * requirements.txt -- pip dependencies