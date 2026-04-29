import os

file_path = r'c:\Users\kaissoune\Downloads\CV-main\CV-main\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Mon Profil
old_profil = """<p>Professionnelle dynamique et rigoureuse, je bénéficie d'une double expertise en gestion administrative et en accompagnement éducatif (AEPE). Reconnue pour mon sens de l’organisation et mon aisance relationnelle, je maîtrise la gestion des flux documentaires ainsi que l’accueil de publics variés. Motivée et polyvalente, je m’adapte rapidement à de nouveaux environnements pour contribuer efficacement à la réussite de votre structure.</p>"""

new_profil = """<p><strong>Professionnelle dynamique et rigoureuse</strong>, je bénéficie d'une <strong>double expertise</strong> en <strong>gestion administrative</strong> et en <strong>accompagnement éducatif (AEPE)</strong>. Reconnue pour mon <strong>sens de l’organisation</strong> et mon <strong>aisance relationnelle</strong>, je maîtrise la <strong>gestion des flux documentaires</strong> ainsi que l’<strong>accueil de publics variés</strong>. <strong>Motivée et polyvalente</strong>, je m’adapte rapidement à de nouveaux environnements pour <strong>contribuer efficacement</strong> à la réussite de votre structure.</p>"""

content = content.replace(old_profil, new_profil)

# Replace Experience 1
old_exp1 = """<p><strong>Accueil & Communication :</strong> Accueillir les familles et assurer la transmission des informations quotidiennes.<br>
              <strong>Animation :</strong> Organiser et encadrer des ateliers d'éveil et des activités pédagogiques.<br>
              <strong>Hygiène & Sécurité :</strong> Veiller au respect strict des protocoles sanitaires et assurer la sécurité des jeunes enfants.</p>"""

new_exp1 = """<p><strong>Accueil & Communication :</strong> <strong>Accueillir les familles</strong> et assurer la <strong>transmission des informations</strong> quotidiennes.<br>
              <strong>Animation :</strong> <strong>Organiser et encadrer</strong> des <strong>ateliers d'éveil</strong> et des <strong>activités pédagogiques</strong>.<br>
              <strong>Hygiène & Sécurité :</strong> Veiller au <strong>respect strict des protocoles sanitaires</strong> et assurer la <strong>sécurité des jeunes enfants</strong>.</p>"""

content = content.replace(old_exp1, new_exp1)

# Replace Experience 2
old_exp2 = """<p><strong>Soutien Pédagogique :</strong> Assister l'enseignant dans la préparation et le bon déroulement des activités de classe.<br>
              <strong>Gestion de Groupe :</strong> Encadrer les enfants durant les temps de repas et de repos.<br>
              <strong>Entretien :</strong> Assurer la propreté et l'organisation des espaces de vie enfantins.</p>"""

new_exp2 = """<p><strong>Soutien Pédagogique :</strong> <strong>Assister l'enseignant</strong> dans la <strong>préparation</strong> et le bon déroulement des <strong>activités de classe</strong>.<br>
              <strong>Gestion de Groupe :</strong> <strong>Encadrer les enfants</strong> durant les temps de repas et de repos.<br>
              <strong>Entretien :</strong> Assurer la <strong>propreté</strong> et l'<strong>organisation des espaces de vie</strong> enfantins.</p>"""

content = content.replace(old_exp2, new_exp2)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Highlighted index.html successfully")
