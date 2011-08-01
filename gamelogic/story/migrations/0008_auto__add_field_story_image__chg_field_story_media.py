# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Story.image'
        db.add_column('story_story', 'image', self.gf('django.db.models.fields.files.ImageField')(default=datetime.date(2011, 8, 1), max_length=100), keep_default=False)

        # Changing field 'Story.media'
        db.alter_column('story_story', 'media', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    def backwards(self, orm):
        
        # Deleting field 'Story.image'
        db.delete_column('story_story', 'image')

        # Changing field 'Story.media'
        db.alter_column('story_story', 'media', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        'story.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'story_question_answer_goes_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'story_destination'", 'to': "orm['story.Story']"}),
            'story_question_appears_on': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'story_question'", 'to': "orm['story.Story']"})
        },
        'story.story': {
            'Meta': {'ordering': "('key',)", 'object_name': 'Story'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'editorial_alpha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'editorial_beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'editorial_gold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'media': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
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
