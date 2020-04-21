id_register = [ '10.5240/843E-C238-7F61-DDFC-F427-9',   # THE GODFATHER
                '10.5240/31CA-F962-3A40-18BD-BFA5-7',   # SHAWSHANK REDEMPTION
                '10.5240/A91C-90AE-1F45-6460-F6AC-U',   # GREEN MILE
                '10.5240/29E6-2D4B-B704-2B69-441F-8',   # TITANIC
                '10.5240/0EF3-54F9-2642-0B49-6829-R',   # INCEPTION
                '10.5240/5C04-098C-6377-F2C5-51B2-J',   # JOKER
                '10.5240/9AEF-D367-C3C0-A851-7D02-7',   # INTOUCHABLES
                '10.5240/B298-00A2-FE19-FF89-8CDD-Z',   # SEVENSAMURAI
              ]

movie_counter = len(id_register)

movies = {0: {'id':0, 'title':'The Godfather',            'eidr':id_register[0], 'year':'1972', 'director':'Francis Ford Coppola', 'books':'9786090138823,9786094840425'}, 
          1: {'id':1, 'title':'The Shawshank Redemption', 'eidr':id_register[1], 'year':'1994', 'director':'Frank Darabont',       'books':'9786098233254'},
          2: {'id':2, 'title':'The Green Mile',           'eidr':id_register[2], 'year':'1999', 'director':'Frank Darabont',       'books':'9786094840425'},
          3: {'id':3, 'title':'Titanic',                  'eidr':id_register[3], 'year':'1997', 'director':'James Cameron',        'books':'9786090138823'},
          4: {'id':4, 'title':'Inception',                'eidr':id_register[4], 'year':'2010', 'director':'Christopher Nolan',    'books':'9786090138823,9786098233254'},
          5: {'id':5, 'title':'Joker',                    'eidr':id_register[5], 'year':'2019', 'director':'Todd Phillips',        'books':'9786094840425,9786090138823,9786098233254'},
          6: {'id':6, 'title':'Intouchables',             'eidr':id_register[6], 'year':'2011', 'director':'Eric Toledano',        'books':'9786090138823'},
          7: {'id':7, 'title':'Shichinin no samurai',     'eidr':id_register[7], 'year':'1954', 'director':'Akira Kurosawa',       'books':'9786098233254,9786094840425'}
         }