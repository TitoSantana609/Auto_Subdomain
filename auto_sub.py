import subprocess
import os

def get_subdomains_amass(domain):
    command = f"amass enum -d {domain} -o amass_output.txt"
    subprocess.run(command, shell=True)

def get_subdomains_subfinder(domain):
    command = f"subfinder -d {domain} -o subfinder_output.txt"
    subprocess.run(command, shell=True)

def get_subdomains_crtsh(domain):
    command = f"curl -s https://crt.sh/?q={domain} | grep 'TD;' | awk -F 'TD' '{{print $3}}' > crtsh_output.txt"
    subprocess.run(command, shell=True)

def combine_subdomains():
    files = ["amass_output.txt", "subfinder_output.txt", "crtsh_output.txt"]
    subdomains = set()
    for file in files:
        if os.path.exists(file):
            with open(file, "r") as f:
                subdomains.update(f.read().splitlines())
    return subdomains

def save_subdomains(subdomains, filename):
    with open(filename, "w") as f:
        for subdomain in subdomains:
            f.write(subdomain + "\n")

def main():
    domain = input("Enter a domain: ")
    get_subdomains_amass(domain)
    get_subdomains_subfinder(domain)
    get_subdomains_crtsh(domain)
    subdomains = combine_subdomains()
    filename = input("Enter a filename to save the output: ")
    save_subdomains(subdomains, filename)
    print(f"Subdomains saved to {filename}")

if __name__ == "__main__":
    main()
