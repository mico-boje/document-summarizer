import os
import ast
import nltk
import json

filename = r'/home/miboj/Data-Science/NLP/document-summarizer/data/internal/raw/articles.json'
file = open(filename, encoding='ascii', errors='ignore')
text = file.read()
file.close()

d = ast.literal_eval(text)
oo = [" WASHINGTON — The U.S. Army is seeing improvements in anti-jam capabilities in new radios crucial to securing manned-unmanned communications at its annual Network Modernization Experiment.", " At NetModX ’20, which runs from ", "late July to early October", " at Joint Base McGuire-Dix-Lakehurst in New Jersey, the Army’s Combat Capabilities Development Command’s C5ISR Center — or Command, Control, Communication, Computers, Cyber, Intelligence, Surveillance, and Reconnaissance Center — is testing the resiliency of the new radios. The effort will help the service observe how they would perform in the field as the Army looks to partner humans and machines.", " Initial data from the event suggests the two companies involved — ", "Silvus ", "and Persistent Systems — have improved their radio capabilities from last year, specifically in regard to anti-jam, according to Daniel Duvak, chief of the C5ISR Center’s Radio Frequency Communications division.", " But one major challenge is making the radios less detectable as the Army’s tactical network team starts to focus on command post survivability — or reducing the electromagnetic signature of command post communications — while not sacrificing latency and throughput.", " “If you want to make it less detectable, you know oftentimes you have to trade off the throughput or the range or one of those other products,” Duvak said. “So that’s the piece and the real technical challenge that they’re continuing to work on over the next few months. We’ve seen progress that they’ve made in those areas, but that’s the piece that they’re still working on.”", " Robert Stevens, an electronics engineer at the Radio Frequency Communications division, told C4ISRNET that the radios are an important piece of the next-generation combat vehicle. And Duvak said the Army’s tactical network modernization team — made up of the Network Cross-Functional Team and Program Executive Office Command, Control, Communications-Tactical — wants to use the radios as a mid-tier radio solution.", "The new funds will prevent emerging technology projects from falling into the \"valley of death.\"", " The development and fielding of new science and technology projects can take more than five years; however, the Army wants to speed that up as it seeks to modernize systems in preparation for future conflicts with near-peer adversaries. At last year’s Network Modernization Experiment, the C5ISR Center tested several vendors' radios to see where commercial technology stood.", "Sign up for the C4ISRNET newsletter about future battlefield technologies.", "For more newsletters click here", "Sign up for the C4ISRNET newsletter about future battlefield technologies.", "By giving us your email, you are opting in to the C4ISRNET Daily Brief.", " Alternative contracting options, like broad agency announcements as well as cooperative research and development agreements, have proved critical to quickening radio development. Under the contracting mechanisms, vendors and the Army have more flexibility to experiment with radios and make iterative modifications as requirements change.", " Duvak said this is different from how the Army did business years ago, when it would award yearslong contracts but eventually receive radios that no longer met current requirements.", " “What we were able to do at this program was, in just about a year and a half of development time, take a couple of those products that we saw that were very promising and we were able to add and actually fund vendors to enhance those radios with those resiliency features that we were just talking about for the contested environment,” Duvak said. “Things like making them anti-jam, or more difficult for the adversary to jam, making them more difficult for the adversary to detect or intercept our communications.”", " Duvak said the Army wants the new radio capabilities for Capability Set ’23, a collection of new tactical network tools to be fielded to soldiers in fiscal 2023. The resiliency of communications is critical as the tactical network modernization team pivots to reduce the electronic signature of the service’s command post under Capability Set ’23. The team is looking to increase bandwidth and reduce latency as part of that set of tools.", " Preliminary design review for Capability Set ’23 is scheduled for April next year.", "Andrew Eversden is a federal IT and cybersecurity reporter for the Federal Times and Fifth Domain. He previously worked as a congressional reporting fellow for the Texas Tribune and Washington intern for the Durango Herald. Andrew is a graduate of American University."]

remove1 = 'Sign up for the C4ISRNET newsletter about future battlefield technologies.'
remove2 = 'For more newsletters click here'
remove3 = 'Sign up for the C4ISRNET newsletter about future battlefield technologies.'
remove4 = 'By giving us your email, you are opting in to the C4ISRNET Daily Brief.'
test = [remove1, remove2, remove3, remove4]

tokens_list = []
for i in d:
    for t in i['content']:
        if t not in test:
            tokens_list.append(t)

a = ''.join(tokens_list)
sent_tokens = nltk.sent_tokenize(a)
json_file = {'tokens': sent_tokens}
with open(r'/home/miboj/Data-Science/NLP/document-summarizer/data/internal/cleaned/sent_tokens.json', 'x') as f:
    json.dump(json_file, f)




