from os.path import join
from json import load

from misc.custom_dnsrecon import OUTPUT_DIR


def main():
    with open(join(OUTPUT_DIR, "exampble_bbc.com.json")) as infile:
        js = load(infile)
        info = js[0]
        j = js[1:]
        a_list = [v["name"] for v in j if v["type"] == "A"]
        aaaa_list = [v["name"] for v in j if v["type"] == "AAAA"]
        cname_list = [v["name"] for v in j if v["type"] == "CNAME"]
        rest_list_names = [' '.join(v.keys()) for v in j if (v["type"] != "A" and v["type"] != "AAAA")]
        print(len(j), len(a_list), len(aaaa_list), len(rest_list_names), len(cname_list))
        print(len(set(a_list)), len(set(aaaa_list)), len(set(cname_list)), len(set(rest_list_names)))
        """
        114 51 24 39 39
        23 7 32 1
        """
        print('\n'.join(a_list))
        print('\n\n')
        print('\n'.join(aaaa_list))
        print('\n\n')
        print('\n'.join(rest_list_names))


def wildcards():
    with open(join(OUTPUT_DIR, "employmenthero.com_5000.json")) as infile:
        js = load(infile)
        info = js[0]
        j = js[1:]
        a_list = [v["name"] for v in j if v["type"] == "A"]
        print(len(a_list), len(set([v["address"] for v in j if v["type"] == "A"])))
        aaaa_list = [v["name"] for v in j if v["type"] == "AAAA"]
        print(len(aaaa_list), len(set([v["address"] for v in j if v["type"] == "AAAA"])))
        """
        4963 39
        16 16
        """
        # 4963 39 - only 39 different IPs. (!) What does in mean?
        # 16 16 - shows that are using different IPs for each subdomain.
        # A: That all means wildcard resolution is enabled only for IPv4.


if __name__ == '__main__':
    # main()
    wildcards()
