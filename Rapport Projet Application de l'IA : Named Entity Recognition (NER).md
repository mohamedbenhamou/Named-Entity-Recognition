# Rapport Projet Application de l'IA : Named Entity Recognition (NER)

- Ben Hamou Mohamed
- El Housni Youssef
- Mouhat Aiman
- Laouan Ilyaas

SpaCy est une bibliothèque populaire de traitement du langage naturel (NLP) qui fournit des modèles pré-entraînés pour diverses tâches, y compris la reconnaissance des entités nommées (NER). Dans ce rapport, nous allons examiner comment SpaCy peut être utilisé pour la NER et présenter un exemple de texte que nous avons testé avec cet outil.

## SpaCy et la reconnaissance des entités nommées (NER)

SpaCy propose plusieurs modèles pré-entraînés qui incluent des informations sur les entités nommées. Par exemple, le modèle "en_core_web_lg" pour l'anglais est capable de reconnaître les entités nommées telles que les personnes, les lieux, les dates, les organisations, etc.

La reconnaissance des entités nommées est réalisée en utilisant des techniques d'apprentissage automatique pour identifier et classer les séquences de mots qui correspondent à des entités spécifiques. Ces modèles pré-entraînés de SpaCy sont entraînés sur de grandes quantités de données annotées et sont capables de détecter les entités dans de nouveaux textes.

## Exemple de texte testé avec SpaCy

Voici un exemple de texte avec lequel nous avons testé l'outil SpaCy pour la NER :


My name is Robinson. I am from England. I am eighteen years old. My father is German. My mother is English. I have two brothers. I have one sister. We are a good family.
My father is a good businessman. We have money. I have a good school. I have a good life. But I have a dream. I want to travel. I want to see the world.
My father is a good man. He wants the best for me. But my dream is not his dream. He is not happy. The situation is not easy.
It is morning. My father is in his room. He wants to speak with me. I go to his room. My father has some questions. My father wants to know why I want to travel.
My father says, “Travelling is dangerous. Travelling is not comfortable. You can die.”
I think about it. Travelling is dangerous. It is not comfortable. I can die. But it is also very interesting. I can see new countries. I can meet new people.
I think about travelling every day. Maybe my mother can help me.
I speak with my mother. I tell my mother, “I want to travel. I want to see the world. Please, speak with my father. Maybe with your help, I can travel.”
My mother loves me. But she thinks that travelling is dangerous. She thinks that my place is at home. She thinks that life in England is the best for me.
One year later, I visit one big town. The name of this town is Hull.
I meet my friend. His father has a ship. They travel to London. My friend tells me, “Go with me.”
I think about it. I am not prepared. But I can try if travelling is for me.
I go to London. I am very happy. It is my first long journey. It is very interesting. The first hour is good. But then we have problems. We see a storm. The storm is big.
The wind is strong. The ship goes up and down. I have fear. I think about my home. I think about my comfortable bed.
The storm is finished in the morning. The weather is nice. And the evening is beautiful. Everything is quiet.
One man comes to me. We speak. We speak about the storm. I speak about my fear. The man gives me a drink. I drink very much. I sleep very well at night.
The next day, I forget about my home. I forget about my comfortable bed. I dream more about travelling.

En utilisant le modèle "en_core_web_lg" de SpaCy, nous avons extrait les entités nommées suivantes :

- Robinson (PERSON)
- England (GPE)
- eighteen years old (DATE)
- German (NORP)
- English (LANGUAGE)
- two (CARDINAL)
- one (CARDINAL)
- One year later (DATE)
- Hull (GPE)
- London (GPE)
- first (ORDINAL)
- The first hour (TIME)
- the morning (TIME)
- One (CARDINAL)
- night (TIME)
- The next day (DATE)

Ces entités ont été détectées par SpaCy en utilisant son modèle pré-entraîné pour la langue anglaise. Chaque entité est associée à un label correspondant à son type, tel que PERSON, GPE, DATE, NORP, LANGUAGE, CARDINAL, ORDINAL ou TIME.

## Conclusion

SpaCy est un outil puissant pour la reconnaissance des entités nommées, offrant des modèles pré-entraînés et performants dans différentes langues. Il peut être utilisé pour extraire des informations structurées à partir de textes non structurés, ce qui est utile dans de nombreux domaines d'application du traitement du langage naturel.

Dans cet exemple, SpaCy a réussi à détecter les entités nommées dans le texte fourni, fournissant des informations telles que les noms de personnes, les lieux, les dates, les nombres, etc. Cependant, il est important de noter que les modèles pré-entraînés ne fournissent pas de scores de confiance par défaut pour les entités détectées.

Pour des cas d'utilisation plus spécifiques ou pour obtenir des scores de confiance, il est possible de former des modèles personnalisés avec des données annotées. SpaCy offre également des fonctionnalités avancées pour le traitement du langage naturel, telles que l'analyse syntaxique, la lemmatisation, le marquage de partie du discours, entre autres.

En résumé, SpaCy est un outil essentiel pour la NER et d'autres tâches de traitement du langage naturel, offrant des fonctionnalités puissantes et des modèles pré-entraînés de qualité.

