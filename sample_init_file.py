# coding: utf8
from __future__ import unicode_literals

from pathlib import Path
from spacy.util import load_model_from_init_py, get_model_meta
from spacy.util import load_model_from_init_py, get_model_meta
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import Matcher
from spacy.tokens import Doc

__version__ = get_model_meta(Path(__file__).parent)['version']


def load(**overrides):
     Language.factories['en_narrow'] = lambda nlp, **cfg: EnNarrow(nlp, **cfg)
     Language.factories['person_narrow'] = lambda nlp, **cfg: PersonNarrow(nlp, **cfg)
     return load_model_from_init_py(__file__, **overrides)

class EnNarrow(object):
    name = 'en_narrow'
    def __init__(self, nlp, **cfg):
        self.matcher = Matcher(nlp.vocab)
        self.doc = Doc(nlp.vocab)
    def __call__(self, doc):
        labels = ["DATE", "GPE", "NORP"]
        previous_labels = ["CAMP", "GHETTO", "DATE", "LOCATION", "NORP", "EVENT"]
        l = []
        for old_ent in doc.ents:
            if old_ent.label_ == "DATE":
                l.append(old_ent)
            elif old_ent.label_ == "GPE":
                new_ent = Span(doc, old_ent.start, old_ent.end, label="LOCATION")
                l.append(new_ent)
            elif old_ent.label_ == "NORP":
                l.append(old_ent)
            elif old_ent.label_ in previous_labels:
                l.append(old_ent)
        l = tuple(l)
        doc.ents = l
        return (doc)


class PersonNarrow(object):
    name = 'person_narrow'
    def __init__(self, nlp, **cfg):
        self.nlp = nlp
        self.doc = Doc(nlp.vocab)
    def __call__(self, doc):
        labels = ["PERSON"]
        previous_labels = ["CAMP", "GHETTO", "DATE", "LOCATION", "NORP", "EVENT"]
        l = []
        for old_ent in doc.ents:
            if old_ent.label_ == "PERSON":
                l.append(old_ent)
            elif old_ent.label_ in previous_labels:
                l.append(old_ent)
        l = tuple(l)
        doc.ents = l
        return (doc)
