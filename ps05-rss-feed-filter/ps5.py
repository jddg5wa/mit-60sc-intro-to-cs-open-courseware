# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.g = guid
        self.t = title
        self.sub = subject
        self.sum = summary
        self.l = link
    def get_guid(self):
        return self.g
    def get_title(self):
        return self.t
    def get_subject(self):
        return self.sub
    def get_summary(self):
        return self.sum
    def get_link(self):
        return self.l

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger

class WordTrigger(Trigger):
    def __init__(self, word):
        Trigger.__init__(self)
        self.word = word

    def is_word_in(self, text):
        replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
        textWords = text.translate(replace_punctuation)
        textWords = textWords.split()
        for x in textWords:
            if x.lower() == self.word.lower():
                return True

        return False

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):

    def evaluate(self, story):
        return self.is_word_in(story.get_title())

# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)

    def evaluate(self, story):
        return self.is_word_in(story.get_subject())

# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)

    def evaluate(self, story):
        return self.is_word_in(story.get_summary())


# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.t = trigger

    def evaluate(self, story):
        return not self.t.evaluate(story)

# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2

    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2

    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.p = phrase

    def evaluate(self, story):
        return self.p in story.get_title() or self.p in story.get_summary() or self.p in story.get_subject()

#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel free to change this line!

    # for each in stories:
    #     print each.get_title()

    filteredStories = []

    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filteredStories.append(story)

    for each in filteredStories:
        print each.get_title()

    return filteredStories

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones

    triggers = []
    triggerMap = {}
    for line in lines:
        splitLine = line.split(" ")
        # print splitLine

        if splitLine[0].lower() != 'add':
            # print splitLine
            triggerType = splitLine[1].lower()
            if triggerType == 'title':
                trigger = TitleTrigger(splitLine[2])
            elif triggerType == 'subject':
                trigger = SubjectTrigger(splitLine[2])
            elif triggerType == 'summary':
                trigger = SummaryTrigger(splitLine[2])
            elif triggerType == 'phrase':
                trigger = PhraseTrigger(' '.join(map(str,splitLine[2:])))
                # print ' '.join(map(str,splitLine[2:]))
            elif triggerType == 'not':
                trigger = NotTrigger(triggerMap[splitLine[2]], triggerMap[splitLine[3]])
            elif triggerType == 'and':
                trigger = AndTrigger(triggerMap[splitLine[2]], triggerMap[splitLine[3]])
                # print "triggers", triggerMap[splitLine[2]], triggerMap[splitLine[3]]
            elif triggerType == 'or':
                trigger = OrTrigger(triggerMap[splitLine[2]], triggerMap[splitLine[3]])
            triggerMap[splitLine[0]] = trigger
            triggers.append(trigger)
        else: 
            for name in splitLine[1:]:
                triggers.append(triggerMap[name])

        # print trigger, splitLine[2:]

    # print triggerMap 
    return triggers


    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")
    print triggerlist

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

# readTriggerConfig("triggers.txt")