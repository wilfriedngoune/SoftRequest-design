# Generated by Django 4.0.1 on 2022-01-16 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APPLICATION', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note_erronee',
            name='requete_ptr',
        ),
        migrations.DeleteModel(
            name='Changement_filiere',
        ),
        migrations.DeleteModel(
            name='Note_erronee',
        ),
    ]
