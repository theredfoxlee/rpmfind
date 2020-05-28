#!/usr/bin/env python3 


""" This script provides API to rpmfind.net query metchnism. """


__author__ = 'Kamil Janiec <kamil.p.janiec@gmail.com>'


import argparse
import collections
import sys
import typing
import logging

import bs4
import requests


RPMFIND_URL = 'https://www.rpmfind.net'

RPM = collections.namedtuple('RPM', ['name', 'html', 'rpm', 'dist', 'spec'])


def _get_query_url(query: str, dist: str = None, arch: str = None) -> str:
    """ Prepare rpmfind query url. """
    query_url = f'{RPMFIND_URL}/linux/rpm2html/search.php?query={query}'
    if dist:
        query_url = query_url + f'&system={dist}'
    if arch:
        query_url = query_url + f'&arch={arch}'
    return query_url


def _get_rpms(query_soup: bs4.BeautifulSoup) -> typing.Generator[RPM, None, None]:
    """ Scrap query website and return generator of all rpms. """
    for tr_tag in query_soup.find_all('tr', {'bgcolor' : True}):
        td_tags = tr_tag.find_all('td')
        if len(td_tags) == 4:
            yield RPM(
                name=td_tags[0].text.rstrip('.html'),
                html=f"{RPMFIND_URL}{td_tags[0].find('a')['href']}",
                rpm=f"{RPMFIND_URL}{td_tags[3].find('a')['href']}",
                dist=td_tags[2].text,
                spec=td_tags[1].text)

def _parse_args(args: typing.List[str]) -> argparse.Namespace:
    """ Return parsed args. """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='turn on debug logging')
    parser.add_argument('-n', type=int, help='head -n <N>')
    parser.add_argument('--dist', help='software distribution')
    parser.add_argument('--arch', help='software architecture')
    parser.add_argument('software', help='software name')
    return parser.parse_args(args)


def get_rpms(software: str, dist: str = None, arch: str = None) -> typing.Generator[RPM, None, None]:
    """ Perform query on rpmfind and return generator of rpms. """ 
    query_url = _get_query_url(software, dist, arch)
    logging.debug(f'query_url: {query_url}')
    query_html = requests.get(query_url).text
    query_soup = bs4.BeautifulSoup(query_html, features='html.parser')
    return _get_rpms(query_soup)


def main():
    """ App entrypoint. """
    args = _parse_args(sys.argv[1:])
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    rpms = get_rpms(args.software, args.dist, args.arch)
    if args.n:
        rpms = list(rpms)[:args.n]
    for rpm in rpms:
        print(rpm.name, rpm.rpm, rpm.dist, sep=',')


if __name__ == '__main__':
    main()
