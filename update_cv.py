import os

file_path = r'c:\Users\kaissoune\Downloads\CV-main\CV-main\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Title
content = content.replace('<title>Abdallah Riziki - CV</title>', '<title>Daniati Ahamadi Ousseni - CV</title>')

# Replace Contact Info
old_contact = """          <div class="title">
            <p class="bold">Abdallah Riziki</p>
            <p class="regular"
              style="background: linear-gradient(135deg, #6a0dad, #1e3c72); color: white; text-align: center; padding: 1px 0; font-size: 24px; height: 31vh; display: flex; justify-content: center; align-items: center; flex-direction: column;">
              Assistante de gestion administrative
            </p>
          </div>
          <ul>
            <li>
              <div class="icon">
                <i class="fas fa-map"></i>
              </div>
              <div class="data">
                16 IMPASSE HARIRI BOINARIZIKI<br>97640 Sada
              </div>
            </li>
            <li>
              <div class="icon">
                <i class="fas fa-mobile-alt"></i>
              </div>
              <div class="data">
                0693522074
              </div>
            </li>
            <li>
              <div class="icon">
                <i class="fas fa-envelope"></i>
              </div>
              <div class="data">
                abdallahriziki61@gmail.com
              </div>
            </li>
          </ul>"""

new_contact = """          <div class="title">
            <p class="bold">Daniati Ahamadi Ousseni</p>
            <p class="regular"
              style="background: linear-gradient(135deg, #6a0dad, #1e3c72); color: white; text-align: center; padding: 1px 0; font-size: 24px; height: 31vh; display: flex; justify-content: center; align-items: center; flex-direction: column;">
              Assistante de Gestion Administrative<br><span style="font-size: 16px;">Spécialiste Petite Enfance</span>
            </p>
          </div>
          <ul>
            <li>
              <div class="icon">
                <i class="fas fa-map"></i>
              </div>
              <div class="data">
                Route du Lycée de Sada<br>97640 Sada
              </div>
            </li>
            <li>
              <div class="icon">
                <i class="fas fa-mobile-alt"></i>
              </div>
              <div class="data">
                06 39 26 64 60
              </div>
            </li>
            <li>
              <div class="icon">
                <i class="fas fa-envelope"></i>
              </div>
              <div class="data">
                ahamadidaniati32@gmail.com
              </div>
            </li>
          </ul>"""

content = content.replace(old_contact, new_contact)

old_right_section = """    <div class="resume_right">
      <div class="resume_item resume_about">
        <div class="title">
          <p class="bold">Mon Profil</p>
        </div>
        <p>Titulaire d'un <strong>Baccalauréat professionnel gestion administrative</strong>, j'ai développé de solides
          compétences en <strong>organisation, accueil client, et suivi administratif</strong> à travers mes différentes
          expériences professionnelles et formations. Je suis passionnée par l'efficacité administrative et je
          m'investis pleinement pour faciliter la gestion et l'organisation au sein d'une équipe.</p>
      </div>
      <div class="resume_item resume_work">
        <div class="title">
          <p class="bold">Expérience Professionnelle</p>
        </div>
        <ul>
          <li>
            <div class="date">20/09/21 - 12/05/22</div>
            <div class="info">
              <p class="semi-bold">AEJ (Association Accompagnement Éducatif des Jeunes)</p>
              <p>Accompagnement éducatif et gestion de projets.</p>
            </div>
          </li>
          <li>
            <div class="date">20/01/20 - 15/03/20</div>
            <div class="info">
              <p class="semi-bold">Stage Police Municipale, Sada</p>
              <p>Organisation de manifestations, accueil du public, rangement et archivage.</p>
            </div>
          </li>
          <li>
            <div class="date">09/09/19 - 13/01/21</div>
            <div class="info">
              <p class="semi-bold">Centre Auto Alonzo</p>
              <p>Gestion administrative, classement, mise à jour de dossiers, réalisation de devis.</p>
            </div>
          </li>
          <li>
            <div class="date">10/04/18 - 27/06/18</div>
            <div class="info">
              <p class="semi-bold">Permis Express</p>
              <p>Accueil et conseil aux clients.</p>
            </div>
          </li>
          <li>
            <div class="date">25/10/17 - 21/12/17</div>
            <div class="info">
              <p class="semi-bold">Gestion comptable et projet</p>
              <p>Suivi comptable et gestion de projet.</p>
            </div>
          </li>
          <li>
            <div class="date">Actuellement</div>
            <div class="info">
              <p class="semi-bold"> <strong>En recherche d'opportunités</strong></p>
              <p>✅ Motivée pour de nouveaux défis professionnels.</p>
            </div>
          </li>
        </ul>
      </div>
      <div class="resume_item resume_education">
        <div class="title">
          <p class="bold">Formations & Diplômes</p>
        </div>
        <ul>
          <li>
            <div class="date">2021</div>
            <div class="info">
              <p class="semi-bold">Lycée de Bandrelé</p>
              <p>Baccalauréat professionnel gestion administrative.</p>
            </div>
          </li>
          <li>
            <div class="date">2016</div>
            <div class="info">
              <p class="semi-bold">Collège de Chiconi</p>
              <p>Brevet des collèges.</p>
            </div>
          </li>
        </ul>
      </div>
      <div class="resume_item resume_certifications">
        <div class="title">
          <p class="bold">Compétences Complémentaires</p>
        </div>
        <ul>
          <li>Gestion des appels téléphoniques et courrier</li>
          <li>Actualisation des supports commerciaux</li>
          <li>Participation aux forums de recrutement</li>
          <li>Organisation des réunions et des voyages</li>
          <li>Facturation, acompte, solde et relances</li>
          <li>Saisie de documents et archivage</li>
          <li>Langue : Français (Courant/Maternel)</li>
        </ul>
      </div>
      <div class="resume_item resume_hobby">
        <div class="title">
          <p class="bold">Centres d'intérêt</p>
        </div>
        <ul>
          <li><i class="fas fa-book"></i> Lecture</li>
          <li><i class="fas fa-users"></i> Échanges professionnels</li>
          <li><i class="fas fa-music"></i> Musique classique</li>
          <li><i class="fab fa-pagelines"></i> Nature & Découvertes</li>
        </ul>
      </div>
    </div>"""

new_right_section = """    <div class="resume_right">
      <div class="resume_item resume_about">
        <div class="title">
          <p class="bold">Mon Profil</p>
        </div>
        <p>Professionnelle dynamique et rigoureuse, je bénéficie d'une double expertise en gestion administrative et en accompagnement éducatif (AEPE). Reconnue pour mon sens de l’organisation et mon aisance relationnelle, je maîtrise la gestion des flux documentaires ainsi que l’accueil de publics variés. Motivée et polyvalente, je m’adapte rapidement à de nouveaux environnements pour contribuer efficacement à la réussite de votre structure.</p>
      </div>
      <div class="resume_item resume_work">
        <div class="title">
          <p class="bold">Expériences Professionnelles</p>
        </div>
        <ul>
          <li>
            <div class="date">13/02/19 - 29/03/19</div>
            <div class="info">
              <p class="semi-bold">Stagiaire Accompagnement Éducatif (AEPE) | École Owa Zaza, Sada</p>
              <p><strong>Accueil & Communication :</strong> Accueillir les familles et assurer la transmission des informations quotidiennes.<br>
              <strong>Animation :</strong> Organiser et encadrer des ateliers d'éveil et des activités pédagogiques.<br>
              <strong>Hygiène & Sécurité :</strong> Veiller au respect strict des protocoles sanitaires et assurer la sécurité des jeunes enfants.</p>
            </div>
          </li>
          <li>
            <div class="date">14/05/17 - 18/06/17</div>
            <div class="info">
              <p class="semi-bold">Assistante d'Éducation Maternelle | École Maternelle de Mangajou</p>
              <p><strong>Soutien Pédagogique :</strong> Assister l'enseignant dans la préparation et le bon déroulement des activités de classe.<br>
              <strong>Gestion de Groupe :</strong> Encadrer les enfants durant les temps de repas et de repos.<br>
              <strong>Entretien :</strong> Assurer la propreté et l'organisation des espaces de vie enfantins.</p>
            </div>
          </li>
        </ul>
      </div>
      <div class="resume_item resume_education">
        <div class="title">
          <p class="bold">Formations & Diplômes</p>
        </div>
        <ul>
          <li>
            <div class="date">En cours</div>
            <div class="info">
              <p class="semi-bold">Spécialisation</p>
              <p>Formation en Gestion Administrative.</p>
            </div>
          </li>
          <li>
            <div class="date">Terminé</div>
            <div class="info">
              <p class="semi-bold">Lycée Professionnel de Kahani</p>
              <p>CAP Accompagnement Éducatif Petite Enfance (AEPE).</p>
            </div>
          </li>
          <li>
            <div class="date">Juillet 2017</div>
            <div class="info">
              <p class="semi-bold">Collège de Sada</p>
              <p>Diplôme National du Brevet.</p>
            </div>
          </li>
        </ul>
      </div>
      <div class="resume_item resume_certifications">
        <div class="title">
          <p class="bold">Compétences Complémentaires</p>
        </div>
        <ul>
          <li><strong>Langues :</strong> Français (Courant – 100%).</li>
          <li><strong>Activités :</strong> Participation active aux forums et événements locaux pour la promotion de la gestion administrative.</li>
        </ul>
      </div>
    </div>"""

content = content.replace(old_right_section, new_right_section)

old_skills = """        <div class="resume_item resume_skills">
          <div class="title">
            <p class="bold">Compétences Techniques</p>
          </div>
          <ul>
            <li>
              <div class="skill_name">
                Gestion des appels
              </div>
              <div class="skill_progress">
                <span style="width: 80%;"></span>
              </div>
              <div class="skill_per">80%</div>
            </li>
            <li>
              <div style="background-color: rgba(177, 128, 22, 0.836);" class="skill_name">
                Actualisation supports
              </div>
              <div class="skill_progress">
                <span style="width: 80%;"></span>
              </div>
              <div class="skill_per">80%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Participation forums
              </div>
              <div class="skill_progress">
                <span style="width: 70%;"></span>
              </div>
              <div class="skill_per">70%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Tenue de l'agenda
              </div>
              <div class="skill_progress">
                <span style="width: 70%;"></span>
              </div>
              <div class="skill_per">70%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Organisation réunions
              </div>
              <div class="skill_progress">
                <span style="width: 90%;"></span>
              </div>
              <div class="skill_per">90%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Saisie de documents
              </div>
              <div class="skill_progress">
                <span style="width: 90%;"></span>
              </div>
              <div class="skill_per">90%</div>
            </li>
            <li>
              <div class="skill_name">
                Archivage
              </div>
              <div class="skill_progress">
                <span style="width: 88%;"></span>
              </div>
              <div class="skill_per">88%</div>
            </li>
            <li>
              <div class="skill_name">
                Gestion fournitures
              </div>
              <div class="skill_progress">
                <span style="width: 88%;"></span>
              </div>
              <div class="skill_per">88%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Facturation
              </div>
              <div class="skill_progress">
                <span style="width: 89%;"></span>
              </div>
              <div class="skill_per">89%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Suivi des paiements
              </div>
              <div class="skill_progress">
                <span style="width: 89%;"></span>
              </div>
              <div class="skill_per">89%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Français
              </div>
              <div class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">100%</div>
            </li>
          </ul>
        </div>
        <div class="resume_item resume_skills">
          <div class="title">
            <p class="bold">Savoir-être</p>
          </div>
          <ul>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                → Capacité d'adaptation
              </div>
              <div style="background-color: rgba(177, 128, 22, 0.795)" class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">
                <i style="color: white;" class="fas fa-sync-alt"></i>
              </div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                → Aisance relationnelle
              </div>
              <div class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">
                <i style="color: white;" class="fas fa-comments"></i>
              </div>
            </li>
            <li>
              <div class="skill_name">
                → Esprit d'équipe
              </div>
              <div class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">
                <i style="color: white;" class="fas fa-users"></i>
              </div>
            </li>
            <li>
              <div class="skill_name">
                → Sens de l'organisation
              </div>
              <div class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">
                <i class="fas fa-lightbulb" style="color: white;"></i>
              </div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                → Sens de l'accueil
              </div>
              <div class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">
                <i style="color: white;" class="fas fa-smile"></i>
              </div>
            </li>
          </ul>
        </div>
        <div class="resume_item resume_social">
          <div class="title">
            <p class="bold">Réseaux Sociaux</p>
          </div>
          <ul>
            <li>
              <div class="icon">
                <i class="fab fa-facebook-square"></i>
              </div>
              <div class="data">
                <p class="semi-bold" style="background-color: rgb(188, 207, 207);">Facebook</p>
                <p style="background-color: rgba(170, 27, 170, 0.795)">Abdallah Riziki</p>
              </div>
            </li>
            <li>
              <div class="icon">
                <i class="fab fa-instagram-square"></i>
              </div>
              <div class="data">
                <p class="semi-bold" style="background-color: rgb(188, 207, 207);">Instagram</p>
                <p style="background-color: rgba(170, 27, 170, 0.795)">abdallahriziki</p>
              </div>
            </li>
            <li>
              <div class="icon">
                <i class="fab fa-linkedin"></i>
              </div>
              <div class="data">
                <p class="semi-bold" style="background-color: rgb(188, 207, 207);">LinkedIn</p>
                <p style="background-color: rgba(170, 27, 170, 0.795)">abdallah-riziki</p>
              </div>
            </li>
          </ul>
        </div>"""

new_skills = """        <div class="resume_item resume_skills">
          <div class="title">
            <p class="bold">Compétences Clés</p>
          </div>
          <ul>
            <li>
              <div class="skill_name">
                Saisie & rédaction
              </div>
              <div class="skill_progress">
                <span style="width: 90%;"></span>
              </div>
              <div class="skill_per">90%</div>
            </li>
            <li>
              <div style="background-color: rgba(177, 128, 22, 0.836);" class="skill_name">
                Archivage & classement
              </div>
              <div class="skill_progress">
                <span style="width: 88%;"></span>
              </div>
              <div class="skill_per">88%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Agenda & réunions
              </div>
              <div class="skill_progress">
                <span style="width: 90%;"></span>
              </div>
              <div class="skill_per">90%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Stocks & fournitures
              </div>
              <div class="skill_progress">
                <span style="width: 88%;"></span>
              </div>
              <div class="skill_per">88%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Aide à la facturation
              </div>
              <div class="skill_progress">
                <span style="width: 89%;"></span>
              </div>
              <div class="skill_per">89%</div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                Suivi des paiements
              </div>
              <div class="skill_progress">
                <span style="width: 89%;"></span>
              </div>
              <div class="skill_per">89%</div>
            </li>
            <li>
              <div class="skill_name">
                Pack Office & appels
              </div>
              <div class="skill_progress">
                <span style="width: 90%;"></span>
              </div>
              <div class="skill_per">90%</div>
            </li>
          </ul>
        </div>
        <div class="resume_item resume_skills">
          <div class="title">
            <p class="bold">Savoir-être (Soft Skills)</p>
          </div>
          <ul>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                → Sens de l'accueil
              </div>
              <div style="background-color: rgba(177, 128, 22, 0.795)" class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">
                <i style="color: white;" class="fas fa-smile"></i>
              </div>
            </li>
            <li>
              <div class="skill_name" style="background-color: rgba(177, 128, 22, 0.795)">
                → Esprit d'équipe
              </div>
              <div class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">
                <i style="color: white;" class="fas fa-users"></i>
              </div>
            </li>
            <li>
              <div class="skill_name">
                → Adaptabilité
              </div>
              <div class="skill_progress">
                <span style="width: 100%;"></span>
              </div>
              <div class="skill_per">
                <i style="color: white;" class="fas fa-sync-alt"></i>
              </div>
            </li>
          </ul>
        </div>
        <div class="resume_item resume_social">
          <div class="title">
            <p class="bold">Réseaux Sociaux</p>
          </div>
          <ul>
            <li>
              <div class="icon">
                <i class="fab fa-facebook-square"></i>
              </div>
              <div class="data">
                <p class="semi-bold" style="background-color: rgb(188, 207, 207);">Facebook</p>
                <p style="background-color: rgba(170, 27, 170, 0.795)">Daniati Ahamadi</p>
              </div>
            </li>
            <li>
              <div class="icon">
                <i class="fab fa-instagram-square"></i>
              </div>
              <div class="data">
                <p class="semi-bold" style="background-color: rgb(188, 207, 207);">Instagram</p>
                <p style="background-color: rgba(170, 27, 170, 0.795)">daniatiahamadi</p>
              </div>
            </li>
            <li>
              <div class="icon">
                <i class="fab fa-linkedin"></i>
              </div>
              <div class="data">
                <p class="semi-bold" style="background-color: rgb(188, 207, 207);">LinkedIn</p>
                <p style="background-color: rgba(170, 27, 170, 0.795)">daniati-ahamadi</p>
              </div>
            </li>
          </ul>
        </div>"""

content = content.replace(old_skills, new_skills)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html successfully")
