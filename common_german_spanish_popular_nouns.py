with open('spanish_english.txt', 'r') as f:
    lines = f.readlines()

english_spanish_words = []
english_spanish_words_masc = []
english_spanish_words_fem = []
english_spanish_dict = {}

for line in lines:
    
    word, translation = line.strip().split('–')
    english_spanish_word = word.split('.')[1].strip()
    spanish = translation.strip()
    article = spanish.split(' ')[0]
    
    if(article == 'el'):
        english_spanish_words_masc.append(english_spanish_word)
    else:
        english_spanish_words_fem.append(english_spanish_word)
    
    english_spanish_words.append(english_spanish_word)
    english_spanish_dict[english_spanish_word] = spanish
        
        
with open('german_english.txt', 'r') as f:
    lines = f.readlines()
    
english_german_words = []
english_german_words_masc = []
english_german_words_fem = []
english_german_words_neut = []
english_german_dict = {}

for line in lines:
    word, translation = line.strip().split('–')
    english_german_word = word.split('.')[1].strip()
    german = translation.strip()
    article = german.split(' ')[0]
    
    if(article == 'Der'):
        english_german_words_masc.append(english_german_word)
    elif(article == 'Die'):
        english_german_words_fem.append(english_german_word)
    else:
        english_german_words_neut.append(english_german_word)
        
    english_german_words.append(english_german_word)
    english_german_dict[english_german_word] = german


common_words = set(english_spanish_words) & set(english_german_words)
common_words_masc = set(english_spanish_words_masc) & set(english_german_words_masc)
common_words_fem = set(english_spanish_words_fem) & set(english_german_words_fem)
        
common_words_ordered = [x for x in english_spanish_words + english_german_words if x in common_words]
        
new_dict = {}  
for key in common_words_ordered:
    new_dict[key] = [english_german_dict[key], english_spanish_dict[key]] 
    
with open('most_popular_both_german_spanish.txt', 'w') as f:
    for key in new_dict:
        f.write(key + ': ' + str(new_dict[key]) + '\n')
        
new_dict = {}  
for key in common_words_masc:
    new_dict[key] = [english_german_dict[key], english_spanish_dict[key]] 
    
with open('most_popular_both_german_spanish_masc.txt', 'w') as f:
    for key in new_dict:
        f.write(key + ': ' + str(new_dict[key]) + '\n')
        
new_dict = {}  
for key in common_words_fem:
    new_dict[key] = [english_german_dict[key], english_spanish_dict[key]] 
    
with open('most_popular_both_german_spanish_fem.txt', 'w') as f:
    for key in new_dict:
        f.write(key + ': ' + str(new_dict[key]) + '\n')