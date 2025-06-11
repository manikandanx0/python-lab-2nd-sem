weeks = ['week-1',
         'week-2',
         'week-3',
         'week-4',
         'week-5',
         'week-6',
         'week-7',]

work =  ['-cod.pdf', '-cy.pdf', '-mcq.pdf', '-pah.pdf']

for w in weeks:
    for m in work:
        print(f"### [{w+ m.strip(".pdf")}](./{w}/{w+m})")