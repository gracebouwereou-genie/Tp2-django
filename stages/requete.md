#5.2 Six requêtes

#1- les offres des entreprises situées à Sokodé:
>>> Offre.objects.filter(entreprise__ville="Sokodé")
<QuerySet [<Offre: Offre object (1)>]>

#2- les étudiants qui possèdent la compétence « Django »:
>>> Etudiant.objects.filter(competences__libelle="Django")
<QuerySet [<Etudiant: Etudiant object (1)>]>

#3- les candidatures d’un étudiant donné, en partant de l’objet étudiant:
>>> etudiant = Etudiant.objects.first()
>>> etudiant.candidature_set.all()
<QuerySet [<Candidature: Candidature object (1)>]>

#4- le nombre de candidatures retenues, sans charger les candidatures en mémoire:
>>> Candidature.objects.filter(statut="retenue").count()
1
>>> 

#5- les stages dont l’offre vient d’une entreprise de Sokodé:
>>> Stage.objects.filter(candidature__offre__entreprise__ville="Sokodé")
<QuerySet [<Stage: Stage object (1)>]>

#6- les offres qui demandent au moins une compétence que possède un étudiant donné:
>>> Offre.objects.filter(competences__in=etudiant.competences.all())
<QuerySet [<Offre: Offre object (1)>]>

#Une offre peut correspondre à plusieurs compétences de l’étudiant, ce qui peut produire des doublons dans le résultat. L’utilisation de distinct() permet de supprimer ces doublons.

#6. Ce que la base accepte

#1. créations d'une offre qui se termine avant de commencer:
>>> Offre.objects.create( entreprise=Entreprise.objects.first(), titre="Test incohérent", description="...", date_debut="2026-12-10", date_fin="2026-01-01", nb_places=1)
<Offre: Offre object (2)>

#2. créations d'une offre dont le titre est une chaîne vide:
>>> Offre.objects.create( entreprise=Entreprise.objects.first(), titre="", description="test...", date_debut="2026-01-01", date_fin="2026-02-01", nb_places=1)
<Offre: Offre object (3)>

#3. créons deux fois la même candidature, pour le même étudiant et la même offre:
>>> etudiant = Etudiant.objects.first()
>>> offre = Offre.objects.first()
>>> 
>>> Candidature.objects.create(etudiant=etudiant, offre=offre, statut="deposee")
Traceback (most recent call last):
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py", line 360, in execute
    return super().execute(query, params)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
sqlite3.IntegrityError: UNIQUE constraint failed: stages_candidature.etudiant_id, stages_candidature.offre_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 665, in create
    obj.save(force_insert=True, using=self.db)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/base.py", line 902, in save
    self.save_base(
    ~~~~~~~~~~~~~~^
        using=using,
        ^^^^^^^^^^^^
    ...<2 lines>...
        update_fields=update_fields,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/base.py", line 1008, in save_base
    updated = self._save_table(
        raw,
    ...<4 lines>...
        update_fields,
    )
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/base.py", line 1169, in _save_table
    results = self._do_insert(
        cls._base_manager, using, fields, returning_fields, raw
    )
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/base.py", line 1210, in _do_insert
    return manager._insert(
           ~~~~~~~~~~~~~~~^
        [self],
        ^^^^^^^
    ...<3 lines>...
        raw=raw,
        ^^^^^^^^
    )
    ^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 1873, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/sql/compiler.py", line 1882, in execute_sql
    cursor.execute(sql, params)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 122, in execute
    return super().execute(sql, params)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        sql, params, many=False, executor=self._execute
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py", line 360, in execute
    return super().execute(query, params)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
django.db.utils.IntegrityError: UNIQUE constraint failed: stages_candidature.etudiant_id, stages_candidature.offre_id
>>> Candidature.objects.create(etudiant=etudiant, offre=offre, statut="deposee")
Traceback (most recent call last):
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py", line 360, in execute
    return super().execute(query, params)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
sqlite3.IntegrityError: UNIQUE constraint failed: stages_candidature.etudiant_id, stages_candidature.offre_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 665, in create
    obj.save(force_insert=True, using=self.db)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/base.py", line 902, in save
    self.save_base(
    ~~~~~~~~~~~~~~^
        using=using,
        ^^^^^^^^^^^^
    ...<2 lines>...
        update_fields=update_fields,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/base.py", line 1008, in save_base
    updated = self._save_table(
        raw,
    ...<4 lines>...
        update_fields,
    )
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/base.py", line 1169, in _save_table
    results = self._do_insert(
        cls._base_manager, using, fields, returning_fields, raw
    )
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/base.py", line 1210, in _do_insert
    return manager._insert(
           ~~~~~~~~~~~~~~~^
        [self],
        ^^^^^^^
    ...<3 lines>...
        raw=raw,
        ^^^^^^^^
    )
    ^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/query.py", line 1873, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/models/sql/compiler.py", line 1882, in execute_sql
    cursor.execute(sql, params)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 122, in execute
    return super().execute(sql, params)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        sql, params, many=False, executor=self._execute
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 92, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ifnti/Documents/AL3/Django (copie)/Projects/suivi_stages/.venv/lib/python3.14/site-packages/django/db/backends/sqlite3/base.py", line 360, in execute
    return super().execute(query, params)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
django.db.utils.IntegrityError: UNIQUE constraint failed: stages_candidature.etudiant_id, stages_candidature.offre_id
>>> 

#a. pour chacun de ces cas: les tests 1 et 2 sont acceptés mais le 3 est refusé
#b. les cas 1 et 2 relèvent du même problème car ce sont des règles métier non contrôlées.

