import json
import os
import string
import time

import requests


class Valuespaces:
    idsVocabs = ['conditionsOfAccess', 'discipline', 'educationalContext', 'hochschulfaechersystematik',
                 'intendedEndUserRole', 'learningResourceType', 'new_lrt', 'oer', 'sourceContentType', 'toolCategory']
    idsW3ID = ['containsAdvertisement', 'price', 'accessibilitySummary', 'dataProtectionConformity', 'fskRating']
    data = {}

    def __init__(self):
        vocab_list: list[dict] = []
        # one singular dictionary in the vocab list will typically look like this:
        # {'key': 'discipline', 'url': 'https://vocabs.openeduhub.de/w3id.org/openeduhub/vocabs/discipline/index.json'}
        for v in self.idsVocabs:
            vocab_list.append(
                {'key': v, 'url': 'https://vocabs.openeduhub.de/w3id.org/openeduhub/vocabs/' + v + '/index.json'})
        for v in self.idsW3ID:
            vocab_list.append({'key': v, 'url': 'http://w3id.org/openeduhub/vocabs/' + v + '/index.json'})
        for vocab_name in vocab_list:
            # try:
            voc = getVocabulary(vocab_name['url'])
            self.data[vocab_name['key']] = self.flatten(voc['hasTopConcept'])
            # except:
            #    self.valuespaces[v] = {}

    def flatten(self, tree: []):
        result = tree
        for leaf in tree:
            if 'narrower' in leaf:
                result.extend(self.flatten(leaf['narrower']))
        return result

    @staticmethod
    def findKey(valuespaceId: string, id: string, valuespace=None):
        if not valuespace:
            valuespace = Valuespaces.data[valuespaceId]
        for key in valuespace:
            if key['id'] == id:
                return key
            if 'narrower' in key:
                found = Valuespaces.findKey(valuespaceId, id, key['narrower'])
                if found:
                    return found
        return None

    def findInText(self, valuespaceId: string, text: string, valuespace = None):
        if valuespace is None:
            valuespace = self.data[valuespaceId]
        result = []
        for v in valuespace:
            labels = list(v["prefLabel"].values())
            if "altLabel" in v:
                labels = labels + list(v["altLabel"].values())
            labels = list(map(lambda x: x.casefold(), labels))
            for label in labels:
                # TODO: dirty hack!
                if (" " + label) in text.casefold():
                    result.append(v["id"])
                    break
        for key in valuespace:
            if key['id'] == id:
                return key
            if 'narrower' in key:
                result = result + self.findInText(valuespaceId, text, key['narrower'])
        return result
    def initTree(self, tree):
        for t in tree:
            names = self.getNames(t)
            # t['words'] = list(map(lambda x: nlp(x)[0], names))
            t['words'] = names
            if 'narrower' in t:
                self.initTree(t['narrower'])

    def getNames(self, key):
        names = []
        if 'prefLabel' in key:
            if 'de' in key['prefLabel']:
                names += [key['prefLabel']['de']]
            if 'en' in key['prefLabel']:
                names += [key['prefLabel']['en']]
        if 'altLabel' in key:
            names += key['altLabel']['de'] if 'de' in key['altLabel'] else []
            names += key['altLabel']['en'] if 'en' in key['altLabel'] else []
        if 'note' in key:
            names += key['note']['de'] if 'de' in key['note'] else []
            names += key['note']['en'] if 'en' in key['note'] else []

        names = list(set(map(lambda x: x.strip(), names)))
        return names


def getVocabulary(url: string):
    # get the vocabulary and cache it under cache/valuespaces/{key}.json
    key = url.split('/')[-2]
    cache_root = 'cache/valuespaces'
    cache_file = cache_root + '/' + key + '.json'
    if os.path.exists(cache_file):
        # timespan of one day
        timespan = 60 * 60 * 24
        # if the file is not older, return the cached version
        if time.time() < os.path.getmtime(cache_file) + timespan:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)

    # fetch the vocabulary and store in cache
    r = requests.get(url, timeout=5)
    result = r.json()
    os.makedirs(cache_root, exist_ok=True)
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(result, f)
        return result
