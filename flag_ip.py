def failed_login(file_path):
	failed_attempts={}
	with open(file_path,"r") as file:
		for line in file:
			if "Failed login" in line:
				ip=line.strip().split(" - ")[0]
				if ip in failed_attempts:
					failed_attempts[ip]+=1
				else:
					failed_attempts[ip]=1
	print("IPs with suspicious activity:\n")
	for ip,count in failed_attempts.items():
		if count>=3:
			print(f"{ip}->{count} failed attempts\n")
failed_login("system_logs.txt")