###############################################
# CS 21B Intermediate Python Programming Lab #7
# Topics: FTP Programming
# Description: This program connects to a server
#              from pureftpd.org and then goes
#              and prints the contents of the
#              misc directory within the server,
#              then downloading the
#              "netopia-config-2.txt" from said
#              directory.
# Input: none
# Output: directory contents and file download
# Version: 3.7.0
# Development Environment:  IDLE
# Developer:  Aadithya Anumala
# Student ID: 20365071
# Date:  06/11/19
###############################################

from ftplib import FTP

filename = "netopia-config-2.txt"
with FTP("ftp.pureftpd.org") as ftp:
    try: #connect
        ftp.login()
        print("Login successful.")
    except:
        print("Error logging in.")
    #print welcome
    print("Welcome:", ftp.getwelcome())
    print("Current working directory: ")
    ftp.cwd("misc")
    #print dir contents
    ftp.dir()

    #open and download file
    with open(filename, 'wb') as f:
        ftp.retrbinary('RETR ' + filename, f.write)

"""
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab8.py 
Login successful.
Welcome: 220---------- Welcome to Pure-FTPd 1.0.48 [privsep] [TLS] ----------
220-You are user number 1 of 50 allowed.
220-Local time is now 02:51. Server port: 21.
220-IPv6 connections are also welcome on this server.
220 You will be disconnected after 15 minutes of inactivity.
Current working directory: 
drwxr-xr-x   12 1000       1008             2560 Jan  4  2018 .
drwxr-xr-x   18 1000       1008             1024 Jul 21  2016 ..
-rw-r--r--    1 1000       1008            70656 Dec  1  2011 7350roaringbeastv3.tar
-rw-r--r--    1 1000       1008           182007 Apr 12  2012 CVE-2012-1182-samba-3.0.x.tar.gz
-rw-r--r--    1 1000       1008         15826540 Oct 11  2003 DiCosmo_Couchet_ScienceFriction_2003_10_11.ogg
drwxr-xr-x   12 1000       1008              512 Aug 25  2009 Evadeo
lrwxr-xr-x    1 1000       20                 22 Sep 11  2008 GEMA -> ../pure-ftpd/misc/GEMA
-rw-r--r--    1 1000       1008          3412026 Mar 31  2006 IE55-SP2.zip
drwxr-xr-x    2 1000       1008              512 Nov 18  2007 OSX-Logitech-Keyboard
drwxr-xr-x    5 1000       1008              512 Mar 22  2012 OpenBSD
-rw-r--r--    1 1000       1008           336244 Apr 14  2003 SPEC-WML-19991104.pdf
-rw-r--r--    1 1000       0               60704 Aug  4  2015 SetPhotoshopHealingBrush.zip
-rw-r--r--    1 1000       1008            15189 Jan 28  2014 UAC.cpp
-rw-r--r--    1 1000       1008            34337 Jan 24  2008 WirelessDetector.php
-rw-r--r--    1 1000       1008              456 Jul  2  2009 alarmer.c
-rw-r--r--    1 1000       1008              799 Oct 14  2006 anti-xsrf.php
-rw-r--r--    1 1000       1008            25073 Jun 22  2002 apache-nosejob.c
-rw-r--r--    1 1000       1008             2557 Apr 10  2008 bloupo.tar.gz
-rw-r--r--    1 1000       1008              949 Oct 20  2002 bsd-crash.c
drwxr-xr-x    3 1000       1008              512 Feb 23  2009 bugs
-rw-r--r--    1 1000       1008             4125 Jan 10  2015 class.cache_cookie.inc.php
drwxr-xr-x    2 1000       1008              512 Aug 30  2008 cross-subdomains-ajax
-rw-r--r--    1 1000       1008            18098 Apr 28  2009 cyberlaurent.c
-rw-r--r--    1 1000       1008             1607 Nov 19  2011 dnscache-dont-read-tcp-one-byte-at-a-time.diff
-rw-r--r--    1 1000       1008             8639 Nov 16  2011 dnscache-dos.c
-rw-r--r--    1 1000       0                 445 May 16  2013 dnscache-force-tcp-for-any-queries.diff
-rw-r--r--    1 1000       0                6136 Feb  7  2014 dnscache-siphash.patch
-rw-r--r--    1 1000       1008             1649 Jul 25  2006 dspam_cssclean_fix.patch
-rw-r--r--    1 1000       1008             3605 Dec 11  2010 eximxpl.pl
-rw-r--r--    1 1000       1008              611 Nov  1  2008 export-excel.php
-rw-r--r--    1 1000       1008             4684 Dec  6  2009 fbsd-rtld-full-package
-rw-r--r--    1 1000       1008             1090 Jan 22  2010 fix_broken_uri_path_components.php
-rw-r--r--    1 1000       1008           412804 May  2  2006 ftpfuzz.zip
-rw-r--r--    1 1000       1008             1713 Dec  1  2009 gettext-x-php-concat.diff
-rw-r--r--    1 1000       1008          1441792 Jan  2  2012 hashcollide.txt
-rw-r--r--    1 1000       1008             2148 Nov  9  2006 ie-img-tag-vb-workaround.diff
-rw-r--r--    1 1000       1008            67901 Nov  5  2003 jokes-html.zip
-rw-r--r--    1 1000       1008             3116 Aug 27  2008 jsafecat.c
-rw-r--r--    1 1000       1008              700 Apr  3  2010 kaleak.c
-rw-r--r--    1 1000       1008             1616 Jun  6  2003 linux_24_signal_logging.patch
-rw-r--r--    1 1000       1008             6003 Jun 15  2014 linux_udp_tcp_blackhole.diff
-rwxr-xr-x    1 1000       1008             1329 May 22  2004 mass-document_root.php
-rw-r--r--    1 1000       1008          1756203 Dec 25  2011 n1548.pdf
-rw-r--r--    1 1000       1008              755 Apr 23  2003 netopia-config-2.txt
-rw-r--r--    1 1000       1008            40985 Nov  8  2011 nkiller2.c
drwxr-xr-x    2 1000       1008              512 Sep 13  2011 nptl-bugs
-rw-r--r--    1 1000       1008              995 Sep 16  2003 openssh-fix.patch
-rw-r--r--    1 1000       1008             2403 Sep 17  2003 openssh-fix2.patch
-rw-r--r--    1 1000       1008              518 Nov  9  2006 php-5.2.0-norealpath.patch
-rwxr-xr-x    1 1000       1008             2591 Nov 24  2009 php-exploit.sh
-rw-r--r--    1 1000       1008             1383 Nov  4  2006 php_clearstatcache_should_clear_realpath_cache.diff
-rw-r--r--    1 1000       1008              506 Nov  4  2006 php_dont_realpath_cache_symlinks.diff
-rw-r--r--    1 1000       1008             2420 Apr 21  2006 php_is_valid_email.php
-rw-r--r--    1 1000       1008               65 Jun 15  2006 php_ob_flush_dos.php
-rw-r--r--    1 1000       1008             3913 Nov  4  2006 php_sync_realpath_cache_with_unlink_and_rename.diff
drwxr-xr-x    2 1000       1008              512 Nov  4  2007 posto
drwx--x--x    2 1000       1008              512 Dec 14  2012 private
-rw-r--r--    1 1000       1008             7123 Jan  9  2011 proftpd.gnu.c
-rw-r--r--    1 1000       1008            15854 Jun 14  2003 pureftpd-fake.c
lrwxr-xr-x    1 1000       20                 15 Feb  1  2006 pureftps-fake.c -> pureftpd-fake.c
drwxr-xr-x    2 1000       1008              512 Oct 27  2010 reisersmtp
drwxr-xr-x    2 1000       1008              512 Mar  5  2010 ruby
-rw-r--r--    1 1000       1008           104637 Mar  4  2008 server.n
-rw-r--r--    1 1000       1008          8374337 May 22  2004 sheekiii14.ogg
-rw-r--r--    1 1000       1008             6273 Apr  4  2016 slowloris.pl.zip
-rw-r--r--    1 1000       0                4362 Jan  4  2018 spectre.c
-rwxr-xr-x    1 1000       1008             1072 Aug 30  2005 stripslashes.php
-rw-r--r--    1 1000       0             1247825 May  3  2016 tinysshd-obsd.tar.gz
lrwxr-xr-x    1 1000       1008               28 Feb  4  2012 udp_tcp_blackhole.diff -> linux_udp_tcp_blackhole.diff
-rw-r--r--    1 1000       1008             5439 Jun 11  2004 zsh-config.tar.gz
-rw-r--r--    1 1000       1008             6249 Jul  7  2003 zsh-modified.tar.gz
"""
