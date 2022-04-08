#!/usr/bin/python3
import os
import re
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)


def main():
    optimize('domains', '')
    pass


def optimize(input_path, output_root):
    domains = set()
    if os.path.isfile(input_path):
        if input_path.endswith(".txt"):
            domains.update(read_file(input_path, r'^\*://(?:\*\.)?([\w\-\.]+)/\*'))
            output_root = os.path.join(output_root, os.path.splitext(os.path.basename(input_path))[0])
        else:
            return []
    else:
        files = os.listdir(input_path)
        for file in files:
            path = os.path.join(input_path, file)
            file_output_root = os.path.join(output_root, file) if os.path.isdir(path) else output_root
            domains.update(optimize(path, file_output_root))

    log.info('Read %s unique lines for %s' % (len(domains), input_path))

    domain_set = set()
    domain_list = []
    for domain in domains:
        if domain.startswith('www.'):
            domain = domain.replace('www.', '')
        domain_set.add(domain)
        pass

    domain_list.extend(domain_set)
    domain_list.sort()
    write_all(domain_list, output_root)

    return domain_list


def write_all(domains, output_root):
    write_ublacklist(domains, output_root)
    write_surge(domains, output_root)
    pass


def read_file(file_path, pattern):
    domains = []
    if os.path.exists(file_path):
        with open(file_path) as f:
            for line in f.readlines():
                m = re.match(pattern, line)
                if m and len(m.groups()) > 0:
                    domains.append(m.group(1))
                pass
            pass
        log.info('Read %s lines from %s' % (len(domains), file_path))
    else:
        log.warning('No such file or directory: %s' % file_path)
    return domains


def write_file(file_path, domains, wrapper):
    lines = []
    parent_path = os.path.dirname(file_path)
    if parent_path != '' and not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(parent_path)

    with open(file_path, 'w') as f:
        for domain in domains:
            lines.append(wrapper(domain))

        f.writelines(lines)
        f.flush()
    pass


def read_ublacklist():
    return read_file('uBlacklist.txt', r'^\*://(?:\*\.)?([\w\-\.]+)/\*')


def write_ublacklist(domains, output_root):
    write_file(os.path.join('uBlacklist', output_root + '.txt') if output_root != '' else 'uBlacklist.txt', domains, lambda x: '*://*.%s/*\n' % x if is_domain(x) else '*://%s/*\n' % x)
    pass


def read_surge():
    return read_file('Surge.txt', r'^(?:\.)?([\w\-\.]+)')


def write_surge(domains, output_root):
    write_file(os.path.join('Surge', output_root + '.txt') if output_root != '' else 'Surge.txt', domains, lambda x: '.%s\n' % x if is_domain(x) else '#%s\n' % x)
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
