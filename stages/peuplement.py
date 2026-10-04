from stages.models import *

# compétences
django = Competence.objects.create(libelle="Django")
python = Competence.objects.create(libelle="Python")

# entreprises
e1 = Entreprise.objects.create(nom="TechCorp", ville="Sokodé", email="a@a.com")
e2 = Entreprise.objects.create(nom="TelNet", ville="Sokodé", email="b@b.com")
e3 = Entreprise.objects.create(nom="BankX", ville="Lomé", email="c@c.com")

# étudiants
et1 = Etudiant.objects.create(nom="AMEZO", prenom="Grâce", sexe="F", date_naissance="2006-03-07", email="grace@mail.com", matricule="E1", promotion=2024)
et1.competences.add(django, python)

# offres
o1 = Offre.objects.create(entreprise=e1, titre="Dev", description="dveloppement d'application web...", date_debut="2026-01-01", date_fin="2026-03-01", nb_places=2)
o1.competences.add(django)


# candidature
c1 = Candidature.objects.create(etudiant=et1, offre=o1, statut="retenue")

# tuteur + enseignant
t = TuteurEntreprise.objects.create(nom="Kodjo", prenom="Moris", sexe="M", date_naissance="1990-01-01", email="moris@mail.com", entreprise=e1)
ens = EnseignantReferent.objects.create(nom="Yao", prenom="Amina", sexe="F", date_naissance="1985-01-01", email="amina@mail.com")

# stage
Stage.objects.create(candidature=c1, tuteur=t, enseignant=ens, sujet="Projet Django")