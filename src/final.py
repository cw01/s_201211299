# -*- coding: utf-8 -*-
import requests
from lxml.cssselect import CSSSelector
import lxml.html

re = requests.get('https://www.op.gg/champion/statistics')
h = lxml.html.fromstring(re.text)
def supporter():
    sel = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-SUPPORT > ul > li:nth-child(n) > a > div.Champion > div.ChampionName')
    sel1 = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-SUPPORT > ul > li:nth-child(n) > a > div.Value > b')
    nodes = sel(h)
    nodes1 = sel1(h)
    
    for i,n in enumerate(nodes):
        if(i < 5):
            print i+1,n.text,"-> winning rate",nodes1[i].text
    print ""
def adcarry():
    sel = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-ADC > ul > li:nth-child(n) > a > div.Champion > div.ChampionName')
    sel1 = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-ADC > ul > li:nth-child(n) > a > div.Value > b')
    nodes = sel(h)
    nodes1 = sel1(h)
    
    for i,n in enumerate(nodes):
        if(i < 5):
            print i+1,n.text,"-> winning rate",nodes1[i].text
    print ""

def mid():
    sel = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-MID > ul > li:nth-child(n) > a > div.Champion > div.ChampionName')
    sel1 = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-MID > ul > li:nth-child(n) > a > div.Value > b')
    nodes = sel(h)
    nodes1 = sel1(h)
    
    for i,n in enumerate(nodes):
        if(i < 5):
            print i+1,n.text,"-> winning rate",nodes1[i].text
    print ""
    
def top():
    sel = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-TOP > ul > li:nth-child(n) > a > div.Champion > div.ChampionName')
    sel1 = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-TOP > ul > li:nth-child(n) > a > div.Value > b')
    nodes = sel(h)
    nodes1 = sel1(h)
    
    for i,n in enumerate(nodes):
        if(i < 5):
            print i+1,n.text,"-> winning rate",nodes1[i].text
    print ""
def jungle():
    
    sel = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-JUNGLE > ul > li:nth-child(n) > a > div.Champion > div.ChampionName')
    sel1 = CSSSelector('#ChampionTrendSummary > div > div.tabItems > div.ChampionTrendSummaryContent.tabItem.ChampionTrendSummary-WinRatio > div > div.tabItems > div.tabItem.ChampionTrendSummary-WinRatio-JUNGLE > ul > li:nth-child(n) > a > div.Value > b')
    nodes = sel(h)
    nodes1 = sel1(h)
    
    for i,n in enumerate(nodes):
        if(i < 5):
            print i+1,n.text,"-> winning rate",nodes1[i].text
    print ""
    
    
while(1):
    print "0.end 1.supporter 2.ad carry 3.mid 4.top 5.jungle"
    number = input();
    if(number == 0):
        break;
    if(number == 1):
        supporter()
    if(number == 2):
        adcarry()
    if(number == 3):
        mid()
    if(number == 4):
        top()
    if(number == 5):
        jungle()
