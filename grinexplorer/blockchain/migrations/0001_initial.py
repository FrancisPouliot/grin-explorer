# Generated by Django 2.0 on 2017-12-14 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('hash', models.CharField(db_index=True, max_length=64, primary_key=True, serialize=False)),
                ('version', models.IntegerField()),
                ('height', models.IntegerField(db_index=True)),
                ('timestamp', models.DateTimeField()),
                ('utxo_root', models.CharField(max_length=64)),
                ('range_proof_root', models.CharField(max_length=64)),
                ('kernel_root', models.CharField(max_length=64)),
                ('nonce', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('total_difficulty', models.IntegerField()),
                ('previous', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children_set', to='blockchain.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=66)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blockchain.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Kernel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.TextField()),
                ('fee', models.IntegerField()),
                ('lock_height', models.IntegerField()),
                ('excess', models.CharField(max_length=66)),
                ('excess_sig', models.CharField(max_length=142)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blockchain.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_type', models.TextField(choices=[('Transaction', 'Transaction'), ('Coinbase', 'Coinbase')])),
                ('commit', models.CharField(max_length=66)),
                ('switch_commit_hash', models.CharField(max_length=40)),
                ('height', models.IntegerField()),
                ('lock_height', models.IntegerField()),
                ('spent', models.BooleanField()),
                ('proof_hash', models.CharField(max_length=64)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blockchain.Block')),
            ],
        ),
    ]