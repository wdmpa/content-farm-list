#!/usr/bin/python3
import os
import re
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)


def main():
    domains = read_all()
    domain_set = set()
    sorted = []
    for domain in domains:
        if domain.startswith('www.'):
            domain = domain.replace('www.', '')
        domain_set.add(domain)
        pass

    sorted.extend(domain_set)
    sorted.sort()
    write_all(sorted)


def read_all():
    domains = set()
    domains.update(read_ublacklist())
    domains.update(read_surge())
    log.info('read %s  unique lines' % len(domains))
    return domains


def write_all(domains):
    write_ublacklist(domains)
    write_surge(domains)
    pass


def read_file(fname, pattern):
    domains = []
    with open('../' + fname) as f:
        for line in f.readlines():
            m = re.match(pattern, line)
            if m and len(m.groups()) > 0:
                domains.append(m.group(1))
            pass
        pass
    log.info('read %s lines from %s' % (len(domains), fname))
    return domains


def write_file(fname, domains, wrapper):
    lines = []
    with open('../' + fname, 'w') as f:
        for domain in domains:
            lines.append(wrapper(domain))

        f.writelines(lines)
        f.flush()
    pass


def read_ublacklist():
    return read_file('uBlacklist.txt', r'^\*://(?:\*\.)?([\w\-\.]+)/\*')


def write_ublacklist(domains):
    write_file('uBlacklist.txt', domains, lambda x: '*://*.%s/*\n' % x if is_domain(x) else '*://%s/*\n' % x)
    pass


def read_surge():
    return read_file('Surge.txt', r'^(?:\.)?([\w\-\.]+)')


def write_surge(domains):
    write_file('Surge.txt', domains, lambda x: '.%s\n' % x if is_domain(x) else '#%s\n' % x)
    pass


def is_domain(domain):
    return re.match(r'([\w-]\.)*[\w-]{3,}\.\w+', domain)
    pass


def is_ip(domain):
    return re.match(r'((\d{1,3}\.){3}\d{1,3})|(([\da-f]+:)+[\da-f]+)', domain)


if __name__ == "__main__":
    file_handler = logging.FileHandler('%s.log' % os.path.basename(sys.argv[0][:-4]))
    file_handler.setLevel(level=logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)
    main()
