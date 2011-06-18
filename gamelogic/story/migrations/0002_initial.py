# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Story'
        db.create_table('story_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('editorial_alpha', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('science_alpha', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('editorial_beta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('science_beta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('editorial_gold', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('science_gold', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal('story', ['Story'])

        # Adding M2M table for field parent on 'Story'
        db.create_table('story_story_parent', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_story', models.ForeignKey(orm['story.story'], null=False)),
            ('to_story', models.ForeignKey(orm['story.story'], null=False))
        ))
        db.create_unique('story_story_parent', ['from_story_id', 'to_story_id'])

        # Adding M2M table for field child on 'Story'
        db.create_table('story_story_child', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_story', models.ForeignKey(orm['story.story'], null=False)),
            ('to_story', models.ForeignKey(orm['story.story'], null=False))
        ))
        db.create_unique('story_story_child', ['from_story_id', 'to_story_id'])

    def backwards(self, orm):
        
        # Deleting model 'Story'
        db.delete_table('story_story')

        # Removing M2M table for field parent on 'Story'
        db.delete_table('story_story_parent')

        # Removing M2M table for field child on 'Story'
        db.delete_table('story_story_child')

    models = {
        'story.story': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Story'},
            'child': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'story_child'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['story.Story']"}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'editorial_alpha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'editorial_beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'editorial_gold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'story_parent'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['story.Story']"}),
            'science_alpha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'science_beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'science_gold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['story']
