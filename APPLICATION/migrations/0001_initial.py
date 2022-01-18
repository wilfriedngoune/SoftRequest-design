# Generated by Django 4.0.1 on 2022-01-15 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('nom_prenom', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('email_pass', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('departement', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('nom_prenom', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('matricule', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('filiere', models.CharField(max_length=20)),
                ('niveau', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('nom_grade', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Requete',
            fields=[
                ('id_request', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Abscence_note',
            fields=[
                ('requete_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='APPLICATION.requete')),
                ('unite_enseignement', models.CharField(max_length=7)),
                ('examen', models.CharField(max_length=10)),
            ],
            bases=('APPLICATION.requete',),
        ),
        migrations.CreateModel(
            name='Abscence_payement',
            fields=[
                ('requete_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='APPLICATION.requete')),
                ('matricule_etudiant', models.CharField(max_length=10)),
            ],
            bases=('APPLICATION.requete',),
        ),
        migrations.CreateModel(
            name='Activation_de_matricule',
            fields=[
                ('requete_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='APPLICATION.requete')),
                ('matricule_etudiant', models.CharField(max_length=10)),
            ],
            bases=('APPLICATION.requete',),
        ),
        migrations.CreateModel(
            name='Bloquage_matricule',
            fields=[
                ('requete_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='APPLICATION.requete')),
                ('matricule_etudiant', models.CharField(max_length=10)),
            ],
            bases=('APPLICATION.requete',),
        ),
        migrations.CreateModel(
            name='Changement_filiere',
            fields=[
                ('requete_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='APPLICATION.requete')),
                ('anciene_filiere', models.CharField(max_length=50)),
                ('new_filiere', models.CharField(max_length=50)),
            ],
            bases=('APPLICATION.requete',),
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('requete_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='APPLICATION.requete')),
                ('object_demande', models.TextField()),
            ],
            bases=('APPLICATION.requete',),
        ),
        migrations.CreateModel(
            name='Information_eronee',
            fields=[
                ('requete_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='APPLICATION.requete')),
                ('non_erronee', models.CharField(max_length=100)),
                ('matricule_erronee', models.CharField(max_length=7)),
                ('non_correct', models.CharField(max_length=100)),
                ('matricule_correct', models.CharField(max_length=7)),
            ],
            bases=('APPLICATION.requete',),
        ),
        migrations.CreateModel(
            name='Note_erronee',
            fields=[
                ('requete_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='APPLICATION.requete')),
                ('note_errone', models.FloatField()),
                ('note_correct', models.FloatField()),
                ('examen', models.CharField(max_length=30)),
                ('unite_enseignement', models.CharField(max_length=30)),
            ],
            bases=('APPLICATION.requete',),
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id_reponse', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('dateHeureRep', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=15)),
                ('requete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPLICATION.requete')),
            ],
        ),
        migrations.CreateModel(
            name='PieceJointe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_piece', models.CharField(max_length=50)),
                ('type_piece', models.CharField(max_length=10)),
                ('requete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPLICATION.requete')),
            ],
        ),
        migrations.CreateModel(
            name='Envoyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateHeureEnvoie', models.DateTimeField()),
                ('administration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPLICATION.administration')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPLICATION.etudiant')),
                ('requete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPLICATION.requete')),
            ],
        ),
        migrations.AddField(
            model_name='administration',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPLICATION.grade'),
        ),
    ]
