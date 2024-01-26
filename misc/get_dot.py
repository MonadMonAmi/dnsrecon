from os.path import join

SUBDOMAIN_LIST_5000_WITHOUT_DOTS = join("misc", "subdomains-top2mil-5000_without_dots.txt")

if __name__ == "__main__":
    with open("subdomains-top1mil-5000.txt") as f:
        l = [line.strip() for line in f.readlines()]

    res = list(filter(lambda v: '.' not in v, l))

    with open(SUBDOMAIN_LIST_5000_WITHOUT_DOTS, "w") as fo:
        fo.write("\n".join(res) + "\n")

    res_dot = list(filter(lambda v: '.' in v, l))
    print(len(res_dot))
